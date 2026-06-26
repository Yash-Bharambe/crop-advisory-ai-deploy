import streamlit as st
from PIL import Image


def render_upload():
    st.markdown("### 📸 Step 1: Upload Crop Image")

    uploaded_file = st.file_uploader(
        "Drag and drop your crop image or click to browse",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear, well-lit photo of the affected crop area"
    )

    if uploaded_file:
        pil_image = Image.open(
            uploaded_file
        ).convert("RGB")

        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(
                pil_image,
                caption="📷 Uploaded Crop Image",
                use_container_width=True
            )
        with col2:
            st.success(f"✅ File: {uploaded_file.name}")
            st.info(f"Size: {uploaded_file.size / 1024:.1f} KB")

        return pil_image, uploaded_file.name

    return None, None
