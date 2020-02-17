.. module:: webcolors

.. _contents:


Module contents
===============

The contents of the webcolors module fall into five categories:

1. A set of (optional) data types for representing color values.

2. Constants for several purposes.

3. Normalization functions which sanitize input in various formats
   prior to conversion or output.

4. Conversion functions between each method of specifying colors.

5. Implementations of the color parsing and serialization algorithms
   in HTML5.

See :ref:`the documentation regarding conventions <conventions>` for
information regarding the types and representation of various color
formats in webcolors.

All conversion functions which involve color names take an optional
argument to determine the specification from which to draw color
names. See :ref:`the set of specification identifiers
<spec-constants>` for valid values.

All conversion functions, when faced with identifiably invalid
hexadecimal color values, or with a request to name a color which has
no name in the requested specification, or with an invalid
specification identifier, will raise :exc:`ValueError`.


Data types
----------

Integer and percentage `rgb()` triplets, and HTML5 simple colors, can
be passed to functions in webcolors as plain 3-:class:`tuple` of the
appropriate data type. But the following
:func:`~collections.namedtuple` instances are also provided to
represent these types more richly, and functions in webcolors which
return triplets or simple colors will return instances of these:

.. class:: IntegerRGB

   A :func:`~collections.namedtuple` representing an integer RGB
   triplet. Has three fields, each of type :class:`int` and in the
   range 0-255 inclusive:

   .. attribute:: red

      The red portion of the color value.

   .. attribute:: green

      The red portion of the color value.

   .. attribute:: blue

      The red portion of the color value.

.. class:: PercentRGB

   A :func:`~collections.namedtuple` representing a percentage RGB
   triplet. Has three fields, each of type :class:`str` and
   representing a percentage value in the range 0%-100% inclusive:

   .. attribute:: red

      The red portion of the color value.

   .. attribute:: green

      The red portion of the color value.

   .. attribute:: blue

      The red portion of the color value.

.. class:: HTML5SimpleColor

   A :func:`~collections.namedtuple` representing an HTML5 simple
   color. Has three fields, each of type :class:`int` and in the range
   0-255 inclusive:

   .. attribute:: red

      The red portion of the color value.

   .. attribute:: green

      The red portion of the color value.

   .. attribute:: blue

      The red portion of the color value.


Constants
---------

Several sets of constants are provided in webcolors, for use when
converting or identifying colors or specifications.

.. _spec-constants:

Specification identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following constants are available for indicating the specification
from which to draw color name choices, in functions which can work
with multiple specifications.

.. data:: CSS2

   Represents the CSS2 specification. Value is `'css2'`.

.. data:: CSS21

   Represents the CSS2.1 specification. Value is `'css21'`.

.. data:: CSS3

   Represents the CSS3 specification. Value is `'css3'`.

.. data:: HTML4

   Represents the HTML 4 specification. Value is `'html4'`.

.. _mapping-constants:

Color mappings
~~~~~~~~~~~~~~

The following constants are available for direct use in mapping from
color names to values, although it is strongly recommended to use one
of the normalizing conversion functions instead.


Mappings from names to hexadecimal values
+++++++++++++++++++++++++++++++++++++++++

.. data:: HTML4_NAMES_TO_HEX

   A :class:`dict` whose keys are the normalized names of the sixteen
   named HTML 4 colors, and whose values are the normalized
   hexadecimal values of those colors.

.. data:: CSS2_NAMES_TO_HEX

   An alias for :data:`~webcolors.HTML4_NAMES_TO_HEX`, as CSS2
   defined the same set of colors.

.. data:: CSS21_NAMES_TO_HEX

   A :class:`dict` whose keys are the normalized names of the
   seventeen named CSS2.1 colors, and whose values are the normalized
   hexadecimal values of those colors (sixteen of these are identical
   to HTML 4 and CSS2; the seventeenth color is `orange`, added in
   CSS2.1).

.. data:: CSS3_NAMES_TO_HEX

   A :class:`dict` whose keys are the normalized names of the 147
   named CSS3 colors, and whose values are the normalized hexadecimal
   values of those colors. These colors are also identical to the 147
   named colors of SVG.


Mappings from hexadecimal values to names
+++++++++++++++++++++++++++++++++++++++++

.. data:: HTML4_HEX_TO_NAMES

   A :class:`dict` whose keys are the normalized hexadecimal values of
   the sixteen named HTML 4 colors, and whose values are the
   corresponding normalized names.

.. data:: CSS2_HEX_TO_NAMES

   An alias for :data:`~webcolors.HTML4_HEX_TO_NAMES`, as CSS2 defined
   the same set of colors.

