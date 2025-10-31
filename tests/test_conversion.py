"""
Test the color-format conversion utilities.

"""

# SPDX-License-Identifier: BSD-3-Clause
# pylint: disable=protected-access

import pytest

import webcolors


@pytest.mark.parametrize(
    ["hex_value", "name"],
    [
        ("#ffffff", "white"),
        ("#fff", "white"),
        ("#000080", "navy"),
        ("#daa520", "goldenrod"),
    ],
    ids=["white-six-digit", "white-three-digit", "navy", "goldenrod"],
)
def test_hex_to_name(hex_value: str, name: str):
    """
    Conversion from hex to color name succeeds.

    """
    assert name == webcolors.hex_to_name(hex_value)


def test_hex_to_name_unnamed_in_any():
    """
    A hex code which does not correspond to a named color raises ValueError.

    """
    with pytest.raises(ValueError, match="has no defined color name"):
        webcolors.hex_to_name("#123456")


def test_hex_to_name_unnamed_in_spec():
    """
    A hex code which does not correspond to a named color in the given specification
    raises ValueError.

    """
    # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
    with pytest.raises(ValueError, match="has no defined color name"):
        webcolors.hex_to_name("#daa520", spec=webcolors.HTML4)


@pytest.mark.parametrize("spec", webcolors._definitions._SUPPORTED_SPECIFICATIONS)
def test_hex_to_name_supported_spec(spec: str):
    """
    Explicitly using one of the supported specifications succeeds.

    """
    assert "white" == webcolors.hex_to_name("#ffffff", spec=spec)


@pytest.mark.parametrize("spec", ["css1", "css4", "html5"])
def test_hex_to_name_unspported_spec(spec: str):
    """
    Using an unsupported specification raises ValueError.

    """
    with pytest.raises(ValueError, match="not a supported specification"):
        webcolors.hex_to_name("#ffffff", spec=spec)


@pytest.mark.parametrize(
    ["hex_value", "triplet"],
    [("#fff", (255, 255, 255)), ("#ffffff", (255, 255, 255)), ("#000080", (0, 0, 128))],
    ids=["white-three-digit", "white-six-digit", "navy"],
)
def test_hex_to_rgb(hex_value: str, triplet: webcolors.IntTuple):
    """
    Conversion from hex to integer RGB triplet succeeds.

    """
    result = webcolors.hex_to_rgb(hex_value)
    assert isinstance(result, webcolors.IntegerRGB)
    assert triplet == result


@pytest.mark.parametrize(
    ["hex_value", "triplet"],
    [
        ("#fff", ("100%", "100%", "100%")),
        ("#ffffff", ("100%", "100%", "100%")),
        ("#000080", ("0%", "0%", "50%")),
    ],
    ids=["white-three-digit", "white-six-digit", "navy"],
)
def test_hex_to_rgb_percent(hex_value: str, triplet: webcolors.PercentTuple):
    """
    Conversion from hex to percent RGB triplet succeeds.

    """
    result = webcolors.hex_to_rgb_percent(hex_value)
    assert isinstance(result, webcolors.PercentRGB)
    assert triplet == result


@pytest.mark.parametrize(
    ["triplet", "name"],
    [
        ((255, 255, 255), "white"),
        ((0, 0, 128), "navy"),
        ((218, 165, 32), "goldenrod"),
        (webcolors.IntegerRGB(218, 165, 32), "goldenrod"),
    ],
    ids=["white", "navy", "goldenrod", "goldenrod-integerrgb"],
)
def test_rgb_to_name(triplet: webcolors.IntTuple, name: str):
    """
    Conversion from integer RGB triplet to color name succeeds.

    """
    assert name == webcolors.rgb_to_name(triplet)


def test_rgb_to_name_unnamed_in_any():
    """
    An integer RGB triplet which does not correspond to a named color raises ValueError.

    """
    with pytest.raises(ValueError, match="has no defined color name"):
        webcolors.rgb_to_name((18, 52, 86))


