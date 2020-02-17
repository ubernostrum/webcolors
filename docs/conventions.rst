.. _conventions:


Normalization and conventions
=============================

Since the various formats used to specify colors in web documents do
not always map cleanly to Python data types, and some variation is
permitted in how to use each format in a web document, webcolors
applies a set of conventions for representing color names and values,
and for normalizing them.


.. _string-types:

Python string types
-------------------

As Python 2 is no longer supported by the Python core team, webcolors
now supports only Python 3, where the string type is a Unicode
string. Python 3 does still have the :class:`bytes` type, but all
string arguments to functions in webcolors must be :class:`str` and
never :class:`bytes`.


Hexadecimal color values
------------------------

For colors specified via hexadecimal values, webcolors will accept
strings in the following formats:

* The character `#` followed by three hexadecimal digits, where digits
  A-F may be upper- or lowercase.

* The character `#` followed by six hexadecimal digits, where digits
  A-F may be upper- or lowercase (i.e., what HTML5 designates a "valid
  simple color" when all digits are uppercase, and a "valid lowercase
  simple color" when all digits are lowercase).

For output which consists of a color specified via hexadecimal values,
and for functions which perform intermediate conversion to hexadecimal
before returning a result in another format, webcolors always
normalizes such values to a string in the following format:

* The character `#` followed by six hexadecimal digits, with digits
  A-F forced to lowercase (what HTML5 designates a "valid lowercase
  simple color").

The function :func:`~webcolors.normalize_hex` can be used to perform
this normalization manually if desired.


Integer and percentage `rgb()` triplets
-----------------------------------------

Functions which work with integer `rgb()` triplets accept them as a
3-:class:`tuple` of Python :class:`int`. Functions which work with
percentage `rgb()` triplets accept them as 3-:class:`tuple` of Python
strings (see :ref:`above regarding Python string types
<string-types>`).

Plain tuples are accepted by all functions which deal with integer or
percentage `rgb()` triplets, but three types of
:func:`~collections.namedtuple` are also provided to represent these
values: :class:`~webcolors.IntegerRGB` for integer triplets,
:class:`~webcolors.PercentRGB` for percentage triplets, and
:class:`~webcolors.HTML5SimpleColor` for an HTML5 simple
color. Functions which return an integer or percentage `rgb()`
triplet, or an HTML5 simple color, will return values of these types.

Internally, Python :class:`float` is used in some conversions to and
from the triplet representations; for each function which may have the
precision of its results affected by this, a note is provided in the
documentation.

For colors specified via `rgb()` triplets, values contained in the
triplets will be normalized in accordance with CSS clipping rules:

* Integer values less than 0 will be normalized to 0, and percentage
  values less than 0% will be normalized to 0%.

* Integer values greater than 255 will be normalized to 255, and
  percentage values greater than 100% will be normalized to 100%.

* The "negative zero" values -0 and -0% will be normalized to 0 and
  0%, respectively.

The functions :func:`~webcolors.normalize_integer_triplet` and
:func:`~webcolors.normalize_percent_triplet` can be used to perform
this normalization manually if desired.


.. _color-name-conventions:

Color names
-----------

For colors specified via predefined names, webcolors will accept
strings containing names case-insensitively, so long as they contain
no spaces or non-alphabetic characters. Thus, for example,
`'AliceBlue'` and `'aliceblue'` are both accepted, and both will
refer to the same color: `rgb(240, 248, 255)`.

For output which consists of a color name, and for functions which
perform intermediate conversion to a predefined name before returning
a result in another format, webcolors always normalizes such values to
be entirely lowercase.

.. note:: **Spelling variants**

   HTML 4, CSS1, and CSS2 each defined a color named `gray`. In CSS3,
   this color can be named either `gray` or `grey`, and several other
   related color values each have two names in CSS3:
   `darkgray`/`darkgrey`, `darkslategray`/`darkslategrey`,
   `dimgray`/`dimgrey`, `lightgray`/`lightgrey`,
   `lightslategray`/`lightslategrey`, `slategray`/`slategrey`.

   Reversing from the hexadecimal value, integer tuple, or percent
   tuple to a name, for these colors, requires picking one spelling,
   and webcolors chooses the `gray` spellings for consistency with
   HTML 4, CSS1, and CSS2.



Identifying sets of named colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For purposes of identifying the specification from which to draw the
selection of defined color names, webcolors uses strings naming the
specifications, and provides :ref:`a set of constants containing the
correct values <spec-constants>`.

Note that the CSS1 named colors are not supported here, as CSS1 merely
"suggested" a set of color names, and declined to provide values for
them. The CSS2 "system colors" are also not represented here, as they
had no fixed defined values and are now deprecated.
