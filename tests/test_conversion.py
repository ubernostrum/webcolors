"""
Test the color-format conversion utilities.

"""
import unittest

import webcolors


class HexConversionTests(unittest.TestCase):
    """
    Test the functions which convert from hex color codes to other
    formats.

    """

    def test_hex_to_name(self):
        """
        Test conversion from hex to color name.
        """
        test_pairs = (
            ("#ffffff", "white"),
            ("#fff", "white"),
            ("#000080", "navy"),
            ("#daa520", "goldenrod"),
        )

        for hex_value, name in test_pairs:
            assert name == webcolors.hex_to_name(hex_value)

    def test_hex_to_name_unnamed(self):
        """
        A hex code which does not correspond to a named color, or does
        not correspond to a named color in the given specification,
        raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(ValueError, webcolors.hex_to_name, "#123456")

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError, webcolors.hex_to_name, "#daa520", spec=webcolors.HTML4
        )

    def test_hex_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.

        """
        for supported_spec in webcolors.SUPPORTED_SPECIFICATIONS:
            result = webcolors.hex_to_name("#ffffff", spec=supported_spec)
            assert "white" == result

        for unsupported_spec in ("css1", "css4", "html5"):
            self.assertRaises(
                ValueError, webcolors.hex_to_name, "#ffffff", spec=unsupported_spec
            )

    def test_hex_to_rgb(self):
        """
        Test conversion from hex to integer RGB triplet.

        """
        test_pairs = (
            ("#fff", (255, 255, 255)),
            ("#ffffff", (255, 255, 255)),
            ("#000080", (0, 0, 128)),
        )

        for hex_value, triplet in test_pairs:
            result = webcolors.hex_to_rgb(hex_value)
            assert isinstance(result, webcolors.IntegerRGB)
            assert triplet == result

    def test_hex_to_rgb_percent(self):
        """
        Test conversion from hex to percent RGB triplet.

        """
        test_pairs = (
            ("#fff", ("100%", "100%", "100%")),
            ("#ffffff", ("100%", "100%", "100%")),
            ("#000080", ("0%", "0%", "50%")),
        )

        for hex_value, triplet in test_pairs:
            result = webcolors.hex_to_rgb_percent(hex_value)
            assert isinstance(result, webcolors.PercentRGB)
            assert triplet == result


class IntegerRGBConversionTests(unittest.TestCase):
    """
    Test the functions which convert from integer RGB triplets to
    other formats.

    """

    def test_rgb_to_name(self):
        """
        Test conversion from integer RGB triplet to color name.

        """
        test_pairs = (
            ((255, 255, 255), "white"),
            ((0, 0, 128), "navy"),
            ((218, 165, 32), "goldenrod"),
            (webcolors.IntegerRGB(218, 165, 32), "goldenrod"),
        )

        for triplet, name in test_pairs:
            assert name == webcolors.rgb_to_name(triplet)

    def test_rgb_to_name_unnamed(self):
        """
        An integer RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(ValueError, webcolors.rgb_to_name, (18, 52, 86))

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError, webcolors.rgb_to_name, (218, 165, 32), spec=webcolors.HTML4
        )

    def test_rgb_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.

        """
        for supported_spec in webcolors.SUPPORTED_SPECIFICATIONS:
            result = webcolors.rgb_to_name((255, 255, 255), spec=supported_spec)
            assert "white" == result

        for unsupported_spec in ("css1", "css4", "html5"):
            self.assertRaises(
                ValueError,
                webcolors.rgb_to_name,
                (255, 255, 255),
                spec=unsupported_spec,
            )

    def test_rgb_to_hex(self):
        """
        Test conversion from integer RGB triplet to hex.

        """
        test_pairs = (
            ((255, 255, 255), "#ffffff"),
            ((0, 0, 128), "#000080"),
            ((218, 165, 32), "#daa520"),
        )

        for triplet, hex_value in test_pairs:
            assert hex_value == webcolors.rgb_to_hex(triplet)

    def test_rgb_to_rgb_percent(self):
        """
        Test conversion from integer RGB triplet to percent RGB
        triplet.

        """
        test_pairs = (
            ((255, 255, 255), ("100%", "100%", "100%")),
            ((0, 0, 128), ("0%", "0%", "50%")),
            ((218, 165, 32), ("85.49%", "64.71%", "12.5%")),
        )

        for triplet, percent_triplet in test_pairs:
            result = webcolors.rgb_to_rgb_percent(triplet)
            assert isinstance(result, webcolors.PercentRGB)
            assert percent_triplet == result


