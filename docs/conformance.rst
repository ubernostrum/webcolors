.. _conformance:


Conformance and testing
=======================

Much of the behavior of webcolors is dictated by the relevant Web
standards, which define the acceptable color formats, how to determine
valid values for each format and the values corresponding to defined
color names. Maintaining correct conversions and conformance to those
standards is crucial.


The normal test suite
---------------------

The normal test suite for webcolors -- that is, the set of unit
tests which will execute using standard Python test runners -- aims
for 100% code coverage, but does *not* aim for 100% coverage of
possible color value inputs and outputs. Instead, it uses a small
number of test values to routinely exercise various functions.

The test values used in most test functions are chosen to provide,
where applicable, at least one of each of the following types of
values:

* An endpoint of the acceptable range of values (i.e., ``#ffffff``
  and/or ``#000000`` for hexadecimal).

* A value beyond the high end of the acceptable range (i.e., greater
  than 255 in an integer triplet, or greater than 100% for a
  percentage triplet).

* A value beyond the low end of the acceptable range (i.e., less than
  0 in an integer triplet, or less than 0% for a percentage triplet).

* A "negative zero" value (-0 in an integer triplet, or -0% in
  a percentage triplet).

* An arbitrary value not from an endpoint of the acceptable range
  (usually ``#000080``, chosen because the author likes navy blue).

* A value which corresponds to a named color in CSS 3/SVG but not in
  earlier standards (usually ``#daa520``, which is ``goldenrod`` in
  CSS 3/SVG).

Since this covers the cases most likely to produce problems, it
provides good basic confidence in the correctness of the tested
functions.

However, the normal test suite cannot guarantee that the color
definitions included in webcolors correspond to those in the
relevant standards, and cannot provide guarantees of correct
conversions for all possible values. For that, additional tests are
required.

Those tests are contained in two files in the source distribution,
which are not executed during normal test runs:
``tests/definitions.py`` and ``tests/full_colors.py``.


Verifying color definitions
---------------------------

The ``definitions`` test file verifies that the color definitions in
webcolors are correct. It does this by retrieving the relevant
standards documents as HTML, parsing out the color definitions in
them, and comparing them to the definitions in webcolors. That
consists of:

* Parsing out the names and hexadecimal values of the 16 named colors
  in the HTML 4 standard, and checking that the names and values in
  :data:`~webcolors.HTML4_NAMES_TO_HEX` match.

* Parsing out the names and hexadecimal values of the 17 named colors
  in the CSS 2.1 standard, and checking that the names and values in
  :data:`~webcolors.CSS21_NAMES_TO_HEX` match.

* Parsing out the names and hexadecimal and integer values of the 147
  named colors in the CSS 3 color module (although the color set is
  taken from SVG, CSS 3 provides both hexadecimal and integer values
  for them, while the SVG standard provides only integer values), and
  checking that the names and values in
  :data:`~webcolors.CSS3_NAMES_TO_HEX` match, and that
  :func:`~webcolors.name_to_rgb` returns the correct integer values.

The ``definitions`` file can be run standalone (i.e., ``python
tests/definitions.py``) to execute these tests, but it does require an
internet connection (to retrieve the standards documents) and requires
a few libraries for retrieving and parsing the standards
documents. The file ``test_requirements.txt`` in `the webcolors source
repository <https://github.com/ubernostrum/webcolors/>`_ will install
all libraries necessary for executing this test file.


Fully verifying correctness of conversions
------------------------------------------

The ``full_colors`` test file exercises :func:`~webcolors.hex_to_rgb`,
:func:`~webcolors.rgb_to_hex`, :func:`~webcolors.rgb_to_rgb_percent`
and :func:`~webcolors.rgb_percent_to_rgb` as fully as is practical.

For conversions between hexadecimal and integer ``rgb()``, that file
generates all 16,777,216 possible color values for each format in
order (starting at ``#000000`` and ``(0, 0, 0)`` and incrementing),
and verifies that each one converts to the corresponding value in the
other format. Thus, it is possible to be confident that webcolors
provides correct conversions between all possible color values in
those formats.

Testing the correctness of conversion to and from percentage
``rgb()``, however, is more difficult, and a full test is not
provided, for two reasons:

1. Because percentage ``rgb()`` values can make use of floating-point
   values, and because standard floating-point types in most common
   programming languages (Python included) are inherently imprecise,
   exact verification is not possible.

2. The only rigorous definition of the format of a percentage value is
   in CSS 2, `which declares a percentage to be
   <http://www.w3.org/TR/CSS2/syndata.html#percentage-units>`_ "a
   ``<number>`` immediately followed by '%'". `The CSS 2 definition of
   a number
   <http://www.w3.org/TR/CSS2/syndata.html#value-def-number>`_ places
   no limit on the length past the decimal point, and appears to be
   declaring any real number as a valid value. As the subset of reals
   in the range 0.0 to 100.0 is uncountably infinite, testing all
   legal values is not possible on current hardware in any reasonable
   amount of time.

Since precise correctness and completeness are not achievable,
webcolors instead aims to achieve *consistency* in
conversions. Specifically, the ``full_colors`` test generates all
16,777,216 integer ``rgb()`` triplets, and for each such triplet ``t``
verifies that the following assertion holds::

    t == rgb_percent_to_rgb(rgb_to_rgb_percent(t))

The ``full_colors`` test has no external dependencies other than
Python, and does not require an internet connection. It is written to
be run standalone (``python tests/full_colors.py``). However, due to
the fact that it must generate all 16,777,216 color values multiple
times, and perform checks on each one, it does take some time to run
even on fast hardware.
