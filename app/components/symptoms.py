import streamlit as st

from tools.symptom_engine import get_questions


def render_symptom_questions(prediction):
    st.markdown("### ✓ Step 3: Symptom Validation")

    questions = get_questions(prediction)

    if not questions:
        st.info("ℹ️ No symptom follow-up questions available for this prediction.")
        return []

    st.markdown(
        "**Answer based on what you observe in the crop or field**",
        help="These questions help verify the AI detection and improve accuracy"
    )

    answers = []
    answered_count = 0

    for index, item in enumerate(questions):
        is_checked = st.checkbox(
            item["question"],
            key=f"symptom_{prediction}_{index}"
        )
        answers.append(is_checked)
        if is_checked:
            answered_count += 1

    # Progress indicator
    st.caption(f"✓ {answered_count}/{len(questions)} symptoms confirmed")

    return answers