class NameConversionTests(unittest.TestCase):
    """
    Test the functions which convert from color names to other
    formats.

    """

    def test_name_to_hex(self):
        """
        Test correct conversion of color names to hex.
        """
        test_pairs = (
            ("white", "#ffffff"),
            ("navy", "#000080"),
            ("goldenrod", "#daa520"),
        )

        for name, hex_value in test_pairs:
            assert hex_value == webcolors.name_to_hex(name)

    def test_name_to_hex_bad_name(self):
        """
        A name which does not correspond to a color, or does not
        correspond to a color in the given specification, raises
        ValueError.

        """
        test_values = (
            {"name": "goldenrod", "spec": "html4"},
            {"name": "glue", "spec": "css21"},
            {"name": "breen", "spec": "css3"},
        )

        for kwarg_dict in test_values:
            self.assertRaises(ValueError, webcolors.name_to_hex, **kwarg_dict)

    def test_name_to_hex_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.

        """
        for supported_spec in webcolors.SUPPORTED_SPECIFICATIONS:
            result = webcolors.name_to_hex("white", spec=supported_spec)
            assert "#ffffff" == result

        for unsupported_spec in ("css1", "css4", "html5"):
            self.assertRaises(
                ValueError, webcolors.name_to_hex, "white", spec=unsupported_spec
            )

    def test_name_to_rgb(self):
        """
        Test conversion from color name to integer RGB triplet.

        """
        test_pairs = (
            ("white", (255, 255, 255)),
            ("navy", (0, 0, 128)),
            ("goldenrod", (218, 165, 32)),
        )

        for name, triplet in test_pairs:
            result = webcolors.name_to_rgb(name)
            assert isinstance(result, webcolors.IntegerRGB)
            assert triplet == result

    def test_name_to_rgb_percent(self):
        """
        Test conversion from color name to percent RGB triplet.

        """
        test_pairs = (
            ("white", ("100%", "100%", "100%")),
            ("navy", ("0%", "0%", "50%")),
            ("goldenrod", ("85.49%", "64.71%", "12.5%")),
        )

        for name, triplet in test_pairs:
            result = webcolors.name_to_rgb_percent(name)
            assert isinstance(result, webcolors.PercentRGB)
            assert triplet == result


class PercentRGBConversionTests(unittest.TestCase):
    """
    Test the functions which convert from percent RGB triplets to
    other formats.

    """

    def test_rgb_percent_to_name(self):
        """
        Test conversion from percent RGB triplet to color name.
        """
        test_pairs = (
            (("100%", "100%", "100%"), "white"),
            (("0%", "0%", "50%"), "navy"),
            (("85.49%", "64.71%", "12.5%"), "goldenrod"),
            (webcolors.PercentRGB("85.49%", "64.71%", "12.5%"), "goldenrod"),
        )

        for triplet, name in test_pairs:
            assert name == webcolors.rgb_percent_to_name(triplet)

    def test_rgb_percent_to_name_unnamed(self):
        """
        A percent RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError, webcolors.rgb_percent_to_name, ("7.06%", "20.39%", "33.73%")
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.rgb_percent_to_name,
            ("85.49%", "64.71%", "12.5%"),
            spec=webcolors.HTML4,
        )

    def test_rgb_percent_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.

        """
        for supported_spec in ("html4", "css2", "css21", "css3"):
            result = webcolors.rgb_percent_to_name(
                ("100%", "100%", "100%"), spec=supported_spec
            )
            assert "white" == result

        for unsupported_spec in ("css1", "css4", "html5"):
            self.assertRaises(
                ValueError,
                webcolors.rgb_percent_to_name,
                ("100%", "100%", "100%"),
                spec=unsupported_spec,
            )

    def test_rgb_percent_to_hex(self):
        """
        Test conversion from percent RGB triplet to hex.

        """
        test_pairs = (
            (("100%", "100%", "0%"), "#ffff00"),
            (("0%", "0%", "50%"), "#000080"),
            (("85.49%", "64.71%", "12.5%"), "#daa520"),
        )

        for triplet, hex_value in test_pairs:
            assert hex_value == webcolors.rgb_percent_to_hex(triplet)

    def test_rgb_percent_to_rgb(self):
        """
        Test conversion from percent RGB triplet to integer RGB
        triplet.

        """
        test_pairs = (
            (("100%", "100%", "0%"), (255, 255, 0)),
            (("0%", "0%", "50%"), (0, 0, 128)),
            (("85.49%", "64.71%", "12.5%"), (218, 165, 32)),
        )

        for triplet, int_triplet in test_pairs:
            result = webcolors.rgb_percent_to_rgb(triplet)
            assert isinstance(result, webcolors.IntegerRGB)
            assert int_triplet == result


class ConversionTests(unittest.TestCase):
    """
    Test other aspects of convevrsion not covered by format-specific
    test cases.

    """

    def test_spelling_variants(self):
        """
        When asked to name a color value that maps to either of 'gray' or
        'grey' in CSS3, or a related color like 'darkgray'/'darkgrey',
        webcolors always picks 'gray' as the spelling.

        """
        test_values = (
            ("#a9a9a9", (169, 169, 169), ("66.27%", "66.27%", "66.27%"), "darkgray",),
            ("#2f4f4f", (47, 79, 79), ("18.43%", "30.98%", "30.98%"), "darkslategray",),
            ("#696969", (105, 105, 105), ("41.18%", "41.18%", "41.18%"), "dimgray",),
            ("#808080", (128, 128, 128), ("50%", "50%", "50%"), "gray"),
            ("#d3d3d3", (211, 211, 211), ("82.75%", "82.75%", "82.75%"), "lightgray",),
            ("#d3d3d3", (211, 211, 211), ("82.75%", "82.75%", "82.75%"), "lightgray",),
            (
                "#778899",
                (119, 136, 153),
                ("46.67%", "53.33%", "60.00%"),
                "lightslategray",
            ),
            ("#708090", (112, 128, 144), ("43.92%", "50%", "56.47%"), "slategray"),
        )
        for hex_value, int_tuple, percent_tuple, name in test_values:
            for converter, value in (
                (webcolors.hex_to_name, hex_value),
                (webcolors.rgb_to_name, int_tuple),
                (webcolors.rgb_percent_to_name, percent_tuple),
            ):
                assert name == converter(value, spec=webcolors.CSS3)
