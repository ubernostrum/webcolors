"""
Test the color-value normalization functions.

"""

# SPDX-License-Identifier: BSD-3-Clause

import pytest

import webcolors


@pytest.mark.parametrize(
    ["raw", "normalized"],
    [
        ("#0099cc", "#0099cc"),
        ("#0099CC", "#0099cc"),
        ("#09c", "#0099cc"),
        ("#09C", "#0099cc"),
    ],
    ids=["lowercase", "uppercase", "three-digit-lowercase", "three-digit-uppercase"],
)
def test_normalize_hex(raw: str, normalized: str):
    """
    Hexadecimal normalization normalizes valid hex color codes to 6 digits,
    lowercase.

    """
    assert normalized == webcolors.normalize_hex(raw)


@pytest.mark.parametrize(
    "hex_value",
    ["0099cc", "#0000gg", "#0000", "#00000000"],
    ids=["no-hash", "not-hex", "too-short", "too-long"],
)
def test_normalize_hex_format(hex_value: str):
    """
    Hex normalization raises ValueError on invalid hex color code.

    """
    with pytest.raises(ValueError, match="not a valid hexadecimal color value"):
        webcolors.normalize_hex(hex_value)


@pytest.mark.parametrize(
    ["raw", "normalized"],
    [(255, 255), (0, 0), (128, 128), (-20, 0), (270, 255), (-0, 0)],
    ids=["max", "min", "middle", "clipped-to-min", "clipped-to-max", "negative-zero"],
)
def test_normalize_integer_rgb(raw: int, normalized: int):
    """
    Integer normalization clips to 0-255.

    """
    # pylint: disable=protected-access
    assert normalized == webcolors._normalization._normalize_integer_rgb(raw)


@pytest.mark.parametrize(
    ["triplet", "normalized"],
    [
        ((128, 128, 128), (128, 128, 128)),
        ((0, 0, 0), (0, 0, 0)),
        ((255, 255, 255), (255, 255, 255)),
        ((270, -20, 128), (255, 0, 128)),
        ((-0, -0, -0), (0, 0, 0)),
    ],
    ids=["navy", "black", "white", "clipped", "negative-zero"],
)
def test_normalize_integer_triplet(
    triplet: webcolors.IntTuple, normalized: webcolors.IntTuple
):
    """
    Integer triplet normalization clips all values to 0-255.

    """
    result = webcolors.normalize_integer_triplet(triplet)
    assert isinstance(result, webcolors.IntegerRGB)
    assert normalized == result


@pytest.mark.parametrize(
    ["raw", "normalized"],
    [
        ("0%", "0%"),
        ("100%", "100%"),
        ("62%", "62%"),
        ("-5%", "0%"),
        ("250%", "100%"),
        ("85.49%", "85.49%"),
        ("-0%", "0%"),
    ],
    ids=[
        "min",
        "max",
        "not-special",
        "clipped-to-min",
        "clipped-to-max",
        "floating-point",
        "negative-zero",
    ],
)
def test_normalize_percent_rgb(raw: str, normalized: str):
    """
    Percent normalization clips to 0%-100%.

    """
    # pylint: disable=protected-access
    assert normalized == webcolors._normalization._normalize_percent_rgb(raw)


@pytest.mark.parametrize(
    ["triplet", "normalized"],
    [
        (("50%", "50%", "50%"), ("50%", "50%", "50%")),
        (("0%", "100%", "0%"), ("0%", "100%", "0%")),
        (("-10%", "250%", "500%"), ("0%", "100%", "100%")),
        (("-0%", "-0%", "-0%"), ("0%", "0%", "0%")),
    ],
    ids=["gray", "green", "clipped", "negative-zero"],
)
def test_normalize_percent_triplet(
    triplet: webcolors.PercentTuple, normalized: webcolors.PercentTuple
):
    """
    Percent triplet normalization clips all values to 0%-100%.

    """
    result = webcolors.normalize_percent_triplet(triplet)
    assert isinstance(result, webcolors.PercentRGB)
    assert normalized == result
