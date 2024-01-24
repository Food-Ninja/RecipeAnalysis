import aenum
from typing import List
from ..model import Recipe


class Edibility(aenum.AutoNumberEnum):
    _init_ = 'label synonyms'
    EDIBLE = 'edible', ['edible']


def search_and_print_edibility(recipes: List[Recipe], term: str, bigram_search: bool):
    if bigram_search:
        print(f'Searching for \'{term}\' edibility using bigrams:')
        use_bigram_search(recipes, term)
    else:
        print(f'Searching for \'{term}\' edibility using two search steps:')
        use_two_step_search(recipes, term)
    print('Search finished.')


def use_bigram_search(recipes: List[Recipe], term: str):
    for part in Edibility:
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
    for part in Edibility:
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
