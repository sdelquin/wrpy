import requests
import user_agent
from bs4 import BeautifulSoup

from wrpy import services

TRANSLATION_URL = 'https://www.wordreference.com/{from_lang}{to_lang}/{word}'


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
