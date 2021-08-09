import re


def parse_entry(entry):
    from_word = entry[0].find('td', 'FrWrd').strong.text.strip()

    to_word = []
    for tr in entry:
        if aux := tr.find('td', 'ToWrd'):
            to_word.append(aux.contents[0].strip())

    aux = entry[0].contents[1].text
    aux = re.search(r'\((.*?)\)', aux)
    notes = aux.groups()[0]

    for tr in entry:
        if aux := tr.find('td', 'FrEx'):
            from_example = aux.contents[0].text.strip()
            break
    else:
        from_example = None

    to_example = []
    for tr in entry:
        if aux := tr.find('td', 'ToEx'):
            to_ex = aux.contents[0].text.strip()
            # remove tooltip (if exists)
            to_ex = re.sub(r'ⓘ[^.]+\. *', '', to_ex)
            to_example.append(to_ex)

    return dict(
        from_word=from_word,
        to_word=to_word,
        notes=notes,
        from_example=from_example,
        to_example=to_example,
    )
