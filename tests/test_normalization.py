import unittest

import webcolors


class NormalizationTests(unittest.TestCase):
    """
    Test both the publicly-exposed and internal normalization
    functions.

    """
    def test_normalize_hex(self):
        """
        Hexadecimal normalization normalizes valid hex color codes to
        6 digits, lowercase.

        """
        test_pairs = (
            (u'#0099cc', u'#0099cc'),
            (u'#0099CC', u'#0099cc'),
            (u'#09c', u'#0099cc'),
            (u'#09C', u'#0099cc')
        )

        for raw, normalized in test_pairs:
            assert normalized == webcolors.normalize_hex(raw)

    def test_normalize_hex_format(self):
        """
        Hex normalization raises ValueError on invalid hex color code.

        """
        test_values = (
            u'0099cc',
            '#0000gg',
            '#0000',
            '#00000000'
        )
        for value in test_values:
            self.assertRaises(
                ValueError,
                webcolors.normalize_hex,
                value
            )

    def test_normalize_integer_rgb(self):
        """
        Integer normalization clips to 0-255.

        """
        test_pairs = (
            (255, 255),
            (0, 0),
            (128, 128),
            (-20, 0),
            (270, 255),
            (-0, 0)
        )

        for raw, normalized in test_pairs:
            assert normalized == webcolors._normalize_integer_rgb(raw)

    def test_normalize_integer_triplet(self):
        """
        Integer triplet normalization clips all values to 0-255.

        """
        test_pairs = (
            ((128, 128, 128), (128, 128, 128)),
            ((0, 0, 0), (0, 0, 0)),
            ((255, 255, 255), (255, 255, 255)),
            ((270, -20, 128), (255, 0, 128)),
            ((-0, -0, -0), (0, 0, 0))
        )

        for triplet, normalized in test_pairs:
            result = webcolors.normalize_integer_triplet(triplet)
            assert isinstance(result, webcolors.IntegerRGB)
            assert normalized == result

    def test_normalize_percent_rgb(self):
        """
        Percent normalization clips to 0%-100%.

        """
        test_pairs = (
            (u'0%', u'0%'),
            (u'100%', u'100%'),
            (u'62%', u'62%'),
            (u'-5%', u'0%'),
            (u'250%', u'100%'),
            (u'85.49%', u'85.49%'),
            (u'-0%', u'0%')
        )

        for raw, normalized in test_pairs:
            assert normalized == webcolors._normalize_percent_rgb(raw)

    def test_normalize_percent_triplet(self):
        """
        Percent triplet normalization clips all values to 0%-100%.

        """
        test_pairs = (
            ((u'50%', u'50%', u'50%'), (u'50%', u'50%', u'50%')),
            ((u'0%', u'100%', u'0%'), (u'0%', u'100%', u'0%')),
            ((u'-10%', u'250%', u'500%'), (u'0%', u'100%', u'100%')),
            ((u'-0%', u'-0%', u'-0%'), (u'0%', u'0%', u'0%'))
        )

        for triplet, normalized in test_pairs:
            result = webcolors.normalize_percent_triplet(triplet)
            assert isinstance(result, webcolors.PercentRGB)
            assert normalized == result
