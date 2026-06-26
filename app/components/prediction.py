import streamlit as st


def _top_pest(pest_results):
    if not pest_results:
        return None

    return max(
        pest_results,
        key=lambda item: item.get("confidence", 0)
    )


def show_prediction(
        disease_result,
        pest_results
):
    st.markdown("### 🤖 Step 2: AI Detection Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🦠 Disease Detection")
        confidence = disease_result['confidence']
        if confidence >= 80:
            st.success(f"🎯 {disease_result['disease']}")
        elif confidence >= 60:
            st.warning(f"⚠️ {disease_result['disease']}")
        else:
            st.info(f"❓ {disease_result['disease']}")
        
        st.metric("Confidence Score", f"{confidence}%")
        
        # Confidence bar
        st.progress(min(confidence / 100, 1.0))
        st.caption("CNN-based disease classifier (224x224 input)")

    with col2:
        st.markdown("#### 🐛 Pest Detection")

        top_pest = _top_pest(pest_results)

        if top_pest:
            conf = top_pest['confidence']
            if conf >= 80:
                st.success(f"🎯 {top_pest['pest']}")
            elif conf >= 60:
                st.warning(f"⚠️ {top_pest['pest']}")
            else:
                st.info(f"❓ {top_pest['pest']}")
            
            st.metric("Confidence Score", f"{conf}%")
            st.progress(min(conf / 100, 1.0))

            if len(pest_results) > 1:
                with st.expander(f"🔍 Other detections ({len(pest_results)} total)"):
                    for i, pest in enumerate(pest_results, 1):
                        st.write(
                            f"{i}. {pest['pest']} — {pest['confidence']}%"
                        )
        else:
            st.info("✅ No pests detected")
            st.metric("Confidence", "0%")
            st.progress(0.0)

        st.caption("YOLO-based pest detector")

    pest_confidence = top_pest["confidence"] if top_pest else 0

    if disease_result["confidence"] >= pest_confidence:
        return (
            disease_result["disease"],
            disease_result["confidence"],
            "Disease"
        )

    return (
        top_pest["pest"],
        top_pest["confidence"],
        "Pest"
    )
