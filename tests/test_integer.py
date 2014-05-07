import unittest

import webcolors


class IntegerRGBConversionTests(unittest.TestCase):
    """
    Test functions which convert from integer RGB triplets to other
    formats.
    
    """
    def test_rgb_to_name(self):
        """
        Test conversion from integer RGB triplet to color name.
        
        """
        test_pairs = (((255, 255, 255), 'white'),
                      ((0, 0, 128), 'navy'),
                      ((218, 165, 32), 'goldenrod'))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.rgb_to_name(pair[0]))

    
    def test_rgb_to_name_unnamed(self):
        """
        An integer RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.
        
        """
        # No name in any spec.
        self.assertRaises(ValueError,
                          webcolors.rgb_to_name,
                          (18, 52, 86))

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(ValueError,
                          webcolors.rgb_to_name,
                          (218, 165, 32), spec='html4')

    def test_rgb_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.
        
        """
        for supported_spec in ('html4', 'css2', 'css21', 'css3'):
            self.assertEqual('white',
                             webcolors.rgb_to_name((255, 255, 255),
                                                   spec=supported_spec))

        for unsupported_spec in ('css1', 'css4', 'html5'):
            self.assertRaises(ValueError,
                              webcolors.rgb_to_name,
                              (255, 255, 255), spec=unsupported_spec)

    def test_rgb_to_hex(self):
        """
        Test conversion from integer RGB triplet to hex.
        
        """
        test_pairs = (((255, 255, 255), '#ffffff'),
                      ((0, 0, 128), '#000080'),
                      ((218, 165, 32), '#daa520'))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.rgb_to_hex(pair[0]))

    def test_rgb_to_rgb_percent(self):
        """
        Test conversion from integer RGB triplet to percent RGB
        triplet.
        
        """
        test_pairs = (((255, 255, 255), ('100%', '100%', '100%')),
                      ((0, 0, 128), ('0%', '0%', '50%')),
                      ((218, 165, 32), ('85.49%', '64.71%', '12.5%')))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.rgb_to_rgb_percent(pair[0]))
