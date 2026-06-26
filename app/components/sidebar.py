import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.markdown("## 🌱 CropCare AI")

        st.markdown(
            """
            **Intelligent crop disease & pest advisory system**
            
            Harness AI to detect and manage crop threats early.
            """
        )

        st.divider()

        st.markdown("### 📋 How it works")
        workflow_steps = [
            "📸 Upload crop image",
            "🤖 AI detection (disease + pest)",
            "✓ Symptom verification",
            "📊 Risk analysis",
            "💡 Smart recommendations"
        ]
        for step in workflow_steps:
            st.markdown(f"**{step}**")

        st.divider()

        with st.expander("ℹ️ Tips for best results"):
            st.markdown(
                """
                • Take clear, well-lit photos
                • Include affected leaves/areas
                • Avoid shadows and blur
                • Check multiple angles if possible
                """
            )
