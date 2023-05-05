import aenum
from typing import List
from ..model import Recipe


class AnatomicalParts(aenum.AutoNumberEnum):
    _init_ = 'label synonyms'
    CORE = 'core', ['core', 'cores']
    FLESH = 'flesh/pulp', ['flesh', 'pulp']
    PIT = 'pit', ['stone', 'stones', 'pit', 'pits']
    SEED = 'seed(s)', ['seed', 'seeds']
    SHELL = 'shell', ['shell']
    SKIN = 'skin/peel', ['skin', 'skins', 'peel', 'peels', 'rind']
    STEM = 'stem', ['stem', 'stems', 'stalk', 'stalks']


def search_and_print_anatomical_parts(recipes: List[Recipe], term: str, bigram_search: bool):
    if bigram_search:
        print(f'Searching for \'{term}\' anatomical parts using bigrams:')
        use_bigram_search(recipes, term)
    else:
        print(f'Searching for \'{term}\' anatomical parts using two search steps:')
        use_two_step_search(recipes, term)


def use_bigram_search(recipes: List[Recipe], term: str):
    for part in AnatomicalParts:
        count_rec = 0
        count_steps = 0
        for syn in part.synonyms:
            for r in recipes:
                r.reset_filter()
                r.filter_complete(f'{term} {syn}')
                if r.is_visible():
                    count_rec += 1
                    count_steps += r.count_visible_steps()
        print(f'{part.label} - {count_rec} recipes with {count_steps} steps')


def use_two_step_search(recipes: List[Recipe], term: str):
    for part in AnatomicalParts:
        count_rec = 0
        count_steps = 0
        for syn in part.synonyms:
            for r in recipes:
                r.reset_filter()
                r.filter_complete(f'{term}')
                r.filter_complete(f'{syn}')
                if r.is_visible():
                    count_rec += 1
                    count_steps += r.count_visible_steps()
        print(f'{part.label} - {count_rec} recipes with {count_steps} steps')
