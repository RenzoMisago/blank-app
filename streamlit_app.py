import streamlit as st
import os

st.title("Image Upload + URL Viewer")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Create a folder to store images
    save_dir = "uploaded_images"
    os.makedirs(save_dir, exist_ok=True)

    # Save file
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display image
    st.image(file_path, caption="Uploaded Image", use_column_width=True)

    # Generate local URL inside Streamlit
    st.success("Image URL:")
    st.code(f"/{file_path}", language="text")
