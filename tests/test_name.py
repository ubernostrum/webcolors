import unittest

import webcolors


class NameConversionTests(unittest.TestCase):
    """
    Test functions which convert from color names to other formats.
    """
    def test_name_to_hex(self):
        """
        Test correct conversion of color names to hex.
        """
        test_pairs = (('white', '#ffffff'),
                      ('navy', '#000080'),
                      ('goldenrod', '#daa520'))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.name_to_hex(pair[0]))

    def test_name_to_hex_bad_name(self):
        """
        A name which does not correspond to a color, or does not
        correspond to a color in the given specification, raises
        ValueError.
        """
        test_values = (('goldenrod', 'html4'),
                       ('glue', 'css21'),
                       ('breen', 'css3'))

        for value in test_values:
            self.assertRaises(ValueError,
                              webcolors.name_to_hex,
                              *value)

    def test_name_to_hex_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.
        """
        for supported_spec in ('html4', 'css2', 'css21', 'css3'):
            self.assertEqual('#ffffff',
                             webcolors.name_to_hex('white',
                                                   spec=supported_spec))

        for unsupported_spec in ('css1', 'css4', 'html5'):
            self.assertRaises(ValueError,
                              webcolors.name_to_hex,
                              'white', spec=unsupported_spec)

    def test_name_to_rgb(self):
        """
        Test conversion from color name to integer RGB triplet.
        """
        test_pairs = (('white', (255, 255, 255)),
                      ('navy', (0, 0, 128)),
                      ('goldenrod', (218, 165, 32)))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.name_to_rgb(pair[0]))

    def test_name_to_rgb_percent(self):
        """
        Test conversion from color name to percent RGB triplet.
        """
        test_pairs = (('white', ('100%', '100%', '100%')),
                      ('navy', ('0%', '0%', '50%')),
                      ('goldenrod', ('85.49%', '64.71%', '12.5%')))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.name_to_rgb_percent(pair[0]))
