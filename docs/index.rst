.. webcolors documentation master file, created by
   sphinx-quickstart on Sun Aug 30 01:02:30 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. module:: webcolors


webcolors
=========

This module provides a simple library for working with the color names
and color codes defined by the HTML and CSS specifications.


An overview of HTML and CSS colors
----------------------------------

Colors on the Web are specified in `the sRGB color space`_, where each
color is made up of a red component, a green component and a blue
component. This is useful because it maps (fairly) cleanly to the red,
green and blue components of pixels on a computer display, and to the
cone cells of a human eye, which come in three sets roughly
corresponding to the wavelengths of light associated with red, green
and blue.

`The HTML 4 standard`_ defines two ways to specify sRGB colors:

* A hash mark ('#') followed by three pairs of hexdecimal digits,
  specifying values for red, green and blue components in that order;
  for example, ``#0099cc``. Since each pair of hexadecimal digits can
  express 256 different values, this allows up to 256**3 or 16,777,216
  unique colors to be specified (though, due to differences in display
  technology, not all of these colors may be clearly distinguished on
  any given physical display).

* A set of predefined color names which correspond to specific
  hexadecimal values; for example, ``white``. HTML 4 defines sixteen
  such colors.

`The CSS 2 standard`_ allows any valid HTML 4 color specification, and
adds three new ways to specify sRGB colors:

* A hash mark followed by three hexadecimal digits, which is expanded
  into three hexadecimal pairs by repeating each digit; thus ``#09c``
  is equivalent to ``#0099cc``.

* The string 'rgb', followed by parentheses, between which are three
  numeric values each between 0 and 255, inclusive, which are taken to
  be the values of the red, green and blue components in that order;
  for example, ``rgb(0, 153, 204)``.

* The same as above, except using percentages instead of numeric
  values; for example, ``rgb(0%, 60%, 80%)``.

`The CSS 2.1 revision`_ does not add any new methods of specifying
sRGB colors, but does add one additional named color.

`The CSS 3 color module`_ (currently a W3C Candidate Recommendation)
adds one new way to specify sRGB colors:

* A hue-saturation-lightness triple (HSL), using the construct
  ``hsl()``.

It also adds support for variable opacity of colors, by allowing the
specification of alpha-channel information, through the ``rgba()`` and
``hsla()`` constructs, which are identical to ``rgb()`` and ``hsl()``
with one exception: a fourth value is supplied, indicating the level
of opacity from ``0.0`` (completely transparent) to ``1.0``
(completely opaque). Though not technically a color, the keyword
``transparent`` is also made available in lieu of a color value, and
corresponds to ``rgba(0,0,0,0)``.

Additionally, CSS3 defines a new set of color names; this set is taken
directly from the named colors defined for SVG (Scalable Vector
Graphics) markup, and is a proper superset of the named colors defined
in CSS 2.1. This set also has significant overlap with traditional X11
color sets as defined by the ``rgb.txt`` file on many Unix and
Unix-like operating systems, though the correspondence is not exact;
the set of X11 colors is not standardized, and the set of CSS3 colors
contains some definitions which diverge significantly from customary
X11 definitions (for example, CSS3's ``green`` is not equivalent to
X11's ``green``; the value which X11 designates ``green`` is
designated ``lime`` in CSS3).

.. _the sRGB color space: http://www.w3.org/Graphics/Color/sRGB
.. _The HTML 4 standard: http://www.w3.org/TR/html401/types.html#h-6.5
.. _The CSS 2 standard: http://www.w3.org/TR/REC-CSS2/syndata.html#value-def-color
.. _The CSS 2.1 revision: http://www.w3.org/TR/CSS21/
.. _The CSS 3 color module: http://www.w3.org/TR/css3-color/

What this module supports
-------------------------

The mappings and functions within this module support the following
methods of specifying sRGB colors, and conversions between them:

* Six-digit hexadecimal.

* Three-digit hexadecimal.

* Integer ``rgb()`` triplet.

* Percentage ``rgb()`` triplet.

* Varying selections of predefined color names (see below).

This module does not support ``hsl()`` triplets, nor does it support
opacity/alpha-channel information via ``rgba()`` or ``hsla()``.

If you need to convert between RGB-specified colors and HSL-specified
colors, or colors specified via other means, consult `the colorsys
module`_ in the Python standard library, which can perform conversions
amongst several common color spaces.

