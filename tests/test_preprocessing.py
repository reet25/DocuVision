import numpy as np

from modules.preprocessing import (
    resize_image,
    convert_to_grayscale,
    apply_gaussian_blur
)


def test_resize_image():
    image = np.zeros((1000, 1000, 3), dtype=np.uint8)

    resized = resize_image(image, width=800)

    assert resized.shape[1] == 800


def test_convert_to_grayscale():
    image = np.zeros((100, 100, 3), dtype=np.uint8)

    gray = convert_to_grayscale(image)

    assert len(gray.shape) == 2


def test_apply_gaussian_blur():
    image = np.zeros((100, 100), dtype=np.uint8)

    blurred = apply_gaussian_blur(image)

    assert blurred.shape == image.shape