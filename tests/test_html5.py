import unittest

import webcolors


class HTML5Tests(unittest.TestCase):
    """
    Test functions which implement the HTML5 color algorithms.
    """
    def test_parse_simple_color(self):
        """
        Test implementation of the HTML5 simple color parsing
        algorithm.
        """
        test_pairs = (('#ffffff', (255, 255, 255)),
                      ('#000080', (0, 0, 128)),
                      ('#daa520', (218, 165, 32)))
        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.html5_parse_simple_color(pair[0]))

    def test_parse_simple_color_error(self):
        """
        Test error conditions of the HTML5 simple color parsing
        algorithm.
        """
        test_values = ('0099cc',
                       '#09c',
                       '#0000',
                       '#0000000',
                       '#0000gg')
        for value in test_values:
            self.assertRaises(ValueError,
                              webcolors.html5_parse_simple_color,
                              value)

    def test_serialize_simple_color(self):
        """
        Test implementation of the HTML5 simple color serialization
        algorithm.
        """
        test_pairs = (((0, 0, 0), '#000000'),
                      ((0, 0, 128), '#000080'),
                      ((218, 165, 32), '#daa520'))
        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.html5_serialize_simple_color(pair[0]))

    def test_parse_legacy_color(self):
        """
        Test implementation of the HTML5 legacy color serialization
        algorithm.
        """
        test_pairs = ((u'chucknorris', (192, 0, 0)),
                      (u'Window', (0, 13, 0)),
                      (u'Z3STGWF1CF', (3, 0, 207)),
                      (u'hZXpGxDtxE', (0, 13, 224)))
        for pair in test_pairs:
            self.assertEqual(pair[1],
                             webcolors.html5_parse_legacy_color(pair[0]))
