import json
import os
from typing import List
from ..model import Recipe, Step


def read_recipes() -> List[Recipe]:
    data_dir = './data/'
    json_files = [pos_json for pos_json in os.listdir(data_dir) if pos_json.endswith('.json')]
    recipes = []
    # TODO: substitute logging with progress bar / GUI
    print(f'Importing the recipes from {data_dir}:')

    for index, js in enumerate(json_files):
        with open(os.path.join(data_dir, js)) as json_file:
            json_text = json.load(json_file)
            for rec in json_text:
                instructions = []
                for idx, s in enumerate(rec['instructions']):
                    step = Step(idx+1, s['text'])
                    instructions.append(step)
                r = Recipe(rec['title'], instructions)
                recipes.append(r)
            print(f'File {index+1} of {len(json_files)} - {len(json_text)} recipes')

    return recipes