.. data:: CSS21_HEX_TO_NAMES

   A :class:`dict` whose keys are the normalized hexadecimal values of
   the seventeen named CSS2.1 colors, and whose values are the
   corresponding normalized names (sixteen of these are identical to
   HTML 4 and CSS2; the seventeenth color is `orange`, added in
   CSS2.1).

.. data:: CSS3_HEX_TO_NAMES

   A :class:`dict` whose keys are the normalized hexadecimal values of
   the 147 named CSS3 colors, and whose values are the corresponding
   normalized names. These colors are also identical to the 147 named
   colors of SVG.

   .. note:: **Spelling variants**

      Some values representing named gray colors can map to either of
      two names in CSS3, because it supports both `gray` and `grey`
      spelling variants for those colors. This mapping will always
      return the variant spelled `gray` (such as `lightgray` instead
      of `lightgrey`). See :ref:`the documentation on name conventions
      <color-name-conventions>` for details.


Normalization functions
-----------------------

.. function:: normalize_hex(hex_value)

   Normalize a hexadecimal color value to a string consisting of the
   character `#` followed by six lowercase hexadecimal digits (what
   HTML5 terms a "valid lowercase simple color").

   If the supplied value cannot be interpreted as a hexadecimal color
   value, :exc:`ValueError` is raised. See :ref:`the conventions used
   by this module <conventions>` for information on acceptable formats
   for hexadecimal values.

   Examples:

   .. code-block:: pycon

       >>> normalize_hex('#0099cc')
       '#0099cc'
       >>> normalize_hex('#0099CC')
       '#0099cc'
       >>> normalize_hex('#09c')
       '#0099cc'
       >>> normalize_hex('#09C')
       '#0099cc'
       >>> normalize_hex('#0099gg')
       Traceback (most recent call last):
           ...
       ValueError: '#0099gg' is not a valid hexadecimal color value.
       >>> normalize_hex('0099cc')
       Traceback (most recent call last):
           ...
       ValueError: '0099cc' is not a valid hexadecimal color value.

   :param str hex_value: The hexadecimal color value to normalize.
   :rtype: :class:`str`
   :raises ValueError: when the input is not a valid hexadecimal color value.

.. function:: normalize_integer_triplet(rgb_triplet)

    Normalize an integer `rgb()` triplet so that all values are
    within the range 0..255.

    Examples:

    .. code-block:: pycon

        >>> normalize_integer_triplet((128, 128, 128))
        IntegerRGB(red=128, green=128, blue=128)
        >>> normalize_integer_triplet((0, 0, 0))
        IntegerRGB(red=0, green=0, blue=0)
        >>> normalize_integer_triplet((255, 255, 255))
        IntegerRGB(red=255, green=255, blue=255)
        >>> normalize_integer_triplet((270, -20, -0))
        IntegerRGB(red=255, green=0, blue=0)
    
    :param tuple rgb_triplet: The integer `rgb()` triplet to normalize.
    :rtype: IntegerRGB

.. function:: normalize_percent_triplet(rgb_triplet)

    Normalize a percentage `rgb()` triplet so that all values are
    within the range 0%..100%.

    Examples:

    .. code-block:: pycon
   
       >>> normalize_percent_triplet(('50%', '50%', '50%'))
       PercentRGB(red='50%', green='50%', blue='50%')
       >>> normalize_percent_triplet(('0%', '100%', '0%'))
       PercentRGB(red='0%', green='100%', blue='0%')
       >>> normalize_percent_triplet(('-10%', '-0%', '500%'))
       PercentRGB(red='0%', green='0%', blue='100%')
    
    :param tuple rgb_triplet: The percentage `rgb()` triplet to normalize.
    :rtype: PercentRGB


Conversions from color names to other formats
---------------------------------------------

.. function:: name_to_hex(name, spec=CSS3)

   Convert a color name to a normalized hexadecimal color value.

   The color name will be normalized to lower-case before being looked
   up.

   Examples:

   .. code-block:: pycon

       >>> name_to_hex('white')
       '#ffffff'
       >>> name_to_hex('navy')
       '#000080'
       >>> name_to_hex('goldenrod')
       '#daa520'
       >>> name_to_hex('goldenrod', spec=HTML4)
       Traceback (most recent call last):
           ...
       ValueError: 'goldenrod' is not defined as a named color in html4.

   :param str name: The color name to convert.
   :param str spec: The specification from which to draw the list of color
      names. Default is :data:`CSS3`.
   :rtype: :class:`str`
   :raises ValueError: when the given name has no definition in the given spec.


