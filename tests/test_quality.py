import numpy as np

from modules.quality_analysis import (
    calculate_sharpness,
    calculate_brightness,
    calculate_contrast,
    calculate_quality_score,
    classify_quality
)


def test_brightness():

    image = np.full(
        (100, 100),
        128,
        dtype=np.uint8
    )

    brightness = calculate_brightness(image)

    assert brightness == 128


def test_contrast():

    image = np.zeros(
        (100, 100),
        dtype=np.uint8
    )

    contrast = calculate_contrast(image)

    assert contrast == 0


def test_sharpness():

    image = np.zeros(
        (100, 100),
        dtype=np.uint8
    )

    sharpness = calculate_sharpness(image)

    assert sharpness == 0


def test_quality_score():

    score = calculate_quality_score(
        500,
        127.5,
        80
    )

    assert 0 <= score <= 100


def test_quality_classification():

    assert classify_quality(80) == "Excellent"
    assert classify_quality(60) == "Good"
    assert classify_quality(30) == "Poor"