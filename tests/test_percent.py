import unittest

import webcolors


class PercentRGBConversionTests(unittest.TestCase):
    """
    Test functions which convert from percent RGB triplets to other
    formats.
    
    """
    def test_rgb_percent_to_name(self):
        """
        Test conversion from percent RGB triplet to color name.

        """
        test_pairs = ((('100%', '100%', '100%'), 'white'),
                      (('0%', '0%', '50%'), 'navy'),
                      (('85.49%', '64.71%', '12.5%'), 'goldenrod'))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.rgb_percent_to_name(pair[0]))

    def test_rgb_percent_to_name_unnamed(self):
        """
        A percent RGB triplet which does not correspond to a named
        color, or does not correspond to a named color in the given
        specification, raises ValueError.
        
        """
        # No name in any spec.
        self.assertRaises(ValueError,
                          webcolors.rgb_percent_to_name,
                          ('7.06%', '20.39%', '33.73%'))

        # This is 'goldenrod' in CSS 3 list, unnamed in HTML 4.
        self.assertRaises(ValueError,
                          webcolors.rgb_percent_to_name,
                          ('85.49%', '64.71%', '12.5%'), spec='html4')

    def test_rgb_percent_to_name_specs(self):
        """
        Using one of the supported specifications succeeds; an
        unsupported specification raises ValueError.
        
        """
        for supported_spec in ('html4', 'css2', 'css21', 'css3'):
            self.assertEqual('white',
                             webcolors.rgb_percent_to_name(('100%',
                                                            '100%',
                                                            '100%'),
                                                   spec=supported_spec))

        for unsupported_spec in ('css1', 'css4', 'html5'):
            self.assertRaises(ValueError,
                              webcolors.rgb_percent_to_name,
                              ('100%', '100%', '100%'),
                              spec=unsupported_spec)

    def test_rgb_percent_to_hex(self):
        """
        Test conversion from percent RGB triplet to hex.
        
        """
        test_pairs = ((('100%', '100%', '0%'), '#ffff00'),
                      (('0%', '0%', '50%'), '#000080'),
                      (('85.49%', '64.71%', '12.5%'), '#daa520'))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.rgb_percent_to_hex(pair[0]))

    def test_rgb_percent_to_rgb(self):
        """
        Test conversion from percent RGB triplet to integer RGB
        triplet.
        
        """
        test_pairs = ((('100%', '100%', '0%'), (255, 255, 0)),
                      (('0%', '0%', '50%'), (0, 0, 128)),
                      (('85.49%', '64.71%', '12.5%'), (218, 165, 32)))

        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.rgb_percent_to_rgb(pair[0]))
