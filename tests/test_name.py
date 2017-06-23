import unittest

import webcolors


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
            (u'white', u'#ffffff'),
            (u'navy', u'#000080'),
            (u'goldenrod', u'#daa520')
        )

        for name, hex_value in test_pairs:
            self.assertEqual(
                hex_value,
                webcolors.name_to_hex(name)
            )

    def test_name_to_hex_bad_name(self):
        """
        A name which does not correspond to a color, or does not
        correspond to a color in the given specification, raises
        ValueError.

        """
        test_values = (
            {u'name': u'goldenrod',
             u'spec': u'html4'},
            {u'name': u'glue',
             u'spec': u'css21'},
            {u'name': u'breen',
             u'spec': u'css3'},
        )

        for kwarg_dict in test_values:
            self.assertRaises(
                ValueError,
                webcolors.name_to_hex,
                **kwarg_dict
            )

    def test_name_to_hex_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.

        """
        for supported_spec in (u'html4', u'css2', u'css21', u'css3'):
            self.assertEqual(
                u'#ffffff',
                webcolors.name_to_hex(
                    u'white',
                    spec=supported_spec
                )
            )

        for unsupported_spec in (u'css1', u'css4', u'html5'):
            self.assertRaises(
                ValueError,
                webcolors.name_to_hex,
                'white', spec=unsupported_spec
            )

    def test_name_to_rgb(self):
        """
        Test conversion from color name to integer RGB triplet.

        """
        test_pairs = (
            (u'white', (255, 255, 255)),
            (u'navy', (0, 0, 128)),
            (u'goldenrod', (218, 165, 32))
        )

        for name, triplet in test_pairs:
            result = webcolors.name_to_rgb(name)
            self.assertTrue(
                isinstance(
                    result,
                    webcolors.IntegerRGB
                )
            )
            self.assertEqual(triplet, result)

    def test_name_to_rgb_percent(self):
        """
        Test conversion from color name to percent RGB triplet.

        """
        test_pairs = (
            (u'white', (u'100%', u'100%', u'100%')),
            (u'navy', (u'0%', u'0%', u'50%')),
            (u'goldenrod', (u'85.49%', u'64.71%', u'12.5%'))
        )

        for name, triplet in test_pairs:
            result = webcolors.name_to_rgb_percent(name)
            self.assertTrue(
                isinstance(result, webcolors.PercentRGB)
            )
            self.assertEqual(triplet, result)
