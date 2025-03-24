from wrpy import WordReference, get_available_dicts


def test_get_available_dicts():
    dicts = get_available_dicts()
    assert len(dicts) > 0
    for langs, labels in dicts.items():
        assert len(langs) == 4
        assert len(labels) == 2
        assert 'from' in labels
        assert 'to' in labels
        assert labels['from'] != labels['to']


def test_multiple_words(translation_bench):
    """It takes more than 10 seconds to run this test"""
    for word, dict_code in translation_bench:
        wr = WordReference(dict_code)
        response = wr.translate(word)
        assert len(response.keys()) == 5
        assert all(v is not None for v in response.values())
        assert len(response['translations'][0]['entries']) >= 1


def test_aclarar_esen():
    """Testing translation of word "aclarar" from Spanish to English"""
    wr = WordReference('esen')
    word = 'aclarar'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/esen/aclarar'
    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'English'

    assert len(response['translations']) == 3

    section = response['translations'][0]
    assert section['title'] == 'Principal Translations'
    entries = section['entries']
    assert len(entries) == 9

    first_entry = entries[0]
    assert first_entry['from_word']['source'] == 'aclarar'
    assert first_entry['from_word']['grammar'] == 'vtr'
    assert first_entry['context'] == 'explicar algo'
    assert first_entry['to_word'][0]['meaning'] == 'clear up'
    assert first_entry['to_word'][0]['notes'] == 'confusion, doubt'
    assert first_entry['to_word'][0]['grammar'] == 'vtr phrasal sep'
    assert first_entry['to_word'][1]['meaning'] == 'clarify, explain'
    assert first_entry['to_word'][1]['notes'] == 'general'
    assert first_entry['to_word'][1]['grammar'] == 'vtr'
    assert first_entry['to_word'][2]['meaning'] == 'cast light on, shed light on'
    assert first_entry['to_word'][2]['notes'] == 'topic'
    assert first_entry['to_word'][2]['grammar'] == 'v expr'
    assert first_entry['to_word'][3]['meaning'] == 'answer'
    assert first_entry['to_word'][3]['notes'] == 'question'
    assert first_entry['to_word'][3]['grammar'] == 'vtr'
    assert first_entry['from_example'] == 'El profesor aclara las dudas de los alumnos.'
    assert first_entry['to_example'][0] == "The teacher clears up the students' doubts."


def test_salir_esde():
    """Testing translation of word "salir" from Spanish to German"""
    wr = WordReference('esde')
    word = 'salir'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/esde/salir'
    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'German'

    section = response['translations'][0]
    assert section['title'] == 'Principal Translations'
    entries = section['entries']
    assert len(entries) == 5

    first_entry = entries[0]
    assert first_entry['from_word']['source'] == 'salir'
    assert first_entry['from_word']['grammar'] == 'vi'
    assert first_entry['context'] is None
    assert first_entry['to_word'][0]['meaning'] == 'rausgehen'
    assert first_entry['to_word'][0]['notes'] is None
    assert first_entry['to_word'][0]['grammar'] == 'Vi, sepa'
    assert first_entry['to_word'][1]['meaning'] == 'hinausgehen'
    assert first_entry['to_word'][1]['notes'] is None
    assert first_entry['to_word'][1]['grammar'] == 'Vi, sepa'
    assert first_entry['to_word'][2]['meaning'] == 'hinaustreten'
    assert first_entry['to_word'][2]['notes'] == 'literarisch'
    assert first_entry['to_word'][2]['grammar'] == 'Vi, sepa'
    assert first_entry['from_example'] == 'No salgas sin un abrigo, hace frío.'
    assert first_entry['to_example'][0] == 'Geh nicht ohne Jacke raus, es ist kalt da draußen.'


def test_hablar_esit():
    """Testing translation of word "hablar" from Spanish to Italian"""
    wr = WordReference('esit')
    word = 'hablar'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/esit/hablar'
    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'Italian'

    section = response['translations'][0]
    assert section['title'] == 'Principal Translations'
    entries = section['entries']
    assert len(entries) == 4

    first_entry = entries[0]
    assert first_entry['from_word']['source'] == 'hablar'
    assert first_entry['from_word']['grammar'] == 'vi'
    assert first_entry['context'] is None
    assert first_entry['to_word'][0]['meaning'] == 'parlare'
    assert first_entry['to_word'][0]['notes'] is None
    assert first_entry['to_word'][0]['grammar'] == 'vi'
    assert first_entry['from_example'] == 'El maestro exigió que el estudiante hablara.'
    assert first_entry['to_example'][0] == "L'insegnante ha chiesto allo studente di parlare."


def test_market_enes():
    """Testing translation of word "market" from English to Spanish"""
    wr = WordReference('enes')
    word = 'market'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/enes/market'
    assert response['word'] == word
    assert response['from_lang'] == 'English'
    assert response['to_lang'] == 'Spanish'

    assert len(response['translations']) == 3

    section = response['translations'][0]
    assert section['title'] == 'Principal Translations'
    entries = section['entries']
    assert len(entries) == 5

    first_entry = entries[0]
    assert first_entry['from_word']['source'] == 'market'
    assert first_entry['from_word']['grammar'] == 'n'
    assert first_entry['context'] == 'street stalls'
    assert first_entry['to_word'][0]['meaning'] == 'mercado'
    assert first_entry['to_word'][0]['notes'] is None
    assert first_entry['to_word'][0]['grammar'] == 'nm'
    assert first_entry['to_word'][1]['meaning'] == 'mercadillo'
    assert first_entry['to_word'][1]['notes'] == 'ES'
    assert first_entry['to_word'][1]['grammar'] == 'nm'
    assert first_entry['from_example'] == "They set up the market at four o'clock in the morning."
    assert first_entry['to_example'][0] == 'Instalaron el mercado a las cuatro de la mañana.'
