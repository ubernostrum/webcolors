import unittest

import webcolors


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
            ((u'100%', u'100%', u'100%'), u'white'),
            ((u'0%', u'0%', u'50%'), u'navy'),
            ((u'85.49%', u'64.71%', u'12.5%'), u'goldenrod'),
            (webcolors.PercentRGB(u'85.49%', u'64.71%', u'12.5%'),
             u'goldenrod')
        )

        for triplet, name in test_pairs:
            self.assertEqual(
                name,
                webcolors.rgb_percent_to_name(triplet)
            )

    def test_rgb_percent_to_name_unnamed(self):
        """
        A percent RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.

        """
        # No name in any spec.
        self.assertRaises(
            ValueError,
            webcolors.rgb_percent_to_name,
            (u'7.06%', u'20.39%', u'33.73%')
        )

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(
            ValueError,
            webcolors.rgb_percent_to_name,
            (u'85.49%', u'64.71%', u'12.5%'),
            spec=u'html4'
        )

    def test_rgb_percent_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'white',
                webcolors.rgb_percent_to_name(
                    (u'100%', u'100%', u'100%'),
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.rgb_percent_to_name,
                (u'100%', u'100%', u'100%'),
                spec=unsupported_spec
            )

    def test_rgb_percent_to_hex(self):
        """
        Test conversion from percent RGB triplet to hex.

        """
        test_pairs = (
            ((u'100%', u'100%', u'0%'), u'#ffff00'),
            ((u'0%', u'0%', u'50%'), u'#000080'),
            ((u'85.49%', u'64.71%', u'12.5%'), u'#daa520')
        )

        for triplet, hex_value in test_pairs:
            self.assertEqual(
                hex_value,
                webcolors.rgb_percent_to_hex(triplet)
            )

    def test_rgb_percent_to_rgb(self):
        """
        Test conversion from percent RGB triplet to integer RGB
        triplet.

        """
        test_pairs = (
            ((u'100%', u'100%', u'0%'), (255, 255, 0)),
            ((u'0%', u'0%', u'50%'), (0, 0, 128)),
            ((u'85.49%', u'64.71%', u'12.5%'), (218, 165, 32))
        )

        for triplet, int_triplet in test_pairs:
            result = webcolors.rgb_percent_to_rgb(triplet)
            self.assertTrue(
                isinstance(result, webcolors.IntegerRGB)
            )
            self.assertEqual(int_triplet, result)
