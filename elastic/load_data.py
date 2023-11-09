import json
import os
from pathlib import Path

def load():
    path = Path(__file__).parent / "../recipes_raw/full_format_recipes.json"

    f = Path.open(path, mode="r")

    recipes = json.load(f)
    print("Loading JSON File\n")
    f.close()

    data = []
    for r in range(len(recipes)):
        ingredients = None
        instructions = None

        if 'ingredients' in recipes[r].keys():
            ingredients = recipes[r]['ingredients']
            ing_str = ", ".join([e for e in ingredients])
            
        if 'directions' in recipes[r].keys():
            instructions = recipes[r]['directions']
            inst_str = ", ".join([e for e in instructions])

        data.append([ing_str, inst_str])
    
    return data

print(load())