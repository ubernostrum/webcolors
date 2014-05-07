.. module:: webcolors

.. _contents:


Module contents
===============

The contents of the ``webcolors`` module fall into three categories:

1. Constants which provide mappings between color names and values.

2. Normalization functions which sanitize input in various formats
   prior to conversion or output.

3. Conversion functions between each method of specifying colors.

All conversion functions which involve color names take an optional
argument to determine which specification to draw color names
from. See :ref:`the list of specification identifiers
<spec-identifiers>` for a list of valid values.

All conversion functions, when faced with identifiably invalid
hexadecimal color values, or with a request to name a color which has
no name in the requested specification, or with an invalid
specification identifier, will raise ``ValueError``.


Constants
---------

The following constants are available for direct use in mapping from
color names to values, although it is strongly recommended to use one
of the normalizing conversion functions instead.


Mappings from names to hexadecimal values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. data:: HTML4_NAMES_TO_HEX

   A dictionary whose keys are the normalized names of the sixteen
   named HTML 4 colors, and whose values are the normalized
   hexadecimal values of those colors.

.. data:: CSS2_NAMES_TO_HEX

   An alias for :data:`~webcolors.HTML4_NAMES_TO_HEX`, as CSS 2
   defined the same set of colors.

.. data:: CSS21_NAMES_TO_HEX

   A dictionary whose keys are the normalized names of the seventeen
   named CSS 2.1 colors, and whose values are the normalized
   hexadecimal values of those colors (sixteen of these are identical
   to HTML 4 and CSS 2; the seventeenth color is ``orange``, added in
   CSS 2.1).

.. data:: CSS3_NAMES_TO_HEX

   A dictionary whose keys are the normalized names of the 147 named
   CSS 3 colors, and whose values are the normalized hexadecimal
   values of those colors. These colors are also identical to the 147
   named colors of SVG.


Mappings from hexadecimal values to names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. data:: HTML4_HEX_TO_NAMES

   A dictionary whose keys are the normalized hexadecimal values of
   the sixteen named HTML 4 colors, and whose values are the
   corresponding normalized names.

.. data:: CSS2_HEX_TO_NAMES

   An alias for :data:`~webcolors.HTML4_HEX_TO_NAMES`.

.. data:: CSS21_HEX_TO_NAMES

   A dictionary whose keys are the normalized hexadecimal values of
   the seventeen named CSS 2.1 colors, and whose values are the
   corresponding normalized names.

.. data:: CSS3_HEX_TO_NAMES

   A dictionary whose keys are the normalized hexadecimal values of
   the 147 names CSS 3 colors, and whose values are the corresponding
   normalized names.

The canonical names of these constants are as listed above, entirely
in uppercase. For backwards compatibility with older versions of these
modules, aliases are provided whose names are entirely lowercase (for
example, ``html4_names_to_hex``).


Normalization functions
-----------------------

.. function:: normalize_hex(hex_value)

   Normalize a hexadecimal color value to a string consisting of a
   hash mark ("#") followed by six lowercase hexadecimal digits (what
   HTML5 terms a "valid lowercase simple color").

   If the supplied value cannot be interpreted as a hexadecimal color
   value, ``ValueError`` is raised. See :ref:`the conventions used by
   this module <conventions>` for information on acceptable formats
   for hexadecimal values.

   Examples::

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

   :param hex_value: The hexadecimal color value to normalize.
   :type hex_value: str
   :rtype: str

.. function:: normalize_integer_triplet(rgb_triplet)

    Normalize an integer ``rgb()`` triplet so that all values are
    within the range 0-255 inclusive.

    Examples::

        >>> normalize_integer_triplet((128, 128, 128))
        (128, 128, 128)
        >>> normalize_integer_triplet((0, 0, 0))
        (0, 0, 0)
        >>> normalize_integer_triplet((255, 255, 255))
        (255, 255, 255)
        >>> normalize_integer_triplet((270, -20, -0))
        (255, 0, 0)
    
    :param rgb_triplet: The integer ``rgb()`` triplet to normalize.
    :type rgb_triplet: 3-tuple of ``int``
    :rtype: 3-tuple of ``int``

.. function:: normalize_percent_triplet(rgb_triplet)

    Normalize a percentage ``rgb()`` triplet to that all values are
    within the range 0%-100% inclusive.

    Examples::

        >>> normalize_percent_triplet(('50%', '50%', '50%'))
        ('50%', '50%', '50%')
        >>> normalize_percent_triplet(('0%', '100%', '0%'))
        ('0%', '100%', '0%')
        >>> normalize_percent_triplet(('-10%', '-0%', '500%'))
        ('0%', '0%', '100%')
    
    :param rgb_triplet: The percentage ``rgb()`` triplet to normalize.
    :type rgb_triplet: 3-tuple of ``str``
    :rtype: 3-tuple of ``str``


