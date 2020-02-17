.. _conformance:


Conformance and testing
=======================

Much of the behavior of webcolors is dictated by the relevant web
standards, which define the acceptable color formats, how to determine
valid values for each format and the values corresponding to defined
color names. Maintaining correct conversions and conformance to those
standards is crucial.

The source distribution of webcolors (the `.tar.gz` file you can
download from the Python Package Index) includes a `tests/` directory
containing a normal test suite as well as supplemental test files
which perform more comprehensive verification.


The normal test suite
---------------------

The normal test suite for webcolors aims for 100% coverage of code
paths, but does *not* aim for 100% coverage of possible color value
inputs and outputs. Instead, it uses a small number of test values to
routinely exercise various functions.

The test values used in most test functions are chosen to provide,
where applicable, at least one of each of the following types of
values:

* An endpoint of the acceptable range of values (i.e., `#ffffff`
  and/or `#000000` for hexadecimal).

* A value beyond the high end of the acceptable range (i.e., greater
  than 255 in an integer triplet, or greater than 100% for a
  percentage triplet).

* A value beyond the low end of the acceptable range (i.e., less than
  0 in an integer triplet, or less than 0% for a percentage triplet).

* A "negative zero" value (-0 in an integer triplet, or -0% in
  a percentage triplet).

* An arbitrary value not from an endpoint of the acceptable range
  (usually `#000080`, chosen because the author likes navy blue).

* A value which corresponds to a named color in CSS3/SVG but not in
  earlier standards (usually `#daa520`, which is `goldenrod` in
  CSS3/SVG).

Since this covers the cases most likely to produce problems, this test
suite provides good basic confidence in the correctness of the tested
functions. It runs on every commit to the repository, and on every
release tag. You can see the results of test runs online `at Travis CI
<https://travis-ci.org/ubernostrum/webcolors/>`_.

However, the normal test suite cannot guarantee that the color
definitions included in webcolors correspond to those in the
relevant standards, and cannot provide guarantees of correct
conversions for all possible values. For that, additional tests are
required.


.. _full-verification:

Full verification tests
-----------------------

These tests are contained in two files which are not executed during
normal test runs: `tests/definitions.py` and
`tests/full_colors.py`. They are not run as part of the normal test
suite, but are run prior to each release of webcolors.


Verifying color definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `definitions.py` test file verifies that the color definitions in
webcolors are correct. It does this by downloading the relevant
standards documents as HTML, parsing out the color definitions in
them, and comparing them to the definitions in webcolors. That
consists of:

* Parsing out the names and hexadecimal values of the 16 named colors
  in the HTML 4 standard, and checking that the names and values in
  :data:`~webcolors.HTML4_NAMES_TO_HEX` match.

* Parsing out the names and hexadecimal values of the 17 named colors
  in the CSS2.1 standard, and checking that the names and values in
  :data:`~webcolors.CSS21_NAMES_TO_HEX` match.

* Parsing out the names and hexadecimal and integer values of the 147
  named colors in the CSS3 color module (although the color set is
  taken from SVG, CSS3 provides both hexadecimal and integer values
  for them, while the SVG standard provides only integer values), and
  checking that the names and values in
  :data:`~webcolors.CSS3_NAMES_TO_HEX` match, and that
  :func:`~webcolors.name_to_rgb` returns the correct integer values.


Fully verifying correctness of conversions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `full_colors.py` test file exercises
:func:`~webcolors.hex_to_rgb`, :func:`~webcolors.rgb_to_hex`,
:func:`~webcolors.rgb_to_rgb_percent` and
:func:`~webcolors.rgb_percent_to_rgb` as fully as is practical.

For conversions between hexadecimal and integer `rgb()`, it generates
all 16,777,216 possible color values for each format in order
(starting at `#000000` and `(0, 0, 0)` and incrementing), and verifies
that each one converts to the corresponding value in the other
format. Thus, it is possible to be confident that webcolors provides
correct conversions between all possible color values in those
formats.

Testing the correctness of conversion to and from percentage
`rgb()`, however, is more difficult, and a full test is not
provided, for two reasons:

1. Because percentage `rgb()` values can make use of floating-point
   values, and because standard floating-point types in most common
   programming languages (Python included) are inherently imprecise,
   exact verification is not possible.

2. The only rigorous definition of the format of a percentage value is
   in CSS2, `which declares a percentage to be
   <http://www.w3.org/TR/CSS2/syndata.html#percentage-units>`_ "a
   `<number>` immediately followed by '%'". `The CSS2 definition of a
   number <http://www.w3.org/TR/CSS2/syndata.html#value-def-number>`_
   places no limit on the length past the decimal point, and appears
   to be declaring any real number as a valid value, though percentage
   triplets clip their inputs to the range 0.0-100.0. As the subset of
   reals in the range 0.0 to 100.0 is uncountably infinite, testing
   all legal values is not possible on current hardware in any
   reasonable amount of time.

Since precise correctness and completeness are not achievable,
webcolors instead aims to achieve *consistency* in
conversions. Specifically, the `full_colors.py` test generates all
16,777,216 integer `rgb()` triplets, and for each such triplet `t`
verifies that the following assertion holds:

.. code-block:: python

   t == rgb_percent_to_rgb(rgb_to_rgb_percent(t))


Running the tests
-----------------

The standard test runner for webcolors is `tox
<https://tox.readthedocs.io/>`_, which supports testing against
multiple Python versions and executing a variety of different test
tasks. The source distribution of webcolors includes its `tox.ini`
file. To run the tests, install tox (`pip install tox`), then download
and unpack `a source distribution of webcolors from the Python Package
Index <https://pypi.org/project/webcolors/>`_. 

To run the normal test suite against the complete set of supported
Python versions:

.. code-block:: shell

   $ tox

This requires that you have each supported version of Python (for
webcolors |release|, this is 2.7, 3.5, 3.6, and 3.7) available. To
test only against a specific version of Python, use the `-e` flag and
pass the version to test. For example, to test on Python 3.7:

.. code-block:: shell

   $ tox -e py37

To run the full verification tests for definition correctness and
conversions, specify the "release" test environment instead (so named
because these tests are usually run only prior to a new release of
webcolors):

.. code-block:: shell

   $ tox -e release

Note that this requires an internet connection, and is
CPU-intensive.