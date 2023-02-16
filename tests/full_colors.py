"""
Test case which exercises webcolors' conversion functions across all
16,777,216 possible hexadecimal values and all 16,777,216 possible
integer rgb() triplet values.

You should not ever need to run this test; it is not part of the
normal unit-test suite, and is used only as a final check when
preparing a new release of webcolors.

Because it generates each of the nearly 17 million color values
multiple times, this test case takes some time to run and consumes
most or all available CPU while running. As a consolation, it is
somewhat efficient with respect to memory.

Due to the inherent imprecision of floating-point percentage values,
and the fact that the legal (with respect to the CSS standards) set of
percentage rgb() triplets is uncountably infinite, percentage rgb()
triplets are not exhaustively tested here, and the normal test suite
is used to ensure correctness of the conversion functions for those
values.

The only test performed here for percentage rgb() triplets is to
ensure that converting an integer rgb() triplet to percentage and back
returns the original integer values, for consistency.

"""

import sys
from pathlib import Path
import unittest

thisDir = Path(__file__).parent.absolute()
sys.path.insert(0, str(thisDir.parent))

import webcolors


def hex_colors():
    """
    Generator which yields all 2**24 hexadecimal color values, in
    order starting from #000000.

    """
    for i in range(16777217):
        yield f"#{i:06x}"


def int_colors():
    """
    Generator which yields all 2**24 integer rgb() triplets, in
    order starting from (0,0,0).

    """
    red_counter = tuple(range(256))
    green_counter = tuple(range(256))
    blue_counter = tuple(range(256))
    for red_value in red_counter:
        for green_value in green_counter:
            for blue_value in blue_counter:
                yield (red_value, green_value, blue_value)


class FullColorTest(unittest.TestCase):
    """
    Exercise color conversion on all testable values.

    """

    def test_full_colors(self):
        """
        Test conversion between hexadecimal and integer rgb() for
        all 2**24 possible values.

        """
        for hex_color, int_triplet in zip(hex_colors(), int_colors()):
            assert int_triplet == webcolors.hex_to_rgb(hex_color)
            assert hex_color == webcolors.rgb_to_hex(int_triplet)

    def test_triplet_conversion(self):
        """
        Test conversion between integer and percentage rgb() as
        fully as possible.

        Because exhaustive testing is not possible (the set of valid
        percentgae rgb() triplets is uncountably infinite), this test
        ensures that for each of the 2**24 possible integer triplets,
        conversion to percentage and back gives the starting value.

        """
        for int_triplet in int_colors():
            conversion = webcolors.rgb_percent_to_rgb(
                webcolors.rgb_to_rgb_percent(int_triplet)
            )
            assert int_triplet == conversion


if __name__ == "__main__":
    unittest.main()