Conversions from color names to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: name_to_hex(name, spec='css3')

   Convert a color name to a normalized hexadecimal color value.

   The color name will be normalized to lower-case before being looked
   up.

   Examples::

       >>> name_to_hex('white')
       '#ffffff'
       >>> name_to_hex('navy')
       '#000080'
       >>> name_to_hex('goldenrod')
       '#daa520'
       >>> name_to_hex('goldenrod', spec='html4')
       Traceback (most recent call last):
           ...
       ValueError: 'goldenrod' is not defined as a named color in html4.

   :param name: The color name to convert.
   :type name: ``str``
   :param spec: The specification from which to draw the list of color
      names; valid values are ``'html4'``, ``'css2'``, ``'css21'`` and
      ``'css3'``. Default is ``'css3'``.
   :type spec: ``str``
   :rtype: ``str``

.. function:: name_to_rgb(name, spec='css3')

   Convert a color name to a 3-tuple of integers suitable for use in
   an ``rgb()`` triplet specifying that color.

   The color name will be normalized to lower-case before being looked
   up.

   Examples::

       >>> name_to_rgb('white')
       (255, 255, 255)
       >>> name_to_rgb('navy')
       (0, 0, 128)
       >>> name_to_rgb('goldenrod')
       (218, 165, 32)

   :param name: The color name to convert.
   :type name: ``str``
   :param spec: The specification from which to draw the list of color
      names; valid values are ``'html4'``, ``'css2'``, ``'css21'`` and
      ``'css3'``. Default is ``'css3'``.
   :type spec: ``str``
   :rtype: 3-tuple of ``int``

.. function:: name_to_rgb_percent(name, spec='css3')

   Convert a color name to a 3-tuple of percentages (as strings)
   suitable for use in an ``rgb()`` triplet specifying that color.

   The color name will be normalized to lower-case before being looked
   up.

   Examples::

       >>> name_to_rgb_percent('white')
       ('100%', '100%', '100%')
       >>> name_to_rgb_percent('navy')
       ('0%', '0%', '50%')
       >>> name_to_rgb_percent('goldenrod')
       ('85.49%', '64.71%', '12.5%')

   :param name: The color name to convert.
   :type name: ``str``
   :param spec: The specification from which to draw the list of color
      names; valid values are ``'html4'``, ``'css2'``, ``'css21'`` and
      ``'css3'``. Default is ``'css3'``.
   :type spec: ``str``
   :rtype: 3-tuple of ``str``


Conversion from hexadecimal color values to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: hex_to_name(hex_value, spec='css3')

   Convert a hexadecimal color value to its corresponding normalized
   color name, if any such name exists.

   The hexadecimal value will be normalized before being looked up.

   Examples::

       >>> hex_to_name('#ffffff')
       'white'
       >>> hex_to_name('#fff')
       'white'
       >>> hex_to_name('#000080')
       'navy'
       >>> hex_to_name('#daa520')
       'goldenrod'
       >>> hex_to_name('#daa520', spec='html4')
       Traceback (most recent call last):
           ...
       ValueError: '#daa520' has no defined color name in html4.

   :param hex_value: The hexadecimal color value to convert.
   :type hex_value: str
   :param spec: The specification from which to draw the list of color
      names; valid values are ``'html4'``, ``'css2'``, ``'css21'`` and
      ``'css3'``. Default is ``'css3'``.
   :type spec: ``str``
   :rtype: ``str``

.. function:: hex_to_rgb(hex_value)

   Convert a hexadecimal color value to a 3-tuple of integers suitable
   for use in an ``rgb()`` triplet specifying that color.

   The hexadecimal value will be normalized before being converted.

   Examples::

       >>> hex_to_rgb('#fff')
       (255, 255, 255)
       >>> hex_to_rgb('#000080')
       (0, 0, 128)

   :param hex_value: The hexadecimal color value to convert.
   :type hex_value: ``str``
   :rtype: 3-tuple of ``int``

.. function:: hex_to_rgb_percent(hex_value)

   Convert a hexadecimal color value to a 3-tuple of percentages (as
   strings) suitable for use in an ``rgb()`` triplet representing that
   color.

   The hexadecimal value will be normalized before being converted.

   Examples::

       >>> hex_to_rgb_percent('#ffffff')
       ('100%', '100%', '100%')
       >>> hex_to_rgb_percent('#000080')
       ('0%', '0%', '50%')

   :param hex_value: The hexadecimal color value to convert.
   :type hex_value: ``str``
   :rtype: 3-tuple of ``str``


