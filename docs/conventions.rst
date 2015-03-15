.. _conventions:


Normalization and conventions
=============================

Since the various formats used to specify colors in Web documents do
not always map cleanly to Python data types, and some variation is
permitted in how to use each format in a Web document, ``webcolors``
applies a set of conventions for representing color names and values,
and for normalizing them.


Python string types
-------------------

The ``webcolors`` module is written to be compatible with both Python
2 and Python 3, which have different approaches to strings:

* On Python 2, the ``str`` type is a sequence of bytes in a particular
  encoding, and Unicode strings are represented by the type
  ``unicode``. Promiscuous mixing of ``str`` and ``unicode`` is
  possible in Python 2, but not recommended as it is a frequent source
  of bugs.

* On Python 3, the ``str`` type is a Unicode string, and sequences of
  bytes in any particular encoding are represented by the type
  ``bytes``. Promiscuous mixing of ``str`` and ``bytes`` is not
  permitted in Python 3, and will often simply raise exceptions.

The approach to string types in ``webcolors`` is as follows:

* All mappings from color names to hexadecimal values (and vice versa)
  are dictionaries whose keys and values are Unicode strings (``str``
  on Python 3 and ``unicode`` on Python 2). This permits promiscuous
  use of byte strings on Python 2, but will yield results as Unicode
  strings.

* All functions which return a string value or a tuple of string
  values will return a Unicode string (``str`` on Python 3 and
  ``unicode`` on Python 2).

* All functions which accept a string value or tuple of string values
  as an argument, *except* for the HTML5 color algorithms (see below),
  will accept a sequence of bytes (``str``) on Python 2, but will
  convert to Unicode strings (``unicode``) for output.

Because the HTML5 Recommendation specifies its color algorithms in
terms of Unicode strings only (and in some cases, requires exact
identification of Unicode code points to determine behavior), the
following constraints apply to these functions:

* Inputs which are specified by HTML5 to be strings must be of type
  ``str`` (not ``bytes``) on Python 3, and of type ``unicode`` (not
  ``str``) on Python 2. A ``ValueError`` will be raised if a
  bytestring (``bytes`` on Python 3 or ``str`` on Python 2) is
  provided as an argument.

* Outputs which are specified by HTML5 to be strings will be of type
  ``str`` (never ``bytes``) on Python 3, and of type ``unicode``
  (never ``str``) on Python 2.

Because Unicode strings are everywhere preferred (and in some cases
mandatory) as input, and consistently produced as output, all
documentation of functions in ``webcolors`` which involves string
input or output uses the ``u`` prefix as a reminder. Use of that
prefix is required in Python 2 to mark Unicode strings; in Python 3.3
and later, use is permitted on strings, but has no effect as ``str``
is a Unicode type in Python 3. Internally, ``webcolors`` uses the
``u`` prefix on all strings it produces for output.


Hexadecimal color values
------------------------

For colors specified via hexadecimal values, ``webcolors`` will accept
strings in the following formats:

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
Python Unicode strings (``unicode`` or ``str`` depending on Python
version).

Internally, Python ``float`` is used in some conversions to and from
the triplet representations; for each function which may have the
precision of its results affected by this, a note is provided in the
documentation.

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