.. function:: name_to_rgb(name, spec=CSS3)

   Convert a color name to a 3-:class:`tuple` of :class:`int` suitable for use in
   an `rgb()` triplet specifying that color.

   The color name will be normalized to lower-case before being looked
   up.

   Examples:
   
   .. code-block:: pycon

       >>> name_to_rgb('white')
       IntegerRGB(red=255, green=255, blue=255)
       >>> name_to_rgb('navy')
       IntegerRGB(red=0, green=0, blue=128)
       >>> name_to_rgb('goldenrod')
       IntegerRGB(red=218, green=165, blue=32)

   :param str name: The color name to convert.
   :param str spec: The specification from which to draw the list of color
      names. Default is :data:`CSS3.`
   :rtype: IntegerRGB
   :raises ValueError: when the given name has no definition in the given spec.


.. function:: name_to_rgb_percent(name, spec=CSS3)

   Convert a color name to a 3-:class:`tuple` of percentages suitable for use
   in an `rgb()` triplet specifying that color.

   The color name will be normalized to lower-case before being looked
   up.

   Examples:
   
   .. code-block:: pycon

       >>> name_to_rgb_percent('white')
       PercentRGB(red='100%', green='100%', blue='100%')
       >>> name_to_rgb_percent('navy')
       PercentRGB(red='0%', green='0%', blue='50%')
       >>> name_to_rgb_percent('goldenrod')
       PercentRGB(red='85.49%', green='64.71%', blue='12.5%')

   :param str name: The color name to convert.
   :param str spec: The specification from which to draw the list of color
      names. Default is :data:`CSS3`.
   :rtype: PercentRGB
   :raises ValueError: when the given name has no definition in the given spec.


Conversion from hexadecimal color values to other formats
---------------------------------------------------------

.. function:: hex_to_name(hex_value, spec=CSS3)

   Convert a hexadecimal color value to its corresponding normalized
   color name, if any such name exists.

   The hexadecimal value will be normalized before being looked up.

   .. note:: **Spelling variants**

      Some values representing named gray colors can map to either of
      two names in CSS3, because it supports both `gray` and `grey`
      spelling variants for those colors. This function will always
      return the variant spelled `gray` (such as `lightgray` instead
      of `lightgrey`). See :ref:`the documentation on name conventions
      <color-name-conventions>` for details.

   Examples:

   .. code-block:: pycon

       >>> hex_to_name('#ffffff')
       'white'
       >>> hex_to_name('#fff')
       'white'
       >>> hex_to_name('#000080')
       'navy'
       >>> hex_to_name('#daa520')
       'goldenrod'
       >>> hex_to_name('#daa520', spec=HTML4)
       Traceback (most recent call last):
           ...
       ValueError: '#daa520' has no defined color name in html4.

   :param str hex_value: The hexadecimal color value to convert.
   :param str spec: The specification from which to draw the list of color
      names. Default is :data:`CSS3`.
   :rtype: :class:`str`
   :raises ValueError: when the given color has no name in the given
      spec, or when the supplied hex value is invalid.

.. function:: hex_to_rgb(hex_value)

   Convert a hexadecimal color value to a 3-:class:`tuple` of :class:`int` suitable
   for use in an `rgb()` triplet specifying that color.

   The hexadecimal value will be normalized before being converted.

   Examples:

   .. code-block:: pycon
   
       >>> hex_to_rgb('#fff')
       IntegerRGB(red=255, green=255, blue=255)
       >>> hex_to_rgb('#000080')
       IntegerRGB(red=0, green=0, blue=128)

   :param str hex_value: The hexadecimal color value to convert.
   :rtype: IntegerRGB
   :raises ValueError: when the supplied hex value is invalid.


.. function:: hex_to_rgb_percent(hex_value)

   Convert a hexadecimal color value to a 3-:class:`tuple` of percentages
   suitable for use in an `rgb()` triplet representing that color.

   The hexadecimal value will be normalized before being converted.

   Examples:

   .. code-block:: pycon

       >>> hex_to_rgb_percent('#ffffff')
       PercentRGB(red='100%', green='100%', blue='100%')
       >>> hex_to_rgb_percent('#000080')
       PercentRGB(red='0%', green='0%', blue='50%')

   :param str hex_value: The hexadecimal color value to convert.
   :rtype: PercentRGB
   :raises ValueError: when the supplied hex value is invalid.


Conversions from integer `rgb()` triplets to other formats
------------------------------------------------------------