def test_rgb_to_name_unnamed_in_spec():
    """
    An integer RGB triplet which does not correspond to a named color in the given
    specification raises ValueError.

    """
    # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
    with pytest.raises(ValueError, match="has no defined color name"):
        webcolors.rgb_to_name((218, 165, 32), spec=webcolors.HTML4)


@pytest.mark.parametrize("spec", webcolors._definitions._SUPPORTED_SPECIFICATIONS)
def test_rgb_to_name_supported_spec(spec: str):
    """
    Using one of the supported specifications succeeds.

    """
    assert "white" == webcolors.rgb_to_name((255, 255, 255), spec=spec)


@pytest.mark.parametrize("spec", ["css1", "css4", "html5"])
def test_rgb_to_name_unsupported_spec(spec: str):
    """
    Using an unsupported specification raises ValueError.

    """
    with pytest.raises(ValueError, match="not a supported specification"):
        webcolors.rgb_to_name((255, 255, 255), spec=spec)


@pytest.mark.parametrize(
    ["triplet", "hex_value"],
    [
        ((255, 255, 255), "#ffffff"),
        ((0, 0, 128), "#000080"),
        ((218, 165, 32), "#daa520"),
    ],
    ids=["white", "navy", "goldenrod"],
)
def test_rgb_to_hex(triplet: webcolors.IntTuple, hex_value: str):
    """
    Conversion from integer RGB triplet to hex succeeds.

    """
    assert hex_value == webcolors.rgb_to_hex(triplet)


@pytest.mark.parametrize(
    ["triplet", "percent_triplet"],
    [
        ((255, 255, 255), ("100%", "100%", "100%")),
        ((0, 0, 128), ("0%", "0%", "50%")),
        ((218, 165, 32), ("85.49%", "64.71%", "12.5%")),
    ],
    ids=["white", "navy", "goldenrod"],
)
def test_rgb_to_rgb_percent(
    triplet: webcolors.IntTuple, percent_triplet: webcolors.PercentTuple
):
    """
    Conversion from integer RGB triplet to percent RGB triplet succeeds.

    """
    result = webcolors.rgb_to_rgb_percent(triplet)
    assert isinstance(result, webcolors.PercentRGB)
    assert percent_triplet == result


@pytest.mark.parametrize(
    ["name", "hex_value"],
    [("white", "#ffffff"), ("navy", "#000080"), ("goldenrod", "#daa520")],
    ids=["white", "navy", "goldenrod"],
)
def test_name_to_hex(name: str, hex_value: str):
    """
    Test correct conversion of color names to hex.

    """
    assert hex_value == webcolors.name_to_hex(name)


@pytest.mark.parametrize(
    ["name", "spec"], [("goldenrod", "html4"), ("glue", "css21"), ("breen", "css3")]
)
def test_name_to_hex_unnamed(name: str, spec: str):
    """
    A name which does not correspond to a color, or does not correspond to a
    color in the given specification, raises ValueError.

    """
    with pytest.raises(ValueError, match="is not defined as a named color"):
        webcolors.name_to_hex(name, spec=spec)


@pytest.mark.parametrize("spec", webcolors._definitions._SUPPORTED_SPECIFICATIONS)
def test_name_to_hex_supported_spec(spec: str):
    """
    Using one of the supported specifications succeeds.

    """
    assert "#ffffff" == webcolors.name_to_hex("white", spec=spec)


@pytest.mark.parametrize("spec", ["css1", "css4", "html5"])
def test_name_to_hex_usupported_spec(spec: str):
    """
    Using an unsupported specification raises ValueError.

    """
    with pytest.raises(ValueError, match="not a supported specification"):
        webcolors.name_to_hex("white", spec=spec)


@pytest.mark.parametrize(
    ["name", "triplet"],
    [("white", (255, 255, 255)), ("navy", (0, 0, 128)), ("goldenrod", (218, 165, 32))],
    ids=["white", "navy", "goldenrod"],
)
def test_name_to_rgb(name: str, triplet: webcolors.IntTuple):
    """
    Conversion from color name to integer RGB triplet succeeds.

    """
    result = webcolors.name_to_rgb(name)
    assert isinstance(result, webcolors.IntegerRGB)
    assert triplet == result


