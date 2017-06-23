import unittest

import webcolors


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
            ((255, 255, 255), u'white'),
            ((0, 0, 128), u'navy'),
            ((218, 165, 32), u'goldenrod'),
            (webcolors.IntegerRGB(218, 165, 32), u'goldenrod')
        )

        for triplet, name in test_pairs:
            self.assertEqual(name,
                             webcolors.rgb_to_name(triplet))

    def test_rgb_to_name_unnamed(self):
        """
        An integer RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError,
            webcolors.rgb_to_name,
            (18, 52, 86)
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.rgb_to_name,
            (218, 165, 32),
            spec=u'html4'
        )

    def test_rgb_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'white',
                webcolors.rgb_to_name(
                    (255, 255, 255),
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.rgb_to_name,
                (255, 255, 255),
                spec=unsupported_spec
            )

    def test_rgb_to_hex(self):
        """
        Test conversion from integer RGB triplet to hex.

        """
        test_pairs = (
            ((255, 255, 255), u'#ffffff'),
            ((0, 0, 128), u'#000080'),
            ((218, 165, 32), u'#daa520')
        )

        for triplet, hex_value in test_pairs:
            self.assertEqual(
                hex_value,
                webcolors.rgb_to_hex(triplet)
            )

    def test_rgb_to_rgb_percent(self):
        """
        Test conversion from integer RGB triplet to percent RGB
        triplet.

        """
        test_pairs = (
            ((255, 255, 255), (u'100%', u'100%', u'100%')),
            ((0, 0, 128), (u'0%', u'0%', u'50%')),
            ((218, 165, 32), (u'85.49%', u'64.71%', u'12.5%'))
        )

        for triplet, percent_triplet in test_pairs:
            result = webcolors.rgb_to_rgb_percent(triplet)
            self.assertTrue(
                isinstance(result, webcolors.PercentRGB)
            )
            self.assertEqual(percent_triplet, result)
