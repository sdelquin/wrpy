# wrpy

This is a Python package to obtain translations from wordreference.com transforming returned data into normalized and structured datatypes.

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

> ⚠️ &nbsp;Next dicts are not working properly since the response is not structured in the same way as the others:
>
> - Spanish to Catalan
> - Russian to English

In order to **translate a word**, you can follow this workflow:

```pycon
>>> from wrpy import WordReference

>>> wr = WordReference('es', 'en')  # same as WordReference('esen')

>>> wr.translate('hola')
{'word': 'hola',
 'from_lang': 'Spanish',
 'to_lang': 'English',
 'url': 'https://www.wordreference.com/esen/hola',
 'translations': [{'title': 'Principal Translations',
   'entries': [{'from_word': {'source': '¡Hola!', 'grammar': 'interjección'},
     'to_word': [{'meaning': 'Hello!',
       'notes': 'formal',
       'grammar': 'interjection'},
      {'meaning': 'Hi!', 'notes': 'informal', 'grammar': 'interjection'},
      {'meaning': "Hey! What's Up!",
       'notes': 'colloquial',
       'grammar': 'interjection'}],
     'context': 'saludo',
     'from_example': '—¡Hola, Rafael! ¿Cómo estás? —¡Hola, Diego! Bien, ¿y tú? ¡Hola a todos!',
     'to_example': ["- Hello, Rafael! How are you?\n- Hello, Diego. I'm well, and you?\nHello, everyone!"]}]},
  {'title': 'Additional Translations',
   'entries': [{'from_word': {'source': '¡Hola!', 'grammar': 'interjección'},
     'to_word': [{'meaning': 'hello',
       'notes': None,
       'grammar': 'interjection'}],
     'context': 'expresa extrañeza',
     'from_example': '¡Hola, hola, hola! ¿Qué tenemos aquí?',
     'to_example': ["Hello, hello, hello. What's all this, then?"]}]},
  {'title': 'Compound Forms',
   'entries': [{'from_word': {'source': 'hola a todos',
      'grammar': 'expresión'},
     'to_word': [{'meaning': 'hi everyone',
       'notes': None,
       'grammar': 'interjection'},
      {'meaning': 'hello all', 'notes': 'formal', 'grammar': 'interjection'}],
     'context': 'saludo a un grupo',
     'from_example': 'Hola a todos, ¿cómo están?',
     'to_example': ['Hi everyone! How are you?']},
    {'from_word': {'source': 'hola y adiós', 'grammar': 'expresión'},
     'to_word': [{'meaning': 'hello and goodbye',
       'notes': None,
       'grammar': 'expression'},
      {'meaning': 'hail and farewell',
       'notes': 'literary',
       'grammar': 'expression'}],
     'context': 'encuentro breve',
     'from_example': 'No somos amigos, apenas nos decimos "hola y adiós".',
     'to_example': ['We aren\'t friends. We only say "hello and goodbye".']}]}]}
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

Response is composed by sections (inside the `translations` list) as they appear in wordreference.com

Number of entries is limited to 100 results.

## Disclaimer

The workflow of this package is based on scraping of wordreference.com. Thus, future changes on the structure of html response may affect the results.
