from pprint import pprint

from wrpy import WordReference

wr = WordReference('es', 'en')
translation = wr.translate('avión')
pprint(translation)
