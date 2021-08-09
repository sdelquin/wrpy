from pprint import pprint

from wrpy import WordReference

wr = WordReference()
wr.translate('avión')

pprint(wr.sections)
