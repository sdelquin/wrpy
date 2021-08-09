import re


def parse_from_word(entry):
    td = entry[0].find('td', 'FrWrd')
    source = td.find('strong').text.strip()
    grammar = None
    if em := td.find('em', 'POS2'):
        if (span := em.span) is not None:
            grammar = span.i.text.strip()
        else:
            grammar = em.text.strip()
    return dict(source=source, grammar=grammar)


def parse_to_word(entry):
    to_word = []
    for tr in entry:
        if td := tr.find('td', 'ToWrd'):
            meaning = td.contents[0].strip()
            notes = None
            if span := tr.find('span', 'dsense'):
                notes = span.i.text.strip()
            grammar = None
            if em := td.find('em', 'POS2'):
                if (span := em.span) is not None:
                    grammar = em.span.i.text.strip()
            to_word.append(dict(meaning=meaning, notes=notes, grammar=grammar))
    return to_word


def parse_context(entry):
    context = entry[0].contents[1].text
    if context := re.search(r'\((.*?)\)', context):
        context = context.groups()[0]
    else:
        context = None
    return context


def parse_from_example(entry):
    for tr in entry:
        if aux := tr.find('td', 'FrEx'):
            from_example = aux.contents[0].text.strip()
            break
    else:
        from_example = None
    return from_example


def parse_to_example(entry):
    to_example = []
    for tr in entry:
        if aux := tr.find('td', 'ToEx'):
            to_ex = aux.contents[0].text.strip()
            # remove tooltip (if exists)
            to_ex = re.sub(r'ⓘ[^.]+\. *', '', to_ex)
            to_example.append(to_ex)
    return to_example


def parse_entry(entry):
    return dict(
        from_word=parse_from_word(entry),
        to_word=parse_to_word(entry),
        context=parse_context(entry),
        from_example=parse_from_example(entry),
        to_example=parse_to_example(entry),
    )
