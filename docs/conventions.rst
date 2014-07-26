.. _conventions:


Normalization and conventions
=============================

Since the various formats used to specify colors in Web documents do
not always map cleanly to Python data types, and some variation is
permitted in how to use each format in a Web document, ``webcolors``
applies a set of conventions for representing color names and values,
and for normalizing them.


Hexadecimal color values
------------------------

For colors specified via hexadecimal values, ``webcolors`` will accept
strings (Python ``str``, regardless of Python version) in the
following formats:

* The character ``#`` followed by three hexadecimal digits, where
  digits A-F may be upper- or lowercase.

* The character ``#`` followed by six hexadecimal digits, where
  digits A-F may be upper- or lowercase (i.e., what HTML5 designates a
  "valid simple color" when all digits are uppercase, and a "valid
  lowercase simple color" when all digits are lowercase).

For output which consists of a color specified via hexadecimal values,
and for functions which perform intermediate conversion to hexadecimal
before returning a result in another format, ``webcolors`` always
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
percentage ``rgb()`` triplets accept and return them as a 3-tuple of
Python ``str``.

For colors specified via ``rgb()`` triplets, values contained in the
triplets will be normalized via clipping in accordance with CSS:

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

For colors specified via predefined names, ``webcolors`` will accept
strings containing names so long as they contain no spaces or
non-alphabetic characters, and regardless of case. Thus, for example,
``AliceBlue`` and ``aliceblue`` are both accepted, and both will refer
to the same color (namely, ``rgb(240, 248, 255)``).

For output which consists of a color name, and for functions which
perform intermediate conversion to a predefined name before returning
a result in another format, ``webcolors`` always normalizes such
values to be entirely lowercase.


.. _spec-identifiers:

Identifying sets of named colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For purposes of identifying the specification from which to draw the
selection of defined color names, ``webcolors`` recognizes the
following strings as identifiers:

``'html4'``
    The HTML 4 named colors.

``'css2'``
    The CSS 2 named colors.

``'css21'``
    The CSS 2.1 named colors.

``'css3'``
    The CSS 3/SVG named colors. For all functions for which the set of
    color names is relevant, this is the default set used.

The CSS 1 named colors are not represented here, as CSS 1 merely
"suggested" a set of color names, and declined to provide values for
them. The CSS 2 "system colors" are also not represented here, as they
had no fixed defined values and are now deprecated.


