from pprint import pprint

from wrpy import WordReference

wr = WordReference('ES', 'en')
translation = wr.translate('avión')
pprint(translation)
