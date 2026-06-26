import json
import os
from functools import lru_cache


BASE_PATH = "knowledge_base"


@lru_cache(maxsize=None)
def load_knowledge():

    disease_path = os.path.join(
        BASE_PATH,
        "disease_guidelines.json"
    )

    pest_path = os.path.join(
        BASE_PATH,
        "pest_guidelines.json"
    )


    with open(disease_path) as f:
        diseases = json.load(f)


    with open(pest_path) as f:
        pests = json.load(f)


    knowledge = {}

    knowledge.update(diseases)
    knowledge.update(pests)


    return knowledge




def generate_recommendation(
        prediction,
        risk_level
):

    knowledge = load_knowledge()


    if prediction not in knowledge:

        return {

            "error":
            "No recommendation found"

        }



    data = knowledge[prediction]


    recommendations = data["recommendations"]


    if risk_level == "LOW":

        advice = recommendations["low"]


    elif risk_level == "MEDIUM":

        advice = recommendations["medium"]


    else:

        advice = recommendations["high"]



    return {


        "prediction":
        prediction,


        "risk":
        risk_level,


        "actions":
        advice,


        "prevention":
        data.get(
            "prevention",
            []
        ),


        "sources":
        data.get(
            "source_category",
            []

        )

    }




if __name__ == "__main__":


    result = generate_recommendation(

        "Tomato_Early_Blight",

        "HIGH"

    )


    print(result)