Conversions from integer ``rgb()`` triplets to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: rgb_to_name(rgb_triplet, spec='css3')

   Convert a 3-tuple of integers, suitable for use in an ``rgb()``
   color triplet, to its corresponding normalized color name, if any
   such name exists.

   To determine the name, the triplet will be converted to a
   normalized hexadecimal value.

   Examples::

       >>> rgb_to_name((255, 255, 255))
       'white'
       >>> rgb_to_name((0, 0, 128))
       'navy'

   :param rgb_triplet: The ``rgb()`` triplet
   :type rgb_triplet: 3-tuple of ``int``
   :param spec: The specification from which to draw the list of color
      names; valid values are ``'html4'``, ``'css2'``, ``'css21'`` and
      ``'css3'``. Default is ``'css3'``.
   :type spec: ``str``
   :rtype: ``str``

.. function:: rgb_to_hex(rgb_triplet)

   Convert a 3-tuple of integers, suitable for use in an ``rgb()``
   color triplet, to a normalized hexadecimal value for that color.

   Examples::

       >>> rgb_to_hex((255, 255, 255))
       '#ffffff'
       >>> rgb_to_hex((0, 0, 128))
       '#000080'

   :param rgb_triplet: The ``rgb()`` triplet.
   :type rgb_triplet: 3-tuple of ``int``
   :rtype: ``str``

.. function:: rgb_to_rgb_percent(rgb_triplet)

   Convert a 3-tuple of integers, suitable for use in an ``rgb()``
   color triplet, to a 3-tuple of percentages (as strings) suitable
   for use in representing that color.

   This function makes some trade-offs in terms of the accuracy of the
   final representation; for some common integer values, special-case
   logic is used to ensure a precise result (e.g., integer 128 will
   always convert to '50%', integer 32 will always convert to
   '12.5%'), but for all other values a standard Python ``float`` is
   used and rounded to two decimal places, which may result in a loss
   of precision for some values.

   Examples::

       >>> rgb_to_rgb_percent((255, 255, 255))
       ('100%', '100%', '100%')
       >>> rgb_to_rgb_percent((0, 0, 128))
       ('0%', '0%', '50%')
       >>> rgb_to_rgb_percent((218, 165, 32))
       ('85.49%', '64.71%', '12.5%')

   :param rgb_triplet: The ``rgb()`` triplet.
   :type rgb_triplet: 3-tuple of ``int``
   :rtype: 3-tuple of ``str``


Conversions from percentage ``rgb()`` triplets to other formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. function:: rgb_percent_to_name(rgb_percent_triplet, spec='css3')

   Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
   color triplet, to its corresponding normalized color name, if any
   such name exists.

   To determine the name, the triplet will be converted to a
   normalized hexadecimal value.

   Examples::

       >>> rgb_percent_to_name(('100%', '100%', '100%'))
       'white'
       >>> rgb_percent_to_name(('0%', '0%', '50%'))
       'navy'
       >>> rgb_percent_to_name(('85.49%', '64.71%', '12.5%'))
       'goldenrod'

   :param rgb_percent_triplet: The ``rgb()`` triplet. 
   :type rgb_percent_triplet: 3-tuple of ``str``
   :param spec: The specification from which to draw the list of color
       names; valid values are ``'html4'``, ``'css2'``, ``'css21'``
       and ``'css3'``. Default is ``'css3'``.
   :type spec: ``str``
   :rtype: ``str``

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

   :param rgb_percent_triplet: The ``rgb()`` triplet.
   :type rgb_percent_triplet: 3-tuple of ``str``
   :rtype: ``str``

.. function:: rgb_percent_to_rgb(rgb_percent_triplet)

   Convert a 3-tuple of percentages, suitable for use in an ``rgb()``
   color triplet, to a 3-tuple of integers suitable for use in
   representing that color.

   Some precision may be lost in this conversion. See the note
   regarding precision for :func:`~webcolors.rgb_to_rgb_percent` for
   details.

   Examples::

       >>> rgb_percent_to_rgb(('100%', '100%', '100%'))
       (255, 255, 255)
       >>> rgb_percent_to_rgb(('0%', '0%', '50%'))
       (0, 0, 128)
       >>> rgb_percent_to_rgb(('85.49%', '64.71%', '12.5%'))
       (218, 165, 32)

   :param rgb_percent_triplet: The ``rgb()`` triplet.
   :type rgb_percent_triplet: 3-tuple of ``str``
   :rtype: 3-tuple of ``int``
