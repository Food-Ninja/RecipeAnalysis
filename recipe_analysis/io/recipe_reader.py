import json
import os
from recipe_analysis.model.recipe import Recipe


def read_recipes():
    data_dir = './data/'
    json_files = [pos_json for pos_json in os.listdir(data_dir) if pos_json.endswith('.json')]
    recipes = []

    for index, js in enumerate(json_files):
        with open(os.path.join(data_dir, js)) as json_file:
            json_text = json.load(json_file)
            for rec in json_text:
                instructions = [step['text'] for step in rec['instructions']]
                r = Recipe(rec['title'], instructions)
                recipes.append(r)

    return recipes
