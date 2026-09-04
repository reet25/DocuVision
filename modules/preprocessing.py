import cv2
import numpy as np


def resize_image(image, width=800):
    """
    Resize an image while maintaining its aspect ratio.
    """
    height, original_width = image.shape[:2]

    if original_width <= width:
        return image

    ratio = width / original_width
    new_height = int(height * ratio)

    return cv2.resize(image, (width, new_height))


def convert_to_grayscale(image):
    """
    Convert a BGR image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """
    Apply Gaussian filtering to reduce image noise.
    """
    return cv2.GaussianBlur(image, kernel_size, 0)


def preprocess_image(image):
    """
    Complete preprocessing pipeline.
    """
    resized = resize_image(image)
    grayscale = convert_to_grayscale(resized)
    blurred = apply_gaussian_blur(grayscale)

    return {
        "resized": resized,
        "grayscale": grayscale,
        "blurred": blurred
    }