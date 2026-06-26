import sys
import os


# allow importing tools
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from tools.symptom_engine import calculate_symptom_score
from tools.risk_engine import calculate_risk
from tools.recommendation_engine import generate_recommendation



def run_advisory_pipeline(

        prediction,

        model_confidence,

        answers,

        rapid_spread=False,

        stem_damage=False,

        crop_percentage=0

):


    # 1. Symptom validation

    symptom_result = calculate_symptom_score(

        prediction,

        answers

    )



    symptom_match = symptom_result.get(
        "symptom_match",
        0
    )



    # 2. Risk calculation

    risk_result = calculate_risk(

        confidence=model_confidence,

        rapid_spread=rapid_spread,

        stem_damage=stem_damage,

        crop_percentage=crop_percentage

    )



    # 3. Recommendation generation

    recommendation = generate_recommendation(

        prediction,

        risk_result["risk_level"]

    )



    final_result = {


        "prediction":

        prediction,


        "model_confidence":

        model_confidence,


        "symptom_match":

        symptom_match,


        "risk":

        risk_result,


        "recommendation":

        recommendation

    }



    return final_result




if __name__ == "__main__":


    result = run_advisory_pipeline(


        prediction="Tomato_Early_Blight",


        model_confidence=91,


        answers=[

            True,

            True,

            False

        ],


        rapid_spread=True,


        stem_damage=False,


        crop_percentage=60

    )



    print(result)