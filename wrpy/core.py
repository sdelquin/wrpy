import re

import requests
import user_agent
from bs4 import BeautifulSoup

from wrpy import services

WR_URL = 'https://www.wordreference.com/'
TRANSLATION_URL = WR_URL + '{dict_code}/{word}'


def get_available_dicts(lang_filter: str = None):
    ua = user_agent.generate_user_agent()
    response = requests.get(WR_URL, headers={'User-Agent': ua})
    soup = BeautifulSoup(response.text, 'html.parser')
    select = soup.find('select', id='fSelect')
    dicts = {}
    for optgroup in select.find_all('optgroup'):
        for option in optgroup.find_all('option', string=re.compile(r'.*-.*')):
            from_lang_label, to_lang_label = option.string.strip().split('-')
            from_lang_code, to_lang_code = option['id'][:2], option['id'][2:]
            if lang_filter is not None and lang_filter.lower() not in [
                from_lang_code.lower(),
                from_lang_label.lower(),
                to_lang_code.lower(),
                to_lang_label.lower(),
            ]:
                continue
            from_to_lang_code = from_lang_code + to_lang_code
            dicts[from_to_lang_code] = {
                'from': from_lang_label,
                'to': to_lang_label,
            }
    return dicts


class WordReference:
    def __init__(self, dict_code: str):
        self.dict_code = dict_code.lower()
        available_dicts = get_available_dicts()
        if self.dict_code not in available_dicts:
            raise NotImplementedError(
                f'{dict_code} is not available as a translation dictionary'
            )
        self.from_lang = available_dicts[self.dict_code]['from']
        self.to_lang = available_dicts[self.dict_code]['to']
        self.user_agent = user_agent.generate_user_agent()

    def translate(self, word):
        url = TRANSLATION_URL.format(dict_code=self.dict_code, word=word)
        response = requests.get(url, headers={'User-Agent': self.user_agent})
        soup = BeautifulSoup(response.text, 'html.parser')

        translation = dict(
            word=word,
            from_lang=self.from_lang,
            to_lang=self.to_lang,
            url=url,
            translations=[],
        )

        for table in soup.find_all('table', 'WRD'):
            entries = []
            last_row_class = 'even'  # each row starts with even class (0-index)
            entry = []
            for tr in table.find_all('tr', ['even', 'odd']):
                current_row_class = tr['class'][0]
                if current_row_class != last_row_class:
                    entries.append(services.parse_entry(entry))
                    entry = []
                    last_row_class = current_row_class
                entry.append(tr)
            if entry:
                entries.append(services.parse_entry(entry))

            section_title = table.tr.td['title']
            for section in translation['translations']:
                if section['title'] == section_title:
                    break
            else:
                section = {'title': section_title, 'entries': []}
                translation['translations'].append(section)
            section['entries'].extend(entries)

        return translation
