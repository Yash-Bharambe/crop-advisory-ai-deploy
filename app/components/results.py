import streamlit as st

from tools.knowledge_loader import load_sources


def _risk_color(risk_level):
    if risk_level == "HIGH":
        return "red"
    if risk_level == "MEDIUM":
        return "orange"
    return "green"


def render_results(result):
    st.markdown("### 💡 Step 5: Advisory Results")

    risk = result["risk"]
    recommendation = result["recommendation"]

    # Summary metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🤖 AI Confidence",
            f"{result['model_confidence']}%"
        )

    with col2:
        st.metric(
            "✓ Symptom Match",
            f"{result['symptom_match']}%"
        )

    with col3:
        risk_icon = "🔴" if risk['risk_level'] == "HIGH" else "🟡" if risk['risk_level'] == "MEDIUM" else "🟢"
        st.markdown(
            f":{_risk_color(risk['risk_level'])}[**{risk_icon} {risk['risk_level']} RISK**]"
        )
        st.caption(
            f"Risk Score: {risk['risk_score']}/9"
        )

    st.divider()

    if risk["factors"]:
        with st.expander("⚠️ Risk Factors", expanded=True):
            for factor in risk["factors"]:
                st.write(f"• {factor}")

    if "error" in recommendation:
        st.warning(f"⚠️ {recommendation['error']}")
        return

    # Recommended actions
    with st.container():
        st.markdown("### 🎯 Recommended Actions")
        actions = recommendation.get("actions", [])
        if actions:
            for i, action in enumerate(actions, 1):
                st.markdown(f"**{i}.** {action}")
        else:
            st.info("No specific actions needed at this time.")

    # Prevention
    prevention = recommendation.get("prevention", [])
    if prevention:
        with st.expander("🛡️ Prevention Measures", expanded=True):
            for item in prevention:
                st.markdown(f"• {item}")

    # Sources
    source_keys = recommendation.get("sources", [])
    if source_keys:
        sources = load_sources()

        with st.expander("📚 References & Sources"):
            for key in source_keys:
                source = sources.get(key, {})
                name = source.get("name", key)
                website = source.get("website")
                purpose = source.get("purpose", "")

                if website:
                    st.markdown(f"**[{name}]({website})**")
                else:
                    st.markdown(f"**{name}**")
                
                if purpose:
                    st.caption(purpose)
