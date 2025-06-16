import streamlit as st
from PIL import Image
from pillow_heif import register_heif_opener
import io
import zipfile
import os
from datetime import datetime

# Register HEIC/HEIF format with Pillow
register_heif_opener()

# Page configuration
st.set_page_config(
    page_title="HEIC Converter",
    page_icon="📸",
    layout="wide"
)

st.markdown('<h1 class="main-header">📸 HEIC to Image Converter</h1>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.subheader("⚙️ Settings")
    
    output_format = st.selectbox(
        "Output Format",
        ["PNG", "JPEG", "WEBP", "BMP"],
        help="Choose the desired output format"
    )
    
    # Quality setting for JPEG
    quality = 95
    if output_format.upper() == "JPEG":
        quality = st.slider(
            "JPEG Quality",
            min_value=1,
            max_value=100,
            value=95,
            help="Higher values = better quality, larger file size"
        )
    
    # Resize option
    resize_option = st.checkbox("Resize Images", help="Resize images to reduce file size")
    
    if resize_option:
        col_w, col_h = st.columns(2)
        with col_w:
            max_width = st.number_input("Max Width", min_value=100, max_value=4000, value=1920)
        with col_h:
            max_height = st.number_input("Max Height", min_value=100, max_value=4000, value=1080)


    st.markdown('---')
    st.header("ℹ️ About")
    st.write("""
    This tool converts HEIC/HEIF images (commonly used by iPhones) 
    to standard formats like PNG or JPEG.
    
    **Features:**
    - Batch conversion
    - Multiple output formats
    - Quality settings
    - Automatic ZIP download
    - Progress tracking
    """)
    
    st.header("📋 Supported Formats")
    st.write("**Input:** HEIC, HEIF")
    st.write("**Output:** PNG, JPEG, WEBP, BMP")

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    # st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "📁 Upload HEIC files",
        type=["heic", "heif"],
        accept_multiple_files=True,
        help="Select one or more HEIC/HEIF files to convert"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Display file information
if uploaded_files:
    st.subheader("📋 File Information")
    
    total_size = sum(file.size for file in uploaded_files)
    
    # Statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Files Selected", len(uploaded_files))
    with col2:
        st.metric("Total Size", f"{total_size / (1024*1024):.1f} MB")
    with col3:
        st.metric("Output Format", output_format.upper())
    
    # File list
    with st.expander("View File Details"):
        for i, file in enumerate(uploaded_files, 1):
            st.write(f"{i}. **{file.name}** ({file.size / (1024*1024):.1f} MB)")

# Conversion button and process
if st.button("🚀 Convert Images", type="primary", use_container_width=True):
    if not uploaded_files:
        st.warning("⚠️ Please upload at least one HEIC file.")
    else:
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        converted_files = []
        failed_files = []
        
        # Create ZIP buffer
        buffer = io.BytesIO()
        
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
            for i, uploaded_file in enumerate(uploaded_files):
                try:
                    # Update progress
                    progress = (i + 1) / len(uploaded_files)
                    progress_bar.progress(progress)
                    status_text.text(f"Converting {i + 1}/{len(uploaded_files)}: {uploaded_file.name}")
                    
                    # Open and process image
                    image = Image.open(uploaded_file)
                    
                    # Resize if requested
                    if resize_option:
                        image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
                    
                    # Prepare output filename
                    file_root = os.path.splitext(uploaded_file.name)[0]
                    out_filename = f"{file_root}.{output_format.lower()}"
                    
                    # Convert and save
                    img_bytes = io.BytesIO()
                    
                    # Handle different formats
                    if output_format.upper() == "JPEG":
                        # Convert RGBA to RGB for JPEG
                        if image.mode in ('RGBA', 'LA', 'P'):
                            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
                            if image.mode == 'P':
                                image = image.convert('RGBA')
                            rgb_image.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                            image = rgb_image
                        image.save(img_bytes, format="JPEG", quality=quality, optimize=True)
                    else:
                        image.save(img_bytes, format=output_format.upper(), optimize=True)
                    
                    img_bytes.seek(0)
                    zipf.writestr(out_filename, img_bytes.read())
                    converted_files.append(uploaded_file.name)
                    
                except Exception as e:
                    failed_files.append(f"{uploaded_file.name}: {str(e)}")
                    st.error(f"❌ Failed to convert {uploaded_file.name}: {e}")
        
        # Final results
        buffer.seek(0)
        progress_bar.progress(1.0)
        status_text.text("Conversion completed!")
        
        # Show results
        if converted_files:
            st.success(f"🎉 Successfully converted {len(converted_files)} out of {len(uploaded_files)} images!")
            
            # Download button
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            zip_filename = f"converted_images_{timestamp}.zip"
            
            st.download_button(
                label="📥 Download Converted Images (ZIP)",
                data=buffer,
                file_name=zip_filename,
                mime="application/zip",
                use_container_width=True
            )
            
            # Show conversion summary
            with st.expander("📊 Conversion Summary"):
                st.write("**Successfully converted:**")
                for file in converted_files:
                    st.write(f"✅ {file}")
                
                if failed_files:
                    st.write("**Failed to convert:**")
                    for error in failed_files:
                        st.write(f"❌ {error}")
        
        else:
            st.error("❌ No files were successfully converted. Please check your files and try again.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        Made with ❤️ using Streamlit | Support for HEIC, HEIF → PNG, JPEG, WEBP, BMP
    </div>
    """, 
    unsafe_allow_html=True
)