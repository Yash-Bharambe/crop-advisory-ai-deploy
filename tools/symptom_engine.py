import json
import os
from functools import lru_cache


BASE_PATH = "knowledge_base"


@lru_cache(maxsize=None)
def load_symptom_questions():

    path = os.path.join(
        BASE_PATH,
        "symptom_questions.json"
    )

    with open(path, "r") as file:
        return json.load(file)



def get_questions(prediction):

    data = load_symptom_questions()


    if prediction not in data:

        return None


    return data[prediction]["questions"]



def calculate_symptom_score(
        prediction,
        answers
):

    data = load_symptom_questions()


    if prediction not in data:

        return {
            "error": "Prediction not found"
        }


    questions = data[prediction]["questions"]


    score = 0


    max_score = data[prediction]["maximum_score"]


    for i, answer in enumerate(answers):

        if answer:

            score += questions[i]["yes_score"]



    percentage = (
        score / max_score
    ) * 100



    return {

        "prediction": prediction,

        "symptom_score": score,

        "maximum_score": max_score,

        "symptom_match": round(
            percentage,
            2
        )

    }



if __name__ == "__main__":


    prediction = "Tomato_Early_Blight"


    questions = get_questions(prediction)


    print("\nQuestions:")

    for q in questions:

        print(
            "-",
            q["question"]
        )


    # Example farmer answers
    # True = Yes
    # False = No

    answers = [
        True,
        True,
        False
    ]


    result = calculate_symptom_score(
        prediction,
        answers
    )


    print("\nResult:")
    print(result)