import streamlit as st

st.title("DrBone AI - Fracture Detection 🦴")

uploaded_file = st.file_uploader("Upload X-ray Image", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image")

    # Dummy output (replace with YOLO later)
    st.success("Fracture Detected ✅")
    st.write("Confidence: 92%")
