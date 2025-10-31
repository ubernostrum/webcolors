"""
Tests for the HTML5 color algorithms.

"""

# SPDX-License-Identifier: BSD-3-Claus
# pylint: disable=protected-access

import re

import pytest

import webcolors


@pytest.mark.parametrize(
    ["raw", "parsed"],
    [
        ("#ffffff", (255, 255, 255)),
        ("#000080", (0, 0, 128)),
        ("#daa520", (218, 165, 32)),
    ],
    ids=["white", "navy", "goldenrod"],
)
def test_parse_simple_color(raw: str, parsed: webcolors.IntTuple):
    """
    Test implementation of the HTML5 simple color parsing algorithm.

    """
    result = webcolors.html5_parse_simple_color(raw)
    assert isinstance(result, webcolors.HTML5SimpleColor)
    assert parsed == result


@pytest.mark.parametrize(
    ["value", "match"],
    [
        (
            "0099ccc",
            re.escape(
                "An HTML5 simple color must begin with the character '#' (U+0023)"
            ),
        ),
        (
            "#09c",
            "An HTML5 simple color must be a Unicode string seven characters long",
        ),
        (
            "#0000",
            "An HTML5 simple color must be a Unicode string seven characters long",
        ),
        (
            "#0000000",
            "An HTML5 simple color must be a Unicode string seven characters long",
        ),
        ("#0000gg", "An HTML5 simple color must contain exactly six ASCII hex digits"),
        (
            "#000000".encode("ascii"),
            "An HTML5 simple color must be a Unicode string seven characters long",
        ),
    ],
    ids=[
        "too-long-no-hash",
        "three-digit",
        "four-digit",
        "too-long",
        "not-hex",
        "not-unicode",
    ],
)
def test_parse_simple_color_error(value: str, match: str):
    """
    Test error conditions of the HTML5 simple color parsing algorithm.

    """
    with pytest.raises(ValueError, match=match):
        webcolors.html5_parse_simple_color(value)


@pytest.mark.parametrize(
    ["raw", "serialized"],
    [
        ((0, 0, 0), "#000000"),
        ((0, 0, 128), "#000080"),
        ((218, 165, 32), "#daa520"),
        (webcolors.IntegerRGB(218, 165, 32), "#daa520"),
        (webcolors.HTML5SimpleColor(218, 165, 32), "#daa520"),
    ],
    ids=["black", "navy", "goldenrod", "goldenrod-integerrgb", "goldenrod-html5tuple"],
)
def test_serialize_simple_color(raw: webcolors.IntTuple, serialized: str):
    """
    Test implementation of the HTML5 simple color serialization algorithm.

    """
    assert serialized == webcolors.html5_serialize_simple_color(raw)


@pytest.mark.parametrize(
    ["raw", "parsed"],
    [
        ("chucknorris", (192, 0, 0)),
        ("Window", (0, 13, 0)),
        ("RE|SXLuAse", (224, 0, 224)),
        ("+=@FnnWL!Yb}5Dk", (0, 0, 176)),
        ("A" * 129, (170, 170, 170)),
    ],
    ids=["chucknorris", "system-color", "junk1", "junk2", "junk3"],
)
def test_parse_legacy_color(raw: str, parsed: webcolors.IntTuple):
    """
    Test implementation of the HTML5 legacy color parsing algorithm.

    """
    result = webcolors.html5_parse_legacy_color(raw)
    assert isinstance(result, webcolors.HTML5SimpleColor)
    assert parsed == result


@pytest.mark.parametrize("name", webcolors._definitions._CSS3_NAMES_TO_HEX)
def test_parse_legacy_color_names(name: str):
    """
    Test the HTML5 legacy color parsing of SVG/CSS3 color names.

    """
    assert webcolors.html5_parse_legacy_color(name) == webcolors.name_to_rgb(name)


@pytest.mark.parametrize(
    "value",
    ["#000", "#000000", "#fff", "#ffffff", "#000080"],
    ids=[
        "three-digit-black",
        "six-digit-black",
        "three-digit-white",
        "six-digit-white",
        "navy",
    ],
)
def test_parse_legacy_color_hex(value: str):
    """
    Test the HTML5 legacy color parsing of three- and six-digit hexadecimal
    color values.

    """
    assert webcolors.html5_parse_legacy_color(value) == webcolors.hex_to_rgb(value)


@pytest.mark.parametrize(
    ["value", "match"],
    [
        (
            "#000000".encode("ascii"),
            "HTML5 legacy color parsing requires a Unicode string as input.",
        ),
        ("transparent", 'HTML5 legacy color parsing forbids "transparent" as a value.'),
        ("", "HTML5 legacy color parsing forbids empty string as a value."),
    ],
    ids=["non-unicode", "transparent", "empty"],
)
def test_parse_legacy_color_error(value: str, match: str):
    """
    Test error conditions of the HTML5 legacy color parsing algorithm.

    """
    with pytest.raises(ValueError, match=match):
        webcolors.html5_parse_legacy_color(value)
