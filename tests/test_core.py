from wrpy import WordReference


def test_multiple_words(translation_bench):
    for word, dict_code in translation_bench:
        wr = WordReference(dict_code)
        response = wr.translate(word)
        assert len(response.keys()) == 5
        assert all(v is not None for v in response.values())
        assert len(response['translations'][0]['entries']) >= 1


def test_aclarar_esen():
    '''Testing translation of word "aclarar" from Spanish to English'''
    wr = WordReference('esen')
    word = 'aclarar'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/esen/aclarar'
    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'English'

    main_entries = response['translations'][0]['entries']
    assert len(main_entries) == 9
    assert main_entries[0]['from_word']['source'] == word
    assert main_entries[0]['from_word']['grammar'] == 'verbo transitivo'
    assert main_entries[0]['to_word'][0]['meaning'] == 'clear up'
    assert main_entries[0]['to_word'][0]['notes'] == 'confusion, doubt'
    assert (
        main_entries[0]['to_word'][0]['grammar'] == 'phrasal verb, transitive, inseparable'
    )
    assert main_entries[0]['context'] == 'explicar'
    assert main_entries[5]['to_word'][1]['meaning'] == 'shed light on [sth]'
    assert main_entries[7]['from_word']['source'] == 'aclararse'
    assert len(main_entries[7]['to_word']) == 3

    additional_entries = response['translations'][1]['entries']
    assert len(additional_entries) == 2

    compound_entries = response['translations'][2]['entries']
    assert len(compound_entries) == 3


def test_salir_esde():
    '''Testing translation of word "salir" from Spanish to German'''
    wr = WordReference('esde')
    word = 'salir'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/esde/salir'
    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'German'

    main_entries = response['translations'][0]['entries']
    assert len(main_entries) == 3
    assert main_entries[1]['to_word'][2]['meaning'] == 'hinaustreten'
    assert main_entries[1]['to_word'][2]['notes'] == 'literarisch'

    additional_entries = response['translations'][1]['entries']
    assert len(additional_entries) == 64
    assert additional_entries[23]['to_word'][0]['meaning'] == '[etw] beenden'
    assert (
        additional_entries[2]['to_example'][0]
        == 'Lass uns heute Abend ausgehen! Wir könnten ins Kino gehen.'
    )
    assert len(additional_entries[3]['to_example']) == 2


def test_hablar_esit():
    '''Testing translation of word "hablar" from Spanish to Italian'''
    wr = WordReference('esit')
    word = 'hablar'
    response = wr.translate(word)

    assert response['url'] == 'https://www.wordreference.com/esit/hablar'
    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'Italian'

    main_entries = response['translations'][0]['entries']
    assert len(main_entries) == 4

    additional_entries = response['translations'][1]['entries']
    assert len(additional_entries) == 13

    assert additional_entries[2]['to_word'][0]['meaning'] == 'parlare, intervenire'
    assert additional_entries[3]['to_word'][0]['meaning'] == 'essere in contatto con [qlcn]'
    assert additional_entries[3]['to_word'][2]['notes'] == 'informale'
