import cv2


def validate_image(image):
    """
    Validate that the input image was loaded successfully.
    """

    if image is None:
        return False, "Input image could not be loaded."

    if image.size == 0:
        return False, "Input image is empty."

    if len(image.shape) != 3:
        return False, "Input image must be a color image."

    if image.shape[2] != 3:
        return False, "Input image must have 3 color channels."

    return True, "Image validation successful."


def validate_output(image):
    """
    Validate that an output image was generated successfully.
    """

    if image is None:
        return False, "Output image is empty."

    if image.size == 0:
        return False, "Output image contains no data."

    return True, "Output validation successful."


def validate_document_contour(contour):
    """
    Validate that a four-corner document contour was detected.
    """

    if contour is None:
        return False, "No document contour detected."

    if len(contour) != 4:
        return False, "Detected document does not have four corners."

    return True, "Document contour validation successful."