.. function:: rgb_to_name(rgb_triplet, spec=CSS3)

   Convert a 3-:class:`tuple` of :class:`int`, suitable for use in an `rgb()`
   color triplet, to its corresponding normalized color name, if any
   such name exists.

   To determine the name, the triplet will be converted to a
   normalized hexadecimal value.

   .. note:: **Spelling variants**

      Some values representing named gray colors can map to either of
      two names in CSS3, because it supports both `gray` and `grey`
      spelling variants for those colors. This function will always
      return the variant spelled `gray` (such as `lightgray` instead
      of `lightgrey`). See :ref:`the documentation on name conventions
      <color-name-conventions>` for details.

   Examples:
   
   .. code-block:: pycon

       >>> rgb_to_name((255, 255, 255))
       'white'
       >>> rgb_to_name((0, 0, 128))
       'navy'

   :param rgb_triplet: The `rgb()` triplet
   :type rgb_triplet: typing.Union[IntegerRGB, Tuple[int, int, int]]
   :param str spec: The specification from which to draw the list of color
      names. Default is :data:`CSS3`.
   :rtype: :class:`str`
   :raises ValueError: when the given color has no name in the given spec.


.. function:: rgb_to_hex(rgb_triplet)

   Convert a 3-:class:`tuple` of :class:`int`, suitable for use in an `rgb()`
   color triplet, to a normalized hexadecimal value for that color.

   Examples:
   
   .. code-block:: pycon

       >>> rgb_to_hex((255, 255, 255))
       '#ffffff'
       >>> rgb_to_hex((0, 0, 128))
       '#000080'

   :param rgb_triplet: The `rgb()` triplet.
   :type rgb_triplet: typing.Union[IntegerRGB, Tuple[int, int, int]]
   :rtype: :class:`str`


.. function:: rgb_to_rgb_percent(rgb_triplet)

   Convert a 3-:class:`tuple` of :class:`int`, suitable for use in an `rgb()`
   color triplet, to a 3-:class:`tuple` of percentages suitable for use in
   representing that color.

   .. note:: **Floating-point precision**

      This function makes some trade-offs in terms of the accuracy of
      the final representation; for some common integer values,
      special-case logic is used to ensure a precise result (e.g.,
      integer 128 will always convert to `'50%'`, integer 32 will
      always convert to `'12.5%'`), but for all other values a
      standard Python :class:`float` is used and rounded to two
      decimal places, which may result in a loss of precision for some
      values due to the inherent imprecision of `IEEE floating-point
      numbers <http://en.wikipedia.org/wiki/IEEE_floating_point>`_.

   Examples:
   
   .. code-block:: pycon

       >>> rgb_to_rgb_percent((255, 255, 255))
       PercentRGB(red='100%', green='100%', blue='100%')
       >>> rgb_to_rgb_percent((0, 0, 128))
       PercentRGB(red='0%', green='0%', blue='50%')
       >>> rgb_to_rgb_percent((218, 165, 32))
       PercentRGB(red='85.49%', green='64.71%', blue='12.5%')

   :param rgb_triplet: The `rgb()` triplet.
   :type rgb_triplet: typing.Union[IntegerRGB, Tuple[int, int, int]]
   :rtype: PercentRGB


Conversions from percentage `rgb()` triplets to other formats
---------------------------------------------------------------

.. function:: rgb_percent_to_name(rgb_percent_triplet, spec=CSS3)

   Convert a 3-:class:`tuple` of percentages, suitable for use in an `rgb()`
   color triplet, to its corresponding normalized color name, if any
   such name exists.

   To determine the name, the triplet will be converted to a
   normalized hexadecimal value.

   .. note:: **Spelling variants**

      Some values representing named gray colors can map to either of
      two names in CSS3, because it supports both `gray` and `grey`
      spelling variants for those colors. This function will always
      return the variant spelled `gray` (such as `lightgray` instead
      of `lightgrey`). See :ref:`the documentation on name conventions
      <color-name-conventions>` for details.

   Examples:

   .. code-block:: pycon

       >>> rgb_percent_to_name(('100%', '100%', '100%'))
       'white'
       >>> rgb_percent_to_name(('0%', '0%', '50%'))
       'navy'
       >>> rgb_percent_to_name(('85.49%', '64.71%', '12.5%'))
       'goldenrod'

   :param rgb_percent_triplet: The `rgb()` triplet. 
   :type rgb_percent_triplet: typing.Union[PercentRGB, Tuple[str, str, str]]
   :param str spec: The specification from which to draw the list of color
       names. Default is :data:`CSS3`.
   :rtype: :class:`str`
   :raises ValueError: when the given color has no name in the given spec.


