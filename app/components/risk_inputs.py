import streamlit as st


def render_risk_inputs():
    st.markdown("### 📊 Step 4: Risk Assessment")
    st.markdown("*Help us understand the severity of the issue*")

    col1, col2, col3 = st.columns(3)

    with col1:
        rapid_spread = st.checkbox(
            "🔴 Spreading rapidly?",
            help="Issue is spreading to other plants quickly"
        )

    with col2:
        stem_damage = st.checkbox(
            "🌱 Main plant damage?",
            help="Stem, trunk, or main plant structure is affected"
        )

    with col3:
        crop_percentage = st.slider(
            "📍 Crop area affected",
            min_value=0,
            max_value=100,
            value=0,
            step=5,
            format="%d%%",
            help="Percentage of crop area showing symptoms"
        )

    # Risk summary
    risk_factors = []
    if rapid_spread:
        risk_factors.append("⚡ Rapid spread")
    if stem_damage:
        risk_factors.append("🌱 Main damage")
    if crop_percentage > 50:
        risk_factors.append("🔴 Large area affected")

    if risk_factors:
        st.warning(f"Risk factors detected: {', '.join(risk_factors)}")

    return rapid_spread, stem_damage, crop_percentage
