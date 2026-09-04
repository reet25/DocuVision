import numpy as np

from modules.document_detection import find_document_contour


def test_document_detection_returns_none_for_blank_image():

    image = np.zeros(
        (500, 500, 3),
        dtype=np.uint8
    )

    contour = find_document_contour(image)

    assert contour is None