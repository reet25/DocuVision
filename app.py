import cv2
import os

from modules.preprocessing import preprocess_image
from modules.edge_detection import canny_edge_detection
from modules.document_detection import find_document_contour
from modules.perspective import perspective_transform
from modules.enhancement import enhance_document
from modules.quality_analysis import analyze_quality
from utils.validation import (
    validate_image,
    validate_output,
    validate_document_contour
)

INPUT_PATH = "data/sample_images/document.jpeg"
OUTPUT_DIR = "outputs"


def main():

    # Create output directory if it does not exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load input image
    image = cv2.imread(INPUT_PATH)

    valid, message = validate_image(image)

    if not valid:
        print("Error:", message)
        return

    print(message)

    print("Image loaded successfully.")
    print("Original shape:", image.shape)

    # Step 1: Preprocessing
    results = preprocess_image(image)

    print("Preprocessing completed successfully.")
    print("Resized shape:", results["resized"].shape)
    print("Grayscale shape:", results["grayscale"].shape)

    # Step 2: Edge detection
    edges = canny_edge_detection(results["blurred"])

    print("Canny edge detection completed successfully.")
    print("Edge image shape:", edges.shape)

    # Step 3: Document detection
    document_contour = find_document_contour(
        results["resized"]
    )
    valid, message = validate_document_contour(
    document_contour
)

    if not valid:
        print("Error:", message)
        return

    print(message)

    print("Document detected successfully.")
    print(
        "Document corners:",
        document_contour.reshape(4, 2)
    )

    # Step 4: Perspective correction
    scanned_document = perspective_transform(
        results["resized"],
        document_contour
    )
    valid, message = validate_output(scanned_document)

    if not valid:
        print("Error:", message)
        return

    print(message)
    print("Perspective correction completed successfully.")
    print("Scanned document shape:", scanned_document.shape)

    # Save perspective-corrected document
    scanned_path = os.path.join(
        OUTPUT_DIR,
        "scanned_document.jpg"
    )

    cv2.imwrite(
        scanned_path,
        scanned_document
    )

    # Step 5: Document enhancement
    enhanced_document = enhance_document(
        scanned_document
    )
    valid, message = validate_output(enhanced_document)

    if not valid:
        print("Error:", message)
        return

    print(message)
    print("Document enhancement completed successfully.")
    print("Enhanced document shape:", enhanced_document.shape)

    # Save enhanced document
    enhanced_path = os.path.join(
        OUTPUT_DIR,
        "enhanced_document.jpg"
    )

    cv2.imwrite(
        enhanced_path,
        enhanced_document
    )

    # Step 6: Quality analysis
    quality = analyze_quality(
        enhanced_document
    )

    print("Quality analysis completed successfully.")
    print("Sharpness:", quality["sharpness"])
    print("Brightness:", quality["brightness"])
    print("Contrast:", quality["contrast"])
    print("Quality score:", quality["quality_score"])
    print("Classification:", quality["classification"])

    # Save quality report
    report_path = os.path.join(
        OUTPUT_DIR,
        "quality_report.txt"
    )

    with open(report_path, "w") as report:

        report.write("DocuVision Quality Report\n")
        report.write("========================\n\n")

        report.write(
            f"Sharpness: {quality['sharpness']}\n"
        )

        report.write(
            f"Brightness: {quality['brightness']}\n"
        )

        report.write(
            f"Contrast: {quality['contrast']}\n"
        )

        report.write(
            f"Quality Score: {quality['quality_score']}\n"
        )

        report.write(
            f"Classification: {quality['classification']}\n"
        )

    print("\nOutput files generated successfully:")
    print(scanned_path)
    print(enhanced_path)
    print(report_path)


if __name__ == "__main__":
    main()