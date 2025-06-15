import streamlit as st
from PIL import Image
from pillow_heif import register_heif_opener
import io
import zipfile
import os

# Register HEIC/HEIF format with Pillow
register_heif_opener()

st.title("📸 HEIC to Image Converter")

uploaded_files = st.file_uploader(
    "Upload one or more HEIC files", 
    type=["heic"],
    accept_multiple_files=True
)

output_format = st.selectbox("Choose output format", ["png", "jpg"])

if st.button("Convert"):
    if not uploaded_files:
        st.warning("Please upload at least one HEIC file.")
    else:
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as zipf:
            for i, uploaded_file in enumerate(uploaded_files, 1):
                try:
                    image = Image.open(uploaded_file)
                    file_root = os.path.splitext(uploaded_file.name)[0]
                    out_filename = f"{file_root}.{output_format}"

                    img_bytes = io.BytesIO()
                    image.save(img_bytes, format=output_format)
                    img_bytes.seek(0)
                    zipf.writestr(out_filename, img_bytes.read())
                    
                    st.write(f"✅ Converted image {i}/{len(uploaded_files)}")
                except Exception as e:
                    st.error(f"❌ Failed to convert {uploaded_file.name}: {e}")

        buffer.seek(0)
        st.success(f"🎉 Successfully converted {len(uploaded_files)} images.")
        st.download_button(
            label="Download ZIP of Converted Images",
            data=buffer,
            file_name="converted_images.zip",
            mime="application/zip"
        )
