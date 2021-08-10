from wrpy import WordReference


def test_aclarar_esen():
    wr = WordReference('esen')
    word = 'aclarar'
    response = wr.translate(word)

    assert response['word'] == word
    assert response['from_lang'] == 'Spanish'
    assert response['to_lang'] == 'English'

    main_entries = response['translations'][0]['entries']

    assert main_entries[0]['from_word']['source'] == word
    assert main_entries[0]['from_word']['grammar'] == 'verbo transitivo'

    assert main_entries[0]['to_word'][0]['meaning'] == 'clear up'
    assert main_entries[0]['to_word'][0]['notes'] == 'confusion, doubt'
    assert (
        main_entries[0]['to_word'][0]['grammar'] == 'phrasal verb, transitive, inseparable'
    )

    assert main_entries[0]['context'] == 'explicar'
