# DocuVision

## Problem Statement

Taking photographs of physical documents using a mobile phone or camera often produces images with perspective distortion, uneven lighting, blur, and poor readability. Manually correcting these issues can be time-consuming and requires additional software.

DocuVision is designed to provide a simple computer vision based solution that automatically detects a document in an input image, corrects its perspective, enhances its visual quality, and evaluates the quality of the resulting document.

## Project Scope

The project focuses on classical computer vision techniques for processing photographs of documents.

The system will:

* Validate the input image.
* Preprocess the image using resizing, grayscale conversion, and Gaussian filtering.
* Detect edges using the Canny edge detection technique.
* Detect the document boundary using thresholding and contour analysis.
* Identify the four document corners.
* Apply projective transformation and homography for perspective correction.
* Enhance the corrected document using contrast enhancement and sharpening.
* Calculate basic image quality metrics including sharpness, brightness, and contrast.
* Generate an overall quality score and quality classification.
* Save the processed document and quality report as output files.

The project does not include OCR, database storage, cloud deployment, or machine learning model training.

## Target Users

The primary target users are:

* Students who need to digitize academic documents.
* Users who want to convert photographs of documents into cleaner digital copies.
* Individuals who need basic document image quality assessment.
* Developers and learners studying practical applications of classical computer vision.

## High-Level Features

1. **Image Validation and Preprocessing**
   Validates the input image and prepares it for further processing.

2. **Document Detection**
   Detects the document boundary and identifies its four corners using image processing and contour analysis.

3. **Perspective Correction**
   Uses projective transformation and homography to convert the photographed document into a top-down view.

4. **Document Enhancement**
   Improves local contrast and sharpness to make the corrected document more readable.

5. **Quality Analysis**
   Measures sharpness, brightness, and contrast and combines them into an overall quality score.

6. **Output Generation**
   Saves the corrected document, enhanced document, and quality report for further use.
