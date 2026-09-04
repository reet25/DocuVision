import cv2
import numpy as np


def calculate_sharpness(image):
    """
    Measure image sharpness using variance of Laplacian.
    Higher value generally indicates a sharper image.
    """
    return cv2.Laplacian(
        image,
        cv2.CV_64F
    ).var()


def calculate_brightness(image):
    """
    Calculate average pixel intensity.
    """
    return np.mean(image)


def calculate_contrast(image):
    """
    Calculate contrast using standard deviation.
    """
    return np.std(image)


def calculate_quality_score(sharpness, brightness, contrast):
    """
    Calculate an overall document quality score.
    """

    sharpness_score = min(sharpness / 500, 1.0)

    brightness_score = 1 - abs(
        brightness - 127.5
    ) / 127.5

    contrast_score = min(
        contrast / 80,
        1.0
    )

    score = (
        0.5 * sharpness_score
        + 0.25 * brightness_score
        + 0.25 * contrast_score
    )

    return round(score * 100, 2)


def classify_quality(score):
    """
    Classify the document based on its quality score.
    """

    if score >= 75:
        return "Excellent"
    elif score >= 50:
        return "Good"
    else:
        return "Poor"


def analyze_quality(image):
    """
    Perform complete document quality analysis.
    """

    sharpness = calculate_sharpness(image)
    brightness = calculate_brightness(image)
    contrast = calculate_contrast(image)

    quality_score = calculate_quality_score(
        sharpness,
        brightness,
        contrast
    )

    classification = classify_quality(
        quality_score
    )

    return {
        "sharpness": round(sharpness, 2),
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "quality_score": quality_score,
        "classification": classification
    }