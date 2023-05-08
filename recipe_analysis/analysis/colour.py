import aenum
from typing import List
from ..model import Recipe


class Colours(aenum.AutoNumberEnum):
    _init_ = 'label synonyms'
    GREEN = 'green', ['green']
    BLUE = 'blue', ['blue']
    YELLOW = 'yellow', ['yellow', 'gold', 'golden']
    RED = 'red', ['red']
    PURPLE = 'purple', ['purple']
    ORANGE = 'orange', ['orange']
    BROWN = 'brown', ['brown']
    GRAY = 'gray', ['grey', 'gray']
    BLACK = 'black', ['black']
    WHITE = 'white', ['white']


def search_and_print_colours(recipes: List[Recipe], term: str, bigram_search: bool):
    if bigram_search:
        print(f'Searching for \'{term}\' colours using bigrams:')
        use_bigram_search(recipes, term)
    else:
        print(f'Searching for \'{term}\' colours using two search steps:')
        use_two_step_search(recipes, term)
    print('Search finished.')


def use_bigram_search(recipes: List[Recipe], term: str):
    for col in Colours:
        count_rec = 0
        count_steps = 0
        for syn in col.synonyms:
            for r in recipes:
                r.reset_filter()
                r.filter_complete(f'{term} {syn}')
                if r.is_visible():
                    count_rec += 1
                    count_steps += r.count_visible_steps()
        print(f'{col.label} - {count_rec} recipes with {count_steps} steps')


def use_two_step_search(recipes: List[Recipe], term: str):
    for col in Colours:
        count_rec = 0
        count_steps = 0
        for syn in col.synonyms:
            for r in recipes:
                r.reset_filter()
                r.filter_complete(f'{term}')
                r.filter_complete(f'{syn}')
                if r.is_visible():
                    count_rec += 1
                    count_steps += r.count_visible_steps()
        print(f'{col.label} - {count_rec} recipes with {count_steps} steps')
