import re

import requests
import user_agent
from bs4 import BeautifulSoup

from wrpy import services

WR_URL = 'https://www.wordreference.com/'
TRANSLATION_URL = WR_URL + '{from_lang}{to_lang}/{word}'


def get_available_langs():
    ua = user_agent.generate_user_agent()
    response = requests.get(WR_URL, headers={'User-Agent': ua})
    soup = BeautifulSoup(response.text, 'html.parser')
    select = soup.find('select', id='fSelect')
    langs = []
    for optgroup in select.find_all('optgroup'):
        for option in optgroup.find_all('option', string=re.compile(r'.*-.*')):
            from_lang_label, to_lang_label = option.string.strip().split('-')
            from_lang_code, to_lang_code = option['id'][:2], option['id'][2:]
            langs.append(
                dict(
                    from_lang_label=from_lang_label,
                    from_lang_code=from_lang_code,
                    to_lang_label=to_lang_label,
                    to_lang_code=to_lang_code,
                )
            )
    return langs


class WordReference:
    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.user_agent = user_agent.generate_user_agent()

    def translate(self, word):
        url = TRANSLATION_URL.format(
            from_lang=self.from_lang, to_lang=self.to_lang, word=word
        )
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