.. _the colorsys module: http://docs.python.org/library/colorsys.html

Normalization
~~~~~~~~~~~~~

For colors specified via hexadecimal values, this module will accept
input in the following formats:

* A hash mark (#) followed by three hexadecimal digits, where letters
  may be upper- or lower-case.

* A hash mark (#) followed by six hexadecimal digits, where letters
  may be upper- or lower-case.

For output which consists of a color specified via hexadecimal values,
and for functions which perform intermediate conversion to hexadecimal
before returning a result in another format, this module always
normalizes such values to the following format:

* A hash mark (#) followed by six hexadecimal digits, with letters
  forced to lower-case.

The function ``normalize_hex()`` in this module can be used to perform
this normalization manually if desired; see its documentation for an
explanation of the normalization process.

For colors specified via predefined names, this module will accept
input in the following formats:

* An entirely lower-case name, such as ``aliceblue``.

* A name using initial capitals, such as ``AliceBlue``.

For output which consists of a color specified via a predefined name,
and for functions which perform intermediate conversion to a
predefined name before returning a result in another format, this
module always normalizes such values to be entirely lower-case.


Module contents
---------------

.. function:: normalize_hex(hex_value)

   Normalize a hexadecimal color value to the following form and
   return the result::

       #[a-f0-9]{6}

   In other words, the following transformations are applied as
   needed:

   * If the value contains only three hexadecimal digits, it is
     expanded to six.

   * The value is normalized to lower-case.

   If the supplied value cannot be interpreted as a hexadecimal color
   value, ``ValueError`` is raised.

   :param hex_value: The hexadecimal color value to normalize.


Constants
~~~~~~~~~

.. data:: html4_names_to_hex

   A dictionary whose keys are the names of the defined colors in HTML
   4 (normalized to lowercase), and whose values are the corresponding
   (normalized) hexadecimal color values.

.. data:: html4_hex_to_names

   A dictionary whose keys are (normalized) hexadecimal color values
   of the named HTML 4 colors, and whose values are the corresponding
   (normalized to lowercase) names.

.. data:: css2_names_to_hex

   A dictionary whose keys are the names of the defined colors in CSS
   2 (normalized to lowercase), and whose values are the corresponding
   (normalized) hexadecimal color values.

   Because CSS 2 defines the same set of colors as HTML 4, this is
   simply an alias for :data:`html4_names_to_hex`.

.. data:: css2_hex_to_names

   A dictionary whose keys are (normalized) hexadecimal color values
   of the named CSS 2 colors, and whose values are the corresponding
   (normalized to lowercase) names.

   Because CSS 2 defines the same set of colors as HTML 4, this is
   simply an alias for :data:`html4_hex_to_names`.

.. data:: css21_names_to_hex

   A dictionary whose keys are the names of the defined colors in CSS
   2.1 (normalized to lowercase), and whose values are the
   corresponding (normalized) hexadecimal color values.

.. data:: css21_hex_to_names

   A dictionary whose keys are the (normalized) hexadecimal color
   values of the named CSS 2.1 colors, and whose values are the
   corresponding (normalized to lowercase) names.

.. data:: css3_names_to_hex

   A dictionary whose keys are the names of the defined colors in the
   CSS 3 color module (normalized to lowercase), and whose values are
   the corresponding (normalized) hexadecimal color values.

.. data:: css3_hex_to_names

   A dictionary whose keys are the (normalized) hexadecimal color
   values of the named CSS 3 colors, and whose values are the
   corresponding (normalized to lowercase) names.


Conversions from color names to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: name_to_hex(name, spec='css3')

   Convert a color name to a normalized hexadecimal color value.

   The color name will be normalized to lower-case before being looked
   up, and when no color of that name exists in the given
   specification, ``ValueError`` is raised.

   Examples::

       >>> name_to_rgb('navy')
       (0, 0, 128)
       >>> name_to_rgb('cadetblue')
       (95, 158, 160)
       >>> name_to_rgb('cadetblue', spec='html4')
       Traceback (most recent call last):
           ...
       ValueError: 'cadetblue' is not defined as a named color in html4.

   :param name: The color name to convert.
   :param spec: The specification from which to draw the list of color
      names; valid values are ``html4``, ``css2``, ``css21`` and
      ``css3``. Default is ``css3``.

.. function:: name_to_rgb(name, spec='css3')

   Convert a color name to a 3-tuple of integers suitable for use in
   an ``rgb()`` triplet specifying that color.

   The color name will be normalized to lower-case before being looked
   up, and when no color of that name exists in the given
   specification, ``ValueError`` is raised.

   Examples::

       >>> name_to_rgb_percent('white')
       ('100%', '100%', '100%')
       >>> name_to_rgb_percent('navy')
       ('0%', '0%', '50%')
       >>> name_to_rgb_percent('goldenrod')
       ('85.49%', '64.71%', '12.5%')

   :param name: The color name to convert.
   :param spec: The specification from which to draw the list of color
      names; valid values are ``html4``, ``css2``, ``css21`` and
      ``css3``. Default is ``css3``.

.. function:: name_to_rgb_percent(name, spec='css3')

   Convert a color name to a 3-tuple of percentages suitable for use
   in an ``rgb()`` triplet specifying that color.

   The color name will be normalized to lower-case before being looked
   up, and when no color of that name exists in the given
   specification, ``ValueError`` is raised.

   Examples::

       >>> name_to_rgb_percent('white')
       ('100%', '100%', '100%')
       >>> name_to_rgb_percent('navy')
       ('0%', '0%', '50%')
       >>> name_to_rgb_percent('goldenrod')
       ('85.49%', '64.71%', '12.5%')

   :param name: The color name to convert.
   :param spec: The specification from which to draw the list of color
      names; valid values are ``html4``, ``css2``, ``css21`` and
      ``css3``. Default is ``css3``.


Conversions from hexadecimal color values to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: hex_to_name(hex_value, spec='css3')

   Convert a hexadecimal color value to its corresponding normalized
   color name, if any such name exists.

   The hexadecimal value will be normalized before being looked up,
   and when no color name for the value is found in the given
   specification, ``ValueError`` is raised.

   Examples::

       >>> hex_to_name('#000080')
       'navy'
       >>> hex_to_name('#000080', spec='html4')
       'navy'
       >>> hex_to_name('#8b4513')
       'saddlebrown'
       >>> hex_to_name('#8b4513', spec='html4')
       Traceback (most recent call last):
           ...
       ValueError: '#8b4513' has no defined color name in html4.

   :param hex_value: The hexadecimal color value to convert.
   :param spec: The specification from which to draw the list of color
      names; valid values are ``html4``, ``css2``, ``css21`` and
      ``css3``. Default is ``css3``.

.. function:: hex_to_rgb(hex_value)

   Convert a hexadecimal color value to a 3-tuple of integers suitable
   for use in an ``rgb()`` triplet specifying that color.

   The hexadecimal value will be normalized before being converted.

   Examples::

       >>> hex_to_rgb('#000080')
       (0, 0, 128)
       >>> hex_to_rgb('#ffff00')
       (255, 255, 0)
       >>> hex_to_rgb('#f00')
       (255, 0, 0)
       >>> hex_to_rgb('#deb887')
       (222, 184, 135)

   :param hex_value: The hexadecimal color value to convert.

.. function:: hex_to_rgb_percent(hex_value)

   Convert a hexadecimal color value to a 3-tuple of percentages
   suitable for use in an ``rgb()`` triplet representing that color.

   The hexadecimal value will be normalized before converting.

   Examples::

       >>> hex_to_rgb_percent('#ffffff')
       ('100%', '100%', '100%')
       >>> hex_to_rgb_percent('#000080')
       ('0%', '0%', '50%')

   :param hex_value: The hexadecimal color value to convert.


Conversions from integer ``rgb()`` triplets to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: rgb_to_name(rgb_triplet, spec='css3')

   Convert a 3-tuple of integers, suitable for use in an ``rgb()``
   color triplet, to its corresponding normalized color name, if any
   such name exists.

   If there is no matching name, ``ValueError`` is raised.

   Examples::

       >>> rgb_to_name((0, 0, 0))
       'black'
       >>> rgb_to_name((0, 0, 128))
       'navy'
       >>> rgb_to_name((95, 158, 160))
       'cadetblue'

   :param rgb_triplet: The ``rgb()`` triplet, as a three-tuple of
      integers.
   :param spec: The specification from which to draw the list of color
      names; valid values are ``html4``, ``css2``, ``css21`` and
      ``css3``. Default is ``css3``.

.. function:: rgb_to_hex(rgb_triplet)

   Convert a 3-tuple of integers, suitable for use in an ``rgb()``
   color triplet, to a normalized hexadecimal value for that color.

   Examples::

       >>> rgb_to_hex((255, 255, 255))
       '#ffffff'
       >>> rgb_to_hex((0, 0, 128))
       '#000080'
       >>> rgb_to_hex((33, 56, 192))
       '#2138c0'

   :param rgb_triplet: The ``rgb()`` triplet, as a three-tuple of
      integers.

.. function:: rgb_to_rgb_percent(rgb_triplet)

   Convert a 3-tuple of integers, suitable for use in an ``rgb()``
   color triplet, to a 3-tuple of percentages suitable for use in
   representing that color.

   This function makes some trade-offs in terms of the accuracy of the
   final representation; for some common integer values, special-case
   logic is used to ensure a precise result (e.g., integer 128 will
   always convert to '50%', integer 32 will always convert to
   '12.5%'), but for all other values a standard Python ``float`` is
   used and rounded to two decimal places, which may result in a loss
   of precision for some values.

   Examples:

       >>> rgb_to_rgb_percent((255, 255, 255))
       ('100%', '100%', '100%')
       >>> rgb_to_rgb_percent((0, 0, 128))
       ('0%', '0%', '50%')
       >>> rgb_to_rgb_percent((33, 56, 192))
       ('12.94%', '21.96%', '75.29%')
       >>> rgb_to_rgb_percent((64, 32, 16))
       ('25%', '12.5%', '6.25%')

   :param rgb_triplet: The ``rgb()`` triplet, as a three-tuple of
      integers.


Conversions from percentage ``rgb()`` triplets to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: rgb_percent_to_name(rgb_percent_triplet, spec='css3')

   Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
   color triplet, to its corresponding normalized color name, if any
   such name exists.

   If there is no matching name, ``ValueError`` is raised.

   Examples::

       >>> rgb_percent_to_name(('0%', '0%', '0%'))
       'black'
       >>> rgb_percent_to_name(('0%', '0%', '50%'))
       'navy'
       >>> rgb_percent_to_name(('85.49%', '64.71%', '12.5%'))
       'goldenrod'

   :param rgb_percent_triplet: The ``rgb()`` triplet, as a three-tuple
      of strings giving percentage values.
   :param spec: The specification from which to draw the list of color
      names; valid values are ``html4``, ``css2``, ``css21`` and
      ``css3``. Default is ``css3``.

.. function:: rgb_percent_to_hex(rgb_percent_triplet)

   Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
   color triplet, to a normalized hexadecimal color value for that
   color.

   Examples::

       >>> rgb_percent_to_hex(('100%', '100%', '0%'))
       '#ffff00'
       >>> rgb_percent_to_hex(('0%', '0%', '50%'))
       '#000080'
       >>> rgb_percent_to_hex(('85.49%', '64.71%', '12.5%'))
       '#daa520'

   :param rgb_percent_triplet: The ``rgb()`` triplet, as a three-tuple
      of strings giving percentage values.

.. function:: rgb_percent_to_rgb(rgb_percent_triplet)

   Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
   color triplet, to a 3-tuple of integers suitable for use in
   representing that color.

   Some precision may be lost in this conversion. See the note
   regarding precision for ``rgb_to_rgb_percent()`` for details;
   generally speaking, the following is true for any 3-tuple ``t`` of
   integers in the range 0...255 inclusive::

       t == rgb_percent_to_rgb(rgb_to_rgb_percent(t))

   Examples::

       >>> rgb_percent_to_rgb(('100%', '100%', '100%'))
       (255, 255, 255)
       >>> rgb_percent_to_rgb(('0%', '0%', '50%'))
       (0, 0, 128)
       >>> rgb_percent_to_rgb(('25%', '12.5%', '6.25%'))
       (64, 32, 16)
       >>> rgb_percent_to_rgb(('12.94%', '21.96%', '75.29%'))
       (33, 56, 192)

   :param rgb_percent_triplet: The ``rgb()`` triplet, as a three-tuple
      of strings giving percentage values.
