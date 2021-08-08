from typing import DefaultDict

import requests
import user_agent
from bs4 import BeautifulSoup

TRANSLATION_URL = 'https://www.wordreference.com/esen/{text}'


class WordReference:
    def __init__(self):
        self.user_agent = user_agent.generate_user_agent()

    def translate(self, text):
        url = TRANSLATION_URL.format(text=text)
        response = requests.get(url, headers={'User-Agent': self.user_agent})
        soup = BeautifulSoup(response.text, 'html.parser')

        self.sections = DefaultDict(list)
        for section in soup.find_all('table', 'WRD'):
            section_title = section.tr.td['title']
            last_row_class = 'even'
            lines = []
            for tr in section.find_all('tr', ['even', 'odd']):
                current_row_class = tr['class'][0]
                if current_row_class != last_row_class:
                    self.sections[section_title].append(lines)
                    lines = []
                    last_row_class = current_row_class
                lines.append(tr)
            if lines:
                self.sections[section_title].append(lines)
