from typing import List
from ..model import Recipe

def get_corpus_metadata(recipes: List[Recipe]) -> (int, int):
    count_rec = len(recipes)
    count_step = 0
    for r in recipes:
        count_step += r.count_visible_steps()
    return count_rec, count_step
