import pandas as pd
from typing import List
from recipe_analysis.model import Recipe
from os.path import exists

# to use this function, the following two files need to exist and have the following columns:
# ,fruit_label,rndm_fruit_id,rndm_def
fruit_path = "./data/fruits_raw.csv"
veggie_path = "./data/veggies_raw.csv"


def count_fruit_and_veggie_occurrences(recipes: List[Recipe]):
    if not exists(fruit_path):
        print(f'{fruit_path} does not exist. Aborting...')
        return
    if not exists(veggie_path):
        print(f'{veggie_path} does not exist. Aborting...')
        return

    fruits = pd.read_csv(fruit_path, header=0)
    veggies = pd.read_csv(veggie_path, header=0)

    combined = []
    for idx, row in fruits.iterrows():
        fruit = [row["fruit_label"], 0, 0]
        combined.append(fruit)
    for idx, row in veggies.iterrows():
        veggie = [row["veg_label"], 0, 0]
        combined.append(veggie)

    for food_row in combined:
        food = food_row[0]
        count_rec = 0
        count_steps = 0
        for r in recipes:
            r.reset_filter()
            r.filter_complete(food)
            if r.is_visible():
                count_rec += 1
                count_steps += r.count_visible_steps()
        food_row[1] = count_rec
        food_row[2] = count_steps
        print(f'{food} - {count_rec} recipes with {count_steps} steps')

    res = pd.DataFrame(combined)
    res.to_csv('./data/recipe_data.csv')
