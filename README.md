# DocuVision

**Computer Vision Based Document Scanner, Enhancement & Quality Analyzer**

DocuVision is a classical computer vision project that processes photographs of physical documents. It automatically detects the document, corrects perspective distortion, enhances the resulting image, and evaluates its visual quality.

## Overview

Photographs of documents can contain perspective distortion, noise, uneven lighting, and reduced readability. DocuVision addresses these issues through a structured image-processing pipeline.

The system takes a document photograph as input and produces:

* A perspective-corrected document
* An enhanced grayscale document
* A document quality report

## Features

* Input image validation
* Image resizing and preprocessing
* Grayscale conversion
* Gaussian filtering
* Canny edge detection
* Document boundary detection using thresholding and contours
* Four-corner document detection
* Perspective correction using homography
* Contrast enhancement using CLAHE
* Image sharpening
* Sharpness, brightness, and contrast analysis
* Overall document quality score
* Quality classification
* Output validation
* Automated unit testing

## Computer Vision Concepts Used

The project demonstrates the following classical computer vision concepts:

* Image preprocessing
* Convolution and Gaussian filtering
* Edge detection
* Canny edge detection
* Image segmentation through thresholding
* Contour detection
* Object/document detection
* Projective transformation
* Homography
* Perspective correction
* Image rectification
* Image enhancement
* Contrast enhancement

## System Workflow

```text
Input Image
     ↓
Image Validation
     ↓
Preprocessing
     ↓
Grayscale + Gaussian Blur
     ↓
Canny Edge Detection
     ↓
Document Detection
     ↓
Four-Corner Detection
     ↓
Homography / Perspective Correction
     ↓
Document Enhancement
     ↓
Quality Analysis
     ↓
Output Images + Quality Report
```

## Project Structure

```text
DocuVision/
│
├── app.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
│
├── modules/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── edge_detection.py
│   ├── document_detection.py
│   ├── perspective.py
│   ├── enhancement.py
│   └── quality_analysis.py
│
├── utils/
│   └── validation.py
│
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_detection.py
│   └── test_quality.py
│
├── data/
│   └── sample_images/
│       └── document.jpeg
│
└── outputs/
    ├── scanned_document.jpg
    ├── enhanced_document.jpg
    └── quality_report.txt
```

## Technologies Used

* Python
* OpenCV
* NumPy
* Pytest

## Installation

Clone the repository:

```bash
git clone https://github.com/reet25/DocuVision.git
cd DocuVision
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Place the input document image at:

```text
data/sample_images/document.jpeg
```

Run:

```bash
python app.py
```

The processed files will be generated in:

```text
outputs/
```

The output includes:

```text
scanned_document.jpg
enhanced_document.jpg
quality_report.txt
```

## Testing

The project uses Pytest for unit testing.

Run:

```bash
pytest
```

The current test suite contains **9 tests** covering preprocessing, document detection, and quality-analysis functionality.

## Quality Analysis

DocuVision evaluates the processed document using:

* **Sharpness:** calculated using the variance of the Laplacian.
* **Brightness:** calculated using average pixel intensity.
* **Contrast:** calculated using standard deviation of pixel intensity.
* **Quality Score:** a weighted engineering score based on the above metrics.

The quality-score thresholds are project-specific engineering thresholds and are not intended to represent a scientifically validated document-quality standard.

## Output

The system generates:

1. **Scanned Document** — perspective-corrected document.
2. **Enhanced Document** — contrast-enhanced and sharpened grayscale document.
3. **Quality Report** — numerical quality metrics and classification.

## Project Scope

DocuVision focuses on classical computer vision techniques for document image processing.

The current MVP does **not** include:

* OCR
* Database storage
* Machine learning model training
* Cloud deployment
* Web application interface

These features are outside the current project scope.

## Limitations

The document detector works best when:

* The document has a reasonably clear boundary.
* The document occupies a significant portion of the image.
* There is sufficient contrast between the document and its background.
* The document has an approximately quadrilateral shape.

Highly cluttered backgrounds, severe occlusion, extreme lighting, or heavily distorted documents may reduce detection accuracy.

## Future Enhancements

Possible future improvements include:

* Automatic document-quality feedback before scanning
* Support for multiple document types
* Improved robustness under complex backgrounds
* OCR-based text extraction
* Mobile or web-based interface
* Additional image-quality metrics

## Author

**Reet Dubey**

B.Tech. Computer Science and Engineering (Artificial Intelligence & Machine Learning)

VIT Bhopal University
