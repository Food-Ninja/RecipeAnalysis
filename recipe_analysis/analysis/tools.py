import aenum
from typing import List
from ..model import Recipe


class RemovalTools(aenum.AutoNumberEnum):
    _init_ = 'label synonyms'
    KNIFE = 'knife', ['knife', 'knives']
    HAND = 'hand', ['hand', 'hands']
    NUTCRACKER = 'nutcracker', ['nutcracker', 'nutcrackers']
    SPOON = 'spoon', ['spoon', 'spoons']
    PEELER = 'peeler', ['peeler']


def search_and_print_removal_tool(recipes: List[Recipe], term: str, bigram_search: bool):
    if bigram_search:
        print(f'Searching for \'{term}\' removal tool using bigrams:')
        use_bigram_search(recipes, term)
    else:
        print(f'Searching for \'{term}\' removal tool using two search steps:')
        use_two_step_search(recipes, term)
    print('Search finished.')


def use_bigram_search(recipes: List[Recipe], term: str):
    for part in RemovalTools:
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
    for part in RemovalTools:
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
