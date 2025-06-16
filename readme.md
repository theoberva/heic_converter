# 📸 HEIC to Image Converter

A modern, user-friendly web application built with Streamlit that converts HEIC/HEIF images (commonly from iPhones) to standard image formats like PNG, JPEG, WEBP, and BMP.

![HEIC Converter Demo](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## ✨ Features

- **Batch Processing**: Convert multiple HEIC files simultaneously
- **Multiple Output Formats**: Support for PNG, JPEG, WEBP, and BMP
- **Quality Control**: Adjustable JPEG quality settings (1-100)
- **Image Resizing**: Optional resizing to reduce file size
- **Progress Tracking**: Real-time conversion progress with visual feedback
- **ZIP Download**: Automatic packaging of converted images
- **Modern UI**: Clean, responsive interface with detailed file information
- **Error Handling**: Comprehensive error reporting and recovery

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heic-converter.git
   cd heic-converter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📋 Usage

1. **Upload Files**: Click the upload area and select one or more HEIC/HEIF files
2. **Choose Settings**:
   - Select output format (PNG, JPEG, WEBP, BMP)
   - Adjust JPEG quality if needed (for JPEG output)
   - Enable resizing and set dimensions if desired
3. **Convert**: Click the "Convert Images" button
4. **Download**: Once conversion is complete, download the ZIP file containing all converted images

## 🛠️ Technical Details

### Supported Formats

**Input:**
- HEIC (High Efficiency Image Container)
- HEIF (High Efficiency Image Format)

**Output:**
- PNG (Portable Network Graphics)
- JPEG (Joint Photographic Experts Group)
- WEBP (Web Picture format)
- BMP (Bitmap)

### Key Dependencies

- **Streamlit**: Web application framework
- **Pillow (PIL)**: Python Imaging Library for image processing
- **pillow-heif**: HEIC/HEIF support for Pillow

## 📁 Project Structure

```
heic-converter/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore file
```

## 🔧 Configuration

The application includes several configurable options:

- **Output Format**: Choose from PNG, JPEG, WEBP, or BMP
- **JPEG Quality**: Slider control from 1-100 (JPEG only)
- **Image Resizing**: Optional with custom width/height limits
- **Batch Size**: No limit on number of files (memory permitting)

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'pillow_heif'" Error**
   ```bash
   pip install pillow-heif
   ```

2. **Memory Issues with Large Files**
   - Try processing fewer files at once
   - Enable resizing to reduce memory usage
   - Ensure sufficient system RAM

3. **Conversion Failures**
   - Check that uploaded files are valid HEIC/HEIF format
   - Verify file isn't corrupted
   - Try converting files individually to isolate issues

### System Requirements

- **RAM**: 4GB minimum (8GB+ recommended for large batches)
- **Storage**: Temporary space for processing (2x input file size)
- **Browser**: Modern browser with JavaScript enabled

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web app framework
- [Pillow](https://python-pillow.org/) - For image processing capabilities
- [pillow-heif](https://github.com/bigcat88/pillow_heif) - For HEIC/HEIF support

## 📞 Support

If you encounter any problems or have suggestions, please:

1. Check the [Issues](https://github.com/yourusername/heic-converter/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your system and the error

## 🔄 Changelog

### v1.0.0
- Initial release
- Basic HEIC to PNG/JPEG conversion
- Batch processing support
- Modern UI with progress tracking
- Quality control and resizing options

---

**Made with ❤️ using Python and Streamlit**