@pytest.mark.parametrize(
    ["name", "triplet"],
    [
        ("white", ("100%", "100%", "100%")),
        ("navy", ("0%", "0%", "50%")),
        ("goldenrod", ("85.49%", "64.71%", "12.5%")),
    ],
    ids=["white", "navy", "goldenrod"],
)
def test_name_to_rgb_percent(name: str, triplet: webcolors.PercentTuple):
    """
    Conversion from color name to percent RGB triplet succeeds.

    """
    result = webcolors.name_to_rgb_percent(name)
    assert isinstance(result, webcolors.PercentRGB)
    assert triplet == result


@pytest.mark.parametrize(
    ["triplet", "name"],
    [
        (("100%", "100%", "100%"), "white"),
        (("0%", "0%", "50%"), "navy"),
        (("85.49%", "64.71%", "12.5%"), "goldenrod"),
        (webcolors.PercentRGB("85.49%", "64.71%", "12.5%"), "goldenrod"),
    ],
    ids=["white", "navy", "goldenrod", "goldenrod-percentrgb"],
)
def test_rgb_percent_to_name(triplet: webcolors.PercentTuple, name: str):
    """
    Conversion from percent RGB triplet to color name succeeds.

    """
    assert name == webcolors.rgb_percent_to_name(triplet)


def test_rgb_percent_to_name_unnamed_in_any():
    """
    A percent RGB triplet which does not correspond to a named color raises ValueError.

    """
    with pytest.raises(ValueError, match="has no defined color name"):
        webcolors.rgb_percent_to_name(("7.06%", "20.39%", "33.73%"))


def test_rgb_percent_to_name_unnamed_in_spec():
    """
    A percent RGB triplet which does not correspond to a named color in the given
    specification raises ValueError.

    """
    # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
    with pytest.raises(ValueError, match="has no defined color name"):
        webcolors.rgb_percent_to_name(
            ("85.49%", "64.71%", "12.5%"), spec=webcolors.HTML4
        )


@pytest.mark.parametrize("spec", webcolors._definitions._SUPPORTED_SPECIFICATIONS)
def test_rgb_percent_to_name_supported_spec(spec: str):
    """
    Using one of the supported specifications succeeds.

    """
    assert "white" == webcolors.rgb_percent_to_name(("100%", "100%", "100%"), spec=spec)


@pytest.mark.parametrize("spec", ["css1", "css4", "html5"])
def test_rgb_percent_to_name_unsupported_spec(spec: str):
    """
    Using an unsupported specification raises ValueError.

    """
    with pytest.raises(ValueError, match="not a supported specification"):
        webcolors.rgb_percent_to_name(("100%", "100%", "100%"), spec=spec)


@pytest.mark.parametrize(
    ["triplet", "hex_value"],
    [
        (("100%", "100%", "0%"), "#ffff00"),
        (("0%", "0%", "50%"), "#000080"),
        (("85.49%", "64.71%", "12.5%"), "#daa520"),
    ],
    ids=["white", "navy", "goldenrod"],
)
def test_rgb_percent_to_hex(triplet: webcolors.PercentTuple, hex_value: str):
    """
    Conversion from percent RGB triplet to hex succeeds.

    """
    assert hex_value == webcolors.rgb_percent_to_hex(triplet)


@pytest.mark.parametrize(
    ["triplet", "int_triplet"],
    [
        (("100%", "100%", "0%"), (255, 255, 0)),
        (("0%", "0%", "50%"), (0, 0, 128)),
        (("85.49%", "64.71%", "12.5%"), (218, 165, 32)),
    ],
)
def test_rgb_percent_to_rgb(
    triplet: webcolors.PercentTuple, int_triplet: webcolors.IntTuple
):
    """
    Conversion from percent RGB triplet to integer RGB triplet succeeds.

    """
    result = webcolors.rgb_percent_to_rgb(triplet)
    assert isinstance(result, webcolors.IntegerRGB)
    assert int_triplet == result


