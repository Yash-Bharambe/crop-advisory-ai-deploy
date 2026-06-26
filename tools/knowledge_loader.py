import json
import os
from functools import lru_cache


BASE_PATH = "knowledge_base"


@lru_cache(maxsize=None)
def load_json(filename):

    path = os.path.join(BASE_PATH, filename)

    with open(path, "r") as file:
        data = json.load(file)

    return data



def load_diseases():

    return load_json(
        "disease_guidelines.json"
    )



def load_pests():

    return load_json(
        "pest_guidelines.json"
    )



def load_sources():

    return load_json(
        "sources.json"
    )



if __name__ == "__main__":

    diseases = load_diseases()
    pests = load_pests()

    print(
        "Diseases loaded:",
        len(diseases)
    )

    print(
        "Pests loaded:",
        len(pests)
    )