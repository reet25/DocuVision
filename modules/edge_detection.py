import cv2


def canny_edge_detection(image, low_threshold=50, high_threshold=150):
    """
    Detect edges using the Canny edge detection algorithm.
    """
    edges = cv2.Canny(image, low_threshold, high_threshold)

    return edges