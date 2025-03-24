# wrpy

This is a Python package to obtain translations from [wordreference.com](https://wordreference.com) transforming returned data into normalized and structured datatypes.

## Installation

```console
$ pip install wrpy
```

## Usage

You can get the **available dictionaries** using the following function:

```pycon
>>> from wrpy import get_available_dicts

>>> get_available_dicts()
{'enes': {'from': 'English', 'to': 'Spanish'},
 'esen': {'from': 'Spanish', 'to': 'English'},
 'esfr': {'from': 'Spanish', 'to': 'French'},
 'espt': {'from': 'Spanish', 'to': 'Portuguese'},
 'esit': {'from': 'Spanish', 'to': 'Italian'},
 'esde': {'from': 'Spanish', 'to': 'German'},
 'esca': {'from': 'Spanish', 'to': 'Catalan'},
 'enfr': {'from': 'English', 'to': 'French'},
 'fren': {'from': 'French', 'to': 'English'},
 'fres': {'from': 'French', 'to': 'Spanish'},
 'enit': {'from': 'English', 'to': 'Italian'},
 'iten': {'from': 'Italian', 'to': 'English'},
 'ites': {'from': 'Italian', 'to': 'Spanish'},
 'ende': {'from': 'English', 'to': 'German'},
 'deen': {'from': 'German', 'to': 'English'},
 'dees': {'from': 'German', 'to': 'Spanish'},
 'ennl': {'from': 'English', 'to': 'Dutch'},
 'nlen': {'from': 'Dutch', 'to': 'English'},
 'ensv': {'from': 'English', 'to': 'Swedish'},
 'sven': {'from': 'Swedish', 'to': 'English'},
 'enru': {'from': 'English', 'to': 'Russian'},
 'ruen': {'from': 'Russian', 'to': 'English'},
 'enpt': {'from': 'English', 'to': 'Portuguese'},
 'pten': {'from': 'Portuguese', 'to': 'English'},
 'ptes': {'from': 'Portuguese', 'to': 'Spanish'},
 'enpl': {'from': 'English', 'to': 'Polish'},
 'plen': {'from': 'Polish', 'to': 'English'},
 'enro': {'from': 'English', 'to': 'Romanian'},
 'roen': {'from': 'Romanian', 'to': 'English'},
 'encz': {'from': 'English', 'to': 'Czech'},
 'czen': {'from': 'Czech', 'to': 'English'},
 'engr': {'from': 'English', 'to': 'Greek'},
 'gren': {'from': 'Greek', 'to': 'English'},
 'entr': {'from': 'English', 'to': 'Turkish'},
 'tren': {'from': 'Turkish', 'to': 'English'},
 'enzh': {'from': 'English', 'to': 'Chinese'},
 'zhen': {'from': 'Chinese', 'to': 'English'},
 'enja': {'from': 'English', 'to': 'Japanese'},
 'jaen': {'from': 'Japanese', 'to': 'English'},
 'enko': {'from': 'English', 'to': 'Korean'},
 'koen': {'from': 'Korean', 'to': 'English'},
 'enar': {'from': 'English', 'to': 'Arabic'},
 'aren': {'from': 'Arabic', 'to': 'English'}}
```

> ⚠️ &nbsp;Next dicts are not working properly since their response is not structured in the same way as the others:
>
> - Spanish to Catalan
> - Russian to English

In order to **translate a word**, you can follow this workflow:

```pycon
>>> from wrpy import WordReference

>>> wr = WordReference('es', 'en')  # same as WordReference('esen')

>>> wr.translate('teclado')
{'word': 'teclado',
 'from_lang': 'Spanish',
 'to_lang': 'English',
 'url': 'https://www.wordreference.com/esen/teclado',
 'translations': [{'title': 'Principal Translations',
   'entries': [{'from_word': {'source': 'teclado', 'grammar': 'nm'},
     'to_word': [{'meaning': 'keyboard', 'notes': None, 'grammar': 'n'},
      {'meaning': 'keypad, touchpad', 'notes': None, 'grammar': 'n'}],
     'context': 'tablero con teclas',
     'from_example': 'No me funciona bien el teclado del portátil.',
     'to_example': ["The laptop keyboard isn't working well."]}]},
  {'title': 'Additional Translations',
   'entries': [{'from_word': {'source': 'teclado', 'grammar': 'nm'},
     'to_word': [{'meaning': 'keyboard', 'notes': 'music', 'grammar': 'n'}],
     'context': 'piano electrónico',
     'from_example': 'Aprendí a tocar el teclado de adolescente.',
     'to_example': ['I learned to play the keyboard when I was a teenager.']},
    {'from_word': {'source': 'teclado', 'grammar': 'nm'},
     'to_word': [{'meaning': 'keyboard', 'notes': 'piano', 'grammar': 'n'},
      {'meaning': 'keys', 'notes': None, 'grammar': 'npl'}],
     'context': 'teclas del piano',
     'from_example': 'Este señor viene a afinar el teclado del piano de cola.',
     'to_example': ["This man has come to fine tune the grand piano's keyboard"]}]},
  {'title': 'Compound Forms',
   'entries': [{'from_word': {'source': 'atajo de teclado',
      'grammar': 'nm + loc adj'},
     'to_word': [{'meaning': 'keyboard shortcut',
       'notes': None,
       'grammar': 'n'}],
     'context': 'Informática: grupo de teclas',
     'from_example': '¿Cuál es el atajo de teclado para guardar los cambios en un documento?',
     'to_example': []}]}]}
```

## Response

Response fields from calling `translate()` method:

```python
response {}
    ├ word
    ├ from_lang
    ├ to_lang
    ├ url  # hitted url
    └ translations []
        ├ title  # title of each section
        └ entries []
            ├ context
            ├ from_word {}
            │    ├ source   # source word
            │    └ grammar  # grammar tips about source word
            ├ to_word []
            │    ├ meaning
            │    ├ notes    # clarification about meaning
            │    └ grammar  # grammar tips about meaning
            ├ from_example
            └ to_example []

```

Response is composed by sections (inside the `translations` list) as they appear in [wordreference.com](https://wordreference.com)

Number of entries is limited to 100 results.

## Disclaimer

The workflow of this package is based on scraping of [wordreference.com](https://wordreference.com). Thus, future changes on the structure of html response may affect the results.
