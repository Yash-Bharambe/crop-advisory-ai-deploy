import sys
import concurrent.futures
from pathlib import Path

import streamlit as st
from PIL import Image


# Fix imports for Streamlit Cloud
ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from app.advisory_pipeline import run_advisory_pipeline
from tools.disease_predictor import predict_disease
from tools.pest_predictor import predict_pest
# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG & CUSTOM CSS
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Crop Advisory AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Fraunces:ital,wght@0,700;1,700&display=swap');

    /* ── Global ── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* ── Background ── */
    .stApp {
        background: #0e1a0f;
        color: #e8ead4;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: #131f14 !important;
        border-right: 1px solid #2a3d2b;
    }
    section[data-testid="stSidebar"] * {
        color: #c4cfa8 !important;
    }

    /* ── Hero ── */
    .hero-wrap {
        background: linear-gradient(135deg, #1a2e1b 0%, #0e1a0f 60%, #172613 100%);
        border: 1px solid #2d4a2e;
        border-radius: 16px;
        padding: 40px 36px 32px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content: "";
        position: absolute;
        top: -40px; right: -40px;
        width: 220px; height: 220px;
        background: radial-gradient(circle, #4caf5033 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-eyebrow {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: #7ec87e;
        margin-bottom: 10px;
    }
    .hero-title {
        font-family: 'Fraunces', serif;
        font-size: clamp(28px, 4vw, 46px);
        font-weight: 700;
        color: #e8ead4;
        line-height: 1.15;
        margin: 0 0 12px;
    }
    .hero-title span {
        color: #7ec87e;
        font-style: italic;
    }
    .hero-sub {
        font-size: 14px;
        color: #8fa88f;
        max-width: 560px;
        line-height: 1.6;
        margin: 0;
    }

    /* ── Upload zone ── */
    .upload-label {
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #7ec87e;
        margin-bottom: 6px;
    }

    /* ── Prediction card ── */
    .pred-card {
        background: #131f14;
        border: 1px solid #2d4a2e;
        border-radius: 12px;
        padding: 20px 22px;
        margin-bottom: 14px;
    }
    .pred-label {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #7ec87e;
        margin-bottom: 4px;
    }
    .pred-name {
        font-family: 'Fraunces', serif;
        font-size: 22px;
        font-weight: 700;
        color: #e8ead4;
        margin-bottom: 8px;
    }
    .conf-bar-bg {
        background: #1e301f;
        border-radius: 99px;
        height: 6px;
        overflow: hidden;
        margin-top: 6px;
    }
    .conf-bar-fg {
        height: 6px;
        border-radius: 99px;
        background: linear-gradient(90deg, #4caf50, #a5d6a7);
    }
    .conf-text {
        font-size: 12px;
        color: #8fa88f;
        margin-top: 4px;
    }

    /* ── Risk badge ── */
    .badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 99px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .badge-high   { background: #3d1515; color: #f48a8a; border: 1px solid #7a2a2a; }
    .badge-medium { background: #3d2e0a; color: #f4c97a; border: 1px solid #7a5c1a; }
    .badge-low    { background: #0e2d13; color: #7ec87e; border: 1px solid #2d6030; }

    /* ── Result panel ── */
    .result-section {
        background: #131f14;
        border: 1px solid #2d4a2e;
        border-radius: 12px;
        padding: 22px 24px;
        margin-bottom: 16px;
    }
    .result-section-title {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #7ec87e;
        margin-bottom: 12px;
    }
    .result-item {
        display: flex;
        gap: 10px;
        align-items: flex-start;
        margin-bottom: 8px;
        font-size: 14px;
        color: #c4cfa8;
        line-height: 1.55;
    }
    .result-dot {
        width: 6px; height: 6px;
        background: #4caf50;
        border-radius: 50%;
        flex-shrink: 0;
        margin-top: 7px;
    }

    /* ── Streamlit widget overrides ── */
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #2e7d32, #388e3c) !important;
        color: #e8ead4 !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        letter-spacing: 0.5px !important;
        padding: 10px 20px !important;
        transition: opacity 0.2s !important;
    }
    div[data-testid="stButton"] > button:hover {
        opacity: 0.88 !important;
    }
    div[data-testid="stFileUploaderDropzone"] {
        background: #131f14 !important;
        border: 2px dashed #2d4a2e !important;
        border-radius: 12px !important;
    }
    div[data-testid="stRadio"] label {
        color: #c4cfa8 !important;
    }
    div[data-testid="stSlider"] label,
    div[data-testid="stCheckbox"] label {
        color: #c4cfa8 !important;
    }
    div[data-testid="stExpander"] {
        background: #131f14 !important;
        border: 1px solid #2d4a2e !important;
        border-radius: 10px !important;
    }
    .stDivider { border-color: #2d4a2e !important; }
    h1,h2,h3,h4 { color: #e8ead4 !important; }
    label, .stRadio, p { color: #c4cfa8 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("###  About")
    st.markdown(
        """
        This tool provides AI-assisted early detection of **crop diseases** and **pest infestations**
        using a MobileNetV2 classifier and YOLO11 detector.

        Upload a clear image of the affected leaf or plant and follow the guided steps.
        """,
        unsafe_allow_html=False,
    )
    st.divider()
    st.markdown("**Supported crops**")
    st.markdown("Tomato · Potato · Corn · Apple · Grape · Pepper · Peach · Cherry · Strawberry · Squash")
    st.divider()
    st.markdown(
        "<span style='font-size:11px; color:#5a6e5a;'>Advisory output is informational only. "
        "Always consult a certified agronomist before applying treatments.</span>",
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────────────────────────
# MODEL PRELOAD
# ─────────────────────────────────────────────────────────────────────────────

# Models are loaded only when prediction starts.
# This keeps Streamlit Cloud startup lightweight.

if "models_loaded" not in st.session_state:
    st.session_state["models_loaded"] = False

# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="hero-wrap">
        <div class="hero-eyebrow">AI-powered crop protection</div>
        <h1 class="hero-title">Detect threats.<br><span>Protect yields.</span></h1>
        <p class="hero-sub">
            Upload a photo of your crop. The system identifies disease and pest risks,
            then generates a field-ready advisory — all in under 30 seconds.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 — UPLOAD & PREDICT
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="upload-label">Step 1 — Upload crop image</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    label="upload",
    type=["jpg", "jpeg", "png", "webp"],
    label_visibility="collapsed",
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    uploaded_name = uploaded_file.name

    col_img, col_meta = st.columns([1, 1], gap="large")
    with col_img:
        st.image(image, caption=uploaded_name, use_container_width=True)
    with col_meta:
        st.markdown(
            f"""
            <div class="pred-card" style="margin-top:0">
                <div class="pred-label">File loaded</div>
                <div class="pred-name" style="font-size:16px">{uploaded_name}</div>
                <p style="font-size:13px; color:#5a7a5a; margin:4px 0 0;">
                    Ready for analysis. Click the button below to run both AI models simultaneously.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🚀 Analyze Image", type="primary", use_container_width=True):
            with st.spinner("Running disease & pest models in parallel…"):
                disease_result = None
                pest_results = []
                disease_error = None
                pest_error = None

                with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                    future_disease = executor.submit(predict_disease, image)
                    future_pest = executor.submit(predict_pest, image)
                    
                    try:
                        disease_result = future_disease.result()
                    except Exception as e:
                        disease_error = str(e)
                    
                    try:
                        pest_results = future_pest.result()
                    except Exception as e:
                        pest_error = str(e)

                st.session_state["analysis"] = {
                    "file": uploaded_name,
                    "disease_result": disease_result,
                    "pest_results": pest_results,
                    "disease_error": disease_error,
                    "pest_error": pest_error,
                }
                st.session_state.pop("advisory_result", None)
                st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2 — PREDICTIONS
# ─────────────────────────────────────────────────────────────────────────────

analysis = st.session_state.get("analysis")

if analysis:
    st.divider()

    if analysis["disease_error"]:
        st.error(f"Disease model error: {analysis['disease_error']}")
    if analysis["pest_error"]:
        st.error(f"Pest model error: {analysis['pest_error']}")

    dr = analysis["disease_result"]
    pr = analysis["pest_results"]

    if dr:
        st.markdown('<div class="upload-label">Step 2 — Review predictions</div>', unsafe_allow_html=True)

        col_d, col_p = st.columns(2, gap="large")

        with col_d:
            conf_pct = int(dr["confidence"] * 100)
            conf_color = "#f48a8a" if conf_pct < 60 else "#f4c97a" if conf_pct < 80 else "#7ec87e"
            st.markdown(
                f"""
                <div class="pred-card">
                    <div class="pred-label">🦠 Disease model</div>
                    <div class="pred-name">{dr["disease"]}</div>
                    <div class="conf-bar-bg">
                        <div class="conf-bar-fg" style="width:{conf_pct}%; background:linear-gradient(90deg,{conf_color},{conf_color}88);"></div>
                    </div>
                    <div class="conf-text">Confidence: <strong style="color:{conf_color}">{conf_pct}%</strong></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if dr.get("top3"):
                with st.expander("See top-3 predictions"):
                    for label, c in dr["top3"]:
                        pct = int(c * 100)
                        st.markdown(
                            f"""
                            <div style="margin-bottom:8px">
                                <div style="font-size:13px; color:#c4cfa8; margin-bottom:3px">{label}</div>
                                <div class="conf-bar-bg">
                                    <div class="conf-bar-fg" style="width:{pct}%"></div>
                                </div>
                                <div class="conf-text">{pct}%</div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

        with col_p:
            if pr:
                for pest in pr[:3]:
                    pct = int(pest["confidence"] * 100)
                    conf_color = "#f48a8a" if pct < 60 else "#f4c97a" if pct < 80 else "#7ec87e"
                    st.markdown(
                        f"""
                        <div class="pred-card">
                            <div class="pred-label">🐛 Pest detector</div>
                            <div class="pred-name">{pest["pest"]}</div>
                            <div class="conf-bar-bg">
                                <div class="conf-bar-fg" style="width:{pct}%; background:linear-gradient(90deg,{conf_color},{conf_color}88);"></div>
                            </div>
                            <div class="conf-text">Confidence: <strong style="color:{conf_color}">{pct}%</strong></div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                st.markdown(
                    """
                    <div class="pred-card" style="text-align:center; padding: 30px;">
                        <div class="pred-label">No pests detected</div>
                        <p style="font-size:13px; color:#5a7a5a; margin:0">The pest model found no significant detections.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # ── Prediction selector ──
        st.divider()
        st.markdown('<div class="upload-label">Step 3 — Select prediction to advise on</div>', unsafe_allow_html=True)

        choices = [f"Disease: {dr['disease']}"] + [f"Pest: {p['pest']}" for p in pr]

        # Pick highest-confidence default
        best = dr["disease"]
        best_conf = dr["confidence"]
        for p in pr:
            if p["confidence"] > best_conf:
                best = p["pest"]
                best_conf = p["confidence"]
        default_choice = f"Disease: {dr['disease']}" if best == dr["disease"] else f"Pest: {best}"

        selected = st.radio(
            "Which detection should the advisory focus on?",
            choices,
            index=choices.index(default_choice) if default_choice in choices else 0,
            horizontal=True,
        )

        if selected.startswith("Disease: "):
            advisory_prediction = dr["disease"]
            advisory_confidence = dr["confidence"]
        else:
            advisory_prediction = selected.replace("Pest: ", "", 1)
            advisory_confidence = next(
                p["confidence"] for p in pr if p["pest"] == advisory_prediction
            )

        # ─────────────────────────────────────────────────────────────────────
        # STEP 4 — SYMPTOM QUESTIONS
        # ─────────────────────────────────────────────────────────────────────
        st.divider()
        st.markdown('<div class="upload-label">Step 4 — Describe field symptoms</div>', unsafe_allow_html=True)

        symptom_questions = {
            "Yellowing / chlorosis visible on leaves": False,
            "Water-soaked or necrotic lesions present": False,
            "Visible fungal growth (white/grey powder or mold)": False,
            "Stunted plant growth compared to healthy plants": False,
            "Wilting despite adequate watering": False,
        }

        answers = {}
        cols = st.columns(2)
        for i, q in enumerate(symptom_questions):
            with cols[i % 2]:
                answers[q] = st.checkbox(q, key=f"symptom_{i}")

        # ─────────────────────────────────────────────────────────────────────
        # STEP 5 — RISK INPUTS
        # ─────────────────────────────────────────────────────────────────────
        st.divider()
        st.markdown('<div class="upload-label">Step 5 — Field risk factors</div>', unsafe_allow_html=True)

        rc1, rc2, rc3 = st.columns(3, gap="large")
        with rc1:
            rapid_spread = st.checkbox("📈 Rapid spread observed (last 48 hrs)")
        with rc2:
            stem_damage = st.checkbox("🪵 Stem / root damage visible")
        with rc3:
            crop_percentage = st.slider(
                "Estimated crop area affected (%)",
                min_value=0, max_value=100, value=20, step=5,
                format="%d%%",
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("✨ Generate Field Advisory", type="primary", use_container_width=True):
            with st.spinner("Generating advisory…"):
                st.session_state["advisory_result"] = run_advisory_pipeline(
                    prediction=advisory_prediction,
                    model_confidence=advisory_confidence,
                    answers=answers,
                    rapid_spread=rapid_spread,
                    stem_damage=stem_damage,
                    crop_percentage=crop_percentage,
                )
            st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# RESULTS (Crash-Proof Version)
# ─────────────────────────────────────────────────────────────────────────────

advisory_result = st.session_state.get("advisory_result")

if advisory_result:
    st.divider()
    st.markdown('<div class="upload-label">Advisory report</div>', unsafe_allow_html=True)

    # Safely extract data with fallbacks
    risk = advisory_result.get("risk_level", "Unknown")
    summary = advisory_result.get("summary", "No summary was generated by the model.")
    treatments = advisory_result.get("treatment", ["Consult a local agronomist."])
    preventions = advisory_result.get("prevention", ["Maintain standard field hygiene."])
    confidence_note = advisory_result.get("confidence_note", "No additional confidence data provided.")

    badge_cls = {
        "High": "badge-high",
        "Medium": "badge-medium",
        "Low": "badge-low",
    }.get(risk, "badge-low")

    st.markdown(
        f'<span class="badge {badge_cls}">{risk} Risk</span>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Summary
    st.markdown(
        f"""
        <div class="result-section">
            <div class="result-section-title">📝 Situation summary</div>
            <p style="font-size:14px; color:#c4cfa8; line-height:1.6; margin:0">{summary}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_t, col_p = st.columns(2, gap="large")

    with col_t:
        items_html = "".join(
            f'<div class="result-item"><div class="result-dot"></div><div>{item}</div></div>'
            for item in treatments
        )
        st.markdown(
            f"""
            <div class="result-section">
                <div class="result-section-title">💊 Recommended treatments</div>
                {items_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_p:
        items_html = "".join(
            f'<div class="result-item"><div class="result-dot" style="background:#7ec87e"></div><div>{item}</div></div>'
            for item in preventions
        )
        st.markdown(
            f"""
            <div class="result-section">
                <div class="result-section-title">🛡️ Prevention for next season</div>
                {items_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="result-section" style="border-color:#2d4020; background:#111d10">
            <div class="result-section-title" style="color:#a0b878">⚠️ Confidence & disclaimer</div>
            <p style="font-size:13px; color:#7a9060; line-height:1.6; margin:0">{confidence_note}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🔄 Start new analysis", use_container_width=True):
        for key in ["analysis", "advisory_result", "models_preloaded"]:
            st.session_state.pop(key, None)
        st.rerun()