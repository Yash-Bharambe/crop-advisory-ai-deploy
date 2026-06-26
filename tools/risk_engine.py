def calculate_risk(
        confidence,
        rapid_spread=False,
        stem_damage=False,
        crop_percentage=0
):

    score = 0

    factors = []


    # Model confidence
    if confidence >= 80:

        score += 2

        factors.append(
            "High AI confidence"
        )


    # Disease spreading
    if rapid_spread:

        score += 3

        factors.append(
            "Rapid spread detected"
        )


    # Stem damage
    if stem_damage:

        score += 3

        factors.append(
            "Stem damage present"
        )


    # Crop affected percentage
    if crop_percentage > 50:

        score += 3

        factors.append(
            "Large crop area affected"
        )


    # Risk classification

    if score <= 2:

        risk = "LOW"


    elif score <=5:

        risk = "MEDIUM"


    else:

        risk = "HIGH"



    return {

        "risk_score": score,

        "risk_level": risk,

        "factors": factors

    }



if __name__ == "__main__":


    result = calculate_risk(

        confidence=91,

        rapid_spread=True,

        stem_damage=False,

        crop_percentage=60

    )


    print(result)