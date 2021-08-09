import requests
import user_agent
from bs4 import BeautifulSoup

from wrpy import services

TRANSLATION_URL = 'https://www.wordreference.com/esen/{text}'


class WordReference:
    def __init__(self):
        self.user_agent = user_agent.generate_user_agent()

    def translate(self, text):
        url = TRANSLATION_URL.format(text=text)
        response = requests.get(url, headers={'User-Agent': self.user_agent})
        soup = BeautifulSoup(response.text, 'html.parser')

        self.sections = []
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
            for section in self.sections:
                if section['title'] == section_title:
                    break
            else:
                section = {'title': section_title, 'entries': []}
                self.sections.append(section)
            section['entries'].extend(entries)