.. function:: rgb_percent_to_hex(rgb_percent_triplet)

   Convert a 3-:class:`tuple` of percentages, suitable for use in an `rgb()`
   color triplet, to a normalized hexadecimal color value for that
   color.

   Examples:
   
   .. code-block:: pycon

       >>> rgb_percent_to_hex(('100%', '100%', '0%'))
       '#ffff00'
       >>> rgb_percent_to_hex(('0%', '0%', '50%'))
       '#000080'
       >>> rgb_percent_to_hex(('85.49%', '64.71%', '12.5%'))
       '#daa520'

   :param rgb_percent_triplet: The `rgb()` triplet.
   :type rgb_percent_triplet: typing.Union[PercentRGB, Tuple[str, str, str]]
   :rtype: `str`

.. function:: rgb_percent_to_rgb(rgb_percent_triplet)

   Convert a 3-:class:`tuple` of percentages, suitable for use in an `rgb()`
   color triplet, to a 3-:class:`tuple` of :class:`int` suitable for use in
   representing that color.

   Some precision may be lost in this conversion. See the note
   regarding precision for :func:`~webcolors.rgb_to_rgb_percent` for
   details.

   Examples:
   
   .. code-block:: pycon

       >>> rgb_percent_to_rgb(('100%', '100%', '100%'))
       IntegerRGB(red=255, green=255, blue=255)
       >>> rgb_percent_to_rgb(('0%', '0%', '50%'))
       IntegerRGB(red=0, green=0, blue=128)
       >>> rgb_percent_to_rgb(('85.49%', '64.71%', '12.5%'))
       IntegerRGB(red=218, green=165, blue=32)

   :param rgb_percent_triplet: The `rgb()` triplet.
   :type rgb_percent_triplet: typing.Union[PercentRGB, Tuple[str, str, str]]
   :rtype: IntegerRGB


.. _html5-algorithms:

HTML5 color algorithms
----------------------

.. warning:: There are two versions of the HTML5 standard. Although
   they have common origins and are extremely similar, one is a living
   document (maintained by WHATWG) and the other is a W3C
   Recommendation. The functions documented below implement the HTML5
   color algorithms as given in `section 2.4.6 of the W3C HTML5
   Recommendation
   <http://www.w3.org/TR/html5/infrastructure.html#colors>`_.

.. function:: html5_parse_simple_color(input)

   Apply the HTML5 simple color parsing algorithm.

   Examples:
   
   .. code-block:: pycon

       >>> html5_parse_simple_color('#ffffff')
       HTML5SimpleColor(red=255, green=255, blue=255)
       >>> html5_parse_simple_color('#fff')
       Traceback (most recent call last):
           ...
       ValueError: An HTML5 simple color must be a string exactly seven characters long.

   :param input: The color to parse.
   :type input: :class:`str`, which must consist of exactly
       the character '#' followed by six hexadecimal digits
   :rtype: HTML5SimpleColor
   :raises ValueError: when the given input is not a Unicode string of
      length 7, consisting of exactly the character `#` followed by
      six hexadecimal digits.


.. function:: html5_serialize_simple_color(simple_color)

   Apply the HTML5 simple color serialization algorithm.

   Examples:
   
   .. code-block:: pycon

       >>> html5_serialize_simple_color((0, 0, 0))
       '#000000'
       >>> html5_serialize_simple_color((255, 255, 255))
       '#ffffff'

   :param simple_color: The color to serialize.
   :type simple_color: typing.Union[IntegerRGB, HTML5SimpleColor,
      Tuple[int, int, int]], all values in the range 0..255 inclusive
   :rtype: A valid lowercase simple color, which is a Unicode string
      exactly seven characters long, beginning with `#` and followed
      by six lowercase hexadecimal digits.


.. function:: html5_parse_legacy_color(input)

   Apply the HTML5 legacy color parsing algorithm.

   Note that, since this algorithm is intended to handle many types of
   malformed color values present in real-world Web documents, it is
   *extremely* forgiving of input, but the results of parsing inputs
   with high levels of "junk" (i.e., text other than a color value)
   may be surprising.

   Examples:
   
   .. code-block:: pycon

       >>> html5_parse_legacy_color('black')
       HTML5SimpleColor(red=0, green=0, blue=0)
       >>> html5_parse_legacy_color('chucknorris')
       HTML5SimpleColor(red=192, green=0, blue=0)
       >>> html5_parse_legacy_color('Window')
       HTML5SimpleColor(red=0, green=13, blue=0)

   :param input: The color to parse.
   :type input: :class:`str`
   :rtype: HTML5SimpleColor
   :raises ValueError: when the given input is not a Unicode string,
      or when it is precisely the string `'transparent'`.