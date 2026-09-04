import cv2


def find_document_contour(image):
    """
    Detect the outer boundary of the document.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth the image to reduce text and ruled-line noise
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Threshold based on the bright paper against the darker background
    _, threshold = cv2.threshold(
        blurred,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Connect broken parts of the document boundary
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (15, 15)
    )

    closed = cv2.morphologyEx(
        threshold,
        cv2.MORPH_CLOSE,
        kernel
    )

    contours, _ = cv2.findContours(
        closed,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    image_area = image.shape[0] * image.shape[1]

    best_contour = None
    best_area = 0

    for contour in contours:

        area = cv2.contourArea(contour)

        # Document is expected to occupy a large part of the image
        if area < 0.30 * image_area:
            continue

        perimeter = cv2.arcLength(contour, True)

        approximation = cv2.approxPolyDP(
            contour,
            0.03 * perimeter,
            True
        )

        if len(approximation) == 4 and cv2.isContourConvex(approximation):

            if area > best_area:
                best_area = area
                best_contour = approximation

    return best_contour