@pytest.mark.parametrize(
    ["value", "name"],
    [
        ("#a9a9a9", "darkgray"),
        ("#2f4f4f", "darkslategray"),
        ("#696969", "dimgray"),
        ("#808080", "gray"),
        ("#d3d3d3", "lightgray"),
        ("#778899", "lightslategray"),
        ("#708090", "slategray"),
    ],
    ids=[
        "darkgray",
        "darkslategray",
        "dimgray",
        "gray",
        "lightgray",
        "lightslategray",
        "slategray",
    ],
)
def test_spelling_variants_hex(value: str, name: str):
    """
    When asked to name a hex color value that maps to either of 'gray' or 'grey' in
    CSS3, or a related color like 'darkgray'/'darkgrey', webcolors always picks
    'gray' as the spelling.

    """
    assert name == webcolors.hex_to_name(value, spec=webcolors.CSS3)


@pytest.mark.parametrize(
    ["value", "name"],
    [
        ((169, 169, 169), "darkgray"),
        ((47, 79, 79), "darkslategray"),
        ((105, 105, 105), "dimgray"),
        ((128, 128, 128), "gray"),
        ((211, 211, 211), "lightgray"),
        ((119, 136, 153), "lightslategray"),
        ((112, 128, 144), "slategray"),
    ],
    ids=[
        "darkgray",
        "darkslategray",
        "dimgray",
        "gray",
        "lightgray",
        "lightslategray",
        "slategray",
    ],
)
def test_spelling_variants_int(value: webcolors.IntTuple, name: str):
    """
    When asked to name an integer RGB color value that maps to either of 'gray' or
    'grey' in CSS3, or a related color like 'darkgray'/'darkgrey', webcolors always
    picks 'gray' as the spelling.

    """
    assert name == webcolors.rgb_to_name(value, spec=webcolors.CSS3)


@pytest.mark.parametrize(
    ["value", "name"],
    [
        (("66.27%", "66.27%", "66.27%"), "darkgray"),
        (("18.43%", "30.98%", "30.98%"), "darkslategray"),
        (("41.18%", "41.18%", "41.18%"), "dimgray"),
        (("50%", "50%", "50%"), "gray"),
        (("82.75%", "82.75%", "82.75%"), "lightgray"),
        (("46.67%", "53.33%", "60.00%"), "lightslategray"),
        (("43.92%", "50%", "56.47%"), "slategray"),
    ],
    ids=[
        "darkgray",
        "darkslategray",
        "dimgray",
        "gray",
        "lightgray",
        "lightslategray",
        "slategray",
    ],
)
def test_spelling_variants_percent(value: webcolors.PercentTuple, name: str):
    """
    When asked to name a percent RGB color value that maps to either of 'gray' or 'grey'
    in CSS3, or a related color like 'darkgray'/'darkgrey', webcolors always picks
    'gray' as the spelling.

    """
    assert name == webcolors.rgb_percent_to_name(value, spec=webcolors.CSS3)


@pytest.mark.parametrize(
    ["spec", "mapping"],
    [
        (webcolors.HTML4, webcolors._definitions._HTML4_NAMES_TO_HEX),
        (webcolors.CSS2, webcolors._definitions._CSS2_NAMES_TO_HEX),
        (webcolors.CSS21, webcolors._definitions._CSS21_NAMES_TO_HEX),
        (webcolors.CSS3, webcolors._definitions._CSS3_NAMES_TO_HEX),
    ],
    ids=["html4", "css2", "css21", "css3"],
)
def test_names_valid(spec: str, mapping: dict):
    """
    names() correctly returns the set of names for a given spec.

    """
    assert webcolors.names(spec) == list(sorted(mapping.keys()))


@pytest.mark.parametrize("spec", ["CSS0", "HTML12", "random"])
def test_names_invalid(spec: str):
    """
    names() raises ValueError when asked for an unsupported spec.

    """
    with pytest.raises(ValueError, match="not a supported specification"):
        webcolors.names(spec)
