.. _conventions:


Normalization and conventions
=============================

Since the various formats used to specify colors in Web documents do
not always map cleanly to Python data types, and some variation is
permitted in how to use each format in a Web document, webcolors
applies a set of conventions for representing color names and values,
and for normalizing them.


.. _string-types:

Python string types
-------------------

The webcolors module is written to be compatible with both Python
2 and Python 3, which have different approaches to strings:

* On Python 2, a sequence of bytes in a particular encoding (a "byte
  string") is represented by the type ``str`` , and Unicode strings
  are represented by the type ``unicode``. Mixing of ``str`` and
  ``unicode`` is possible in Python 2, but not recommended as it is a
  frequent source of bugs.

* On Python 3, a sequence of bytes in a particular encoding is
  represented by the type ``bytes``, and Unicode strings are
  represented by the type ``str``. Mixing of ``str`` and ``bytes`` is
  not permitted in Python 3, and will usually raise exceptions.

The approach to string types in webcolors is as follows:

* On Python 3, use of Unicode strings -- ``str`` -- is mandatory for
  all string arguments to functions in webcolors. Use of ``bytes``
  values is forbidden and will result in errors.

* All mappings from color names to hexadecimal values (and vice versa)
  are dictionaries whose keys and values are Unicode strings (``str``
  on Python 3 and ``unicode`` on Python 2). This permits use of byte
  strings on Python 2, but ensures that results will be Unicode
  strings.

* All functions whose return values include strings will use Unicode
  strings (``unicode`` on Python 2 and ``str`` on Python 3).

* All functions whose arguments include string values, *except* for
  the HTML5 color algorithms (see below), will accept a sequence of
  bytes (``str``) on Python 2, but will convert to Unicode strings
  (``unicode``) for output.

Because the HTML5 Recommendation specifies its color algorithms in
terms of Unicode strings only (and in some cases, requires exact
identification of Unicode code points to determine behavior), the
following constraint applies to the functions implementing these
algorithms:

* Any string arguments *must* be Unicode strings (``unicode`` on
  Python 2 or ``str`` on Python 3). Use of ``str`` on Python 2 or
  ``bytes`` on Python 3 will raise a ``ValueError``.

Use of Unicode strings whenever possible is strongly preferred. To
encourage this, all documentation for webcolors uses the ``u``
prefix for string literals. Use of the ``u`` prefix is required on
Python 2 to mark a string literal as Unicode; on Python 3.3 and later,
use of this prefix is permitted but not necessary (as all un-prefixed
string literals on Python 3 are Unicode strings).

Due to use of the ``u`` prefix, using webcolors on Python 3 will
require at least Python 3.3.


Hexadecimal color values
------------------------

For colors specified via hexadecimal values, webcolors will accept
strings in the following formats:

* The character ``#`` followed by three hexadecimal digits, where
  digits A-F may be upper- or lowercase.

* The character ``#`` followed by six hexadecimal digits, where
  digits A-F may be upper- or lowercase (i.e., what HTML5 designates a
  "valid simple color" when all digits are uppercase, and a "valid
  lowercase simple color" when all digits are lowercase).

For output which consists of a color specified via hexadecimal values,
and for functions which perform intermediate conversion to hexadecimal
before returning a result in another format, webcolors always
normalizes such values to a string in the following format:

* The character ``#`` followed by six hexadecimal digits, with digits
  A-F forced to lowercase (what HTML5 designates a "valid lowercase
  simple color").

The function :func:`~webcolors.normalize_hex` can be used to perform
this normalization manually if desired.


Integer and percentage ``rgb()`` triplets
-----------------------------------------

Functions which work with integer ``rgb()`` triplets accept and return
them as a 3-tuple of Python ``int``. Functions which work with
percentage ``rgb()`` triplets accept them as 3-tuple of Python strings
(either ``str`` or ``unicode`` is permitted on Python 2; only ``str``
is permitted on Python 3) and return them as a 3-tuple of Python
Unicode strings (``unicode`` or ``str`` depending on Python version).

Plain tuples are accepted by all functions which deal with integer or
percentage ``rgb()`` triplets, but three types of ``namedtuple`` are
also provided to represent these values:
:class:`~webcolors.IntegerRGB` for integer triplets,
:class:`~webcolors.PercentRGB` for percentage triplets, and
:class:`~webcolors.HTML5SimpleColor` for an HTML5 simple
color. Functions which return an integer or percentage ``rgb()``
triplet, or an HTML5 simple color, will return values of these types.

Internally, Python ``float`` is used in some conversions to and from
the triplet representations; for each function which may have the
precision of its results affected by this, a note is provided in the
documentation.

For colors specified via ``rgb()`` triplets, values contained in the
triplets will be normalized in accordance with CSS clipping rules:

* Integer values less than 0 will be normalized to 0, and percentage
  values less than 0% will be normalized to 0%.

* Integer values greater than 255 will be normalized to 255, and
  percentage values greater than 100% will be normalized to 100%.

* The "negative zero" values -0 and -0% will be normalized to 0 and
  0%, respectively.

The functions :func:`~webcolors.normalize_integer_triplet` and
:func:`~webcolors.normalize_percent_triplet` can be used to
perform this normalization manually if desired.


Color names
-----------

For colors specified via predefined names, webcolors will accept
strings containing names case-insensitively, so long as they contain
no spaces or non-alphabetic characters. Thus, for example,
``u'AliceBlue'`` and ``u'aliceblue'`` are both accepted, and both will
refer to the same color: ``rgb(240, 248, 255)``.

For output which consists of a color name, and for functions which
perform intermediate conversion to a predefined name before returning
a result in another format, webcolors always normalizes such
values to be entirely lowercase.


.. _spec-identifiers:

Identifying sets of named colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For purposes of identifying the specification from which to draw the
selection of defined color names, webcolors recognizes the
following strings as identifiers:

``u'html4'``
    The HTML 4 named colors.

``u'css2'``
    The CSS 2 named colors.

``u'css21'``
    The CSS 2.1 named colors.

``u'css3'``
    The CSS 3/SVG named colors. For all functions for which the set of
    color names is relevant, this is the default set used.

The CSS 1 named colors are not represented here, as CSS 1 merely
"suggested" a set of color names, and declined to provide values for
them. The CSS 2 "system colors" are also not represented here, as they
had no fixed defined values and are now deprecated.
