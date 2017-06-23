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
            (u'#ffffff', u'white'),
            (u'#fff', u'white'),
            (u'#000080', u'navy'),
            (u'#daa520', u'goldenrod')
        )

        for hex_value, name in test_pairs:
            self.assertEqual(
                name,
                webcolors.hex_to_name(hex_value)
            )

    def test_hex_to_name_unnamed(self):
        """
        A hex code which does not correspond to a named color, or does
        not correspond to a named color in the given specification,
        raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError,
            webcolors.hex_to_name,
            '#123456'
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.hex_to_name,
            '#daa520',
            spec=u'html4'
        )

    def test_hex_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'white',
                webcolors.hex_to_name(
                    u'#ffffff',
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.hex_to_name,
                '#ffffff',
                spec=unsupported_spec
            )

    def test_hex_to_rgb(self):
        """
        Test conversion from hex to integer RGB triplet.

        """
        test_pairs = (
            (u'#fff', (255, 255, 255)),
            (u'#ffffff', (255, 255, 255)),
            (u'#000080', (0, 0, 128))
        )

        for hex_value, triplet in test_pairs:
            result = webcolors.hex_to_rgb(hex_value)
            self.assertTrue(
                isinstance(result, webcolors.IntegerRGB)
            )
            self.assertEqual(result, triplet)

    def test_hex_to_rgb_percent(self):
        """
        Test conversion from hex to percent RGB triplet.

        """
        test_pairs = (
            (u'#fff', (u'100%', u'100%', u'100%')),
            (u'#ffffff', (u'100%', u'100%', u'100%')),
            (u'#000080', (u'0%', u'0%', u'50%'))
        )

        for hex_value, triplet in test_pairs:
            result = webcolors.hex_to_rgb_percent(hex_value)
            self.assertTrue(
                isinstance(result, webcolors.PercentRGB)
            )
            self.assertEqual(result, triplet)
