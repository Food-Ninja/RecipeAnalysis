from typing import List
from ..model import Recipe
from openie import StanfordOpenIE
import re


def extract_triples(recipes: List[Recipe], search: str):
    properties = {
        'openie.affinity_probability_cap': 2 / 3,
    }

    with StanfordOpenIE(properties=properties) as client:
        print('Starting the annotation / triple extraction process...')
        corp = ""
        count_rec = 0
        triples = []
        for r in recipes:
            if not r.is_visible():
                continue
            steps = r.get_steps_as_single_string()
            count_rec += 1
            if len(corp) + len(steps) + 1 <= 100000:
                corp = f'{corp}\n{steps}'
            else:
                triples_corpus = client.annotate(corp)
                corp = ''
                for tr in triples_corpus:
                    if re.fullmatch(search, tr['subject']):
                        triples.append(tr)
        print(f'Found {len(triples)} triples by looking at {count_rec} recipes')
        return triples
