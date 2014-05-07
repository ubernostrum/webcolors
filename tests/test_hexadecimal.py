import unittest

import webcolors


class HexConversionTests(unittest.TestCase):
    """
    Test functions which convert from hex color codes to other
    formats.
    
    """
    def test_hex_to_name(self):
        """
        Test conversion from hex to color name.
        
        """
        test_pairs = (('#ffffff', 'white'),
                      ('#fff', 'white'),
                      ('#000080', 'navy'),
                      ('#daa520', 'goldenrod'))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.hex_to_name(pair[0]))

    def test_hex_to_name_unnamed(self):
        """
        A hex code which does not correspond to a named color, or does
        not correspond to a named color in the given specification,
        raises ValueError.
        
        """
        # No name in any spec.
        self.assertRaises(ValueError,
                          webcolors.hex_to_name,
                          '#123456')

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(ValueError,
                          webcolors.hex_to_name,
                          '#daa520', spec='html4')

    def test_hex_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; using an
        unsupported specification raises ValueError.
        
        """
        for supported_spec in ('html4', 'css2', 'css21', 'css3'):
            self.assertEqual('white',
                             webcolors.hex_to_name('#ffffff', spec=supported_spec))

        for unsupported_spec in ('css1', 'css4', 'html5'):
            self.assertRaises(ValueError,
                              webcolors.hex_to_name,
                              '#ffffff', spec=unsupported_spec)

    def test_hex_to_rgb(self):
        """
        Test conversion from hex to integer RGB triplet.
        
        """
        test_pairs = (('#fff', (255, 255, 255)),
                      ('#ffffff', (255, 255, 255)),
                      ('#000080', (0, 0, 128)))

        for pair in test_pairs:
                      self.assertEqual(pair[1],
                                       webcolors.hex_to_rgb(pair[0]))

    def test_hex_to_rgb_percent(self):
        """
        Test conversion from hex to percent RGB triplet.
        
        """
        test_pairs = (('#fff', ('100%', '100%', '100%')),
                      ('#ffffff', ('100%', '100%', '100%')),
                      ('#000080', ('0%', '0%', '50%')))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.hex_to_rgb_percent(pair[0]))
