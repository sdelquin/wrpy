import pytest

TRANSLATION_BENCH = (
    # word, dict
    ('glass', 'enes'),
    ('árbol', 'esen'),
    ('coche', 'esfr'),
    ('alfombra', 'espt'),
    ('biblioteca', 'esit'),
    ('carretera', 'esde'),
    ('people', 'enfr'),
    ('fête', 'fren'),
    ('vie', 'fres'),
    ('food', 'enit'),
    ('notte', 'iten'),
    ('posto', 'ites'),
    ('culture', 'ende'),
    ('haus', 'deen'),
    ('music', 'ennl'),
    ('zon', 'nlen'),
    ('tiger', 'ensv'),
    ('haj', 'sven'),
    ('screen', 'enru'),
    ('hug', 'enpt'),
    ('rua', 'pten'),
    ('televisão', 'ptes'),
    ('keyboard', 'enpl'),
    ('lotnisko', 'plen'),
    ('number', 'enro'),
    ('scaun', 'roen'),
    ('bag', 'encz'),
    ('schody', 'czen'),
    ('winter', 'engr'),
    ('καλοκαίρι', 'gren'),
    ('amigo', 'entr'),
    ('çiçek', 'tren'),
    ('kitchen', 'enzh'),
    ('水', 'zhen'),
    ('sport', 'enja'),
    ('自然', 'jaen'),
    ('math', 'enko'),
    ('쌀', 'koen'),
    ('water', 'enar'),
    ('تفاح', 'aren'),
)


@pytest.fixture
def translation_bench():
    return TRANSLATION_BENCH
