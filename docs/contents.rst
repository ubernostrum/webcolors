.. module:: webcolors

.. _contents:


Module contents
===============

The contents of the webcolors module fall into five categories:

1. A set of (optional) data types for representing color values.

2. Constants for several purposes.

3. Normalization functions which sanitize input in various formats prior to
   conversion or output.

4. Conversion functions between each method of specifying colors.

5. Implementations of the color parsing and serialization algorithms in HTML5.

See :ref:`the documentation regarding conventions <conventions>` for
information regarding the types and representation of various color formats in
webcolors.

All conversion functions which involve color names take an optional argument to
determine the specification from which to draw color names. See :ref:`the set
of specification identifiers <spec-constants>` for valid values.

All conversion functions, when faced with identifiably invalid hexadecimal
color values, or with a request to name a color which has no name in the
requested specification, or with an invalid specification identifier, will
raise :exc:`ValueError`.

.. admonition:: **Imports and submodules**

   The public, supported API of webcolors is exported from its top-level
   module, ``webcolors``. Although the codebase is internally organized into
   several submodules for easier maintenance, the existence, names, and
   organization of these submodules is *not* part of webcolors' public API and
   cannot be relied upon.

   For example: although :func:`normalize_hex` is actually implemented
   in a submodule named ``webcolors.normalization``, it must always be
   referred to as ``webcolors.normalize_hex``, **never** as
   ``webcolors.normalization.normalize_hex``.


Data types
----------

Integer and percentage ``rgb()`` triplets, and HTML5 simple colors, can be
passed to functions in webcolors as plain 3-:class:`tuple` of the appropriate
data type. But the following :class:`~typing.NamedTuple` instances are also
provided to represent these types more richly, and functions in webcolors which
return triplets or simple colors will return instances of these:

.. autoclass:: IntegerRGB
.. autoclass:: PercentRGB
.. autoclass:: HTML5SimpleColor

Additionally, to aid in type annotations, the following type aliases are
defined, and used throughout this module:

.. autodata:: IntTuple
.. autodata:: PercentTuple

Constants
---------

Several sets of constants are provided in webcolors, for use when converting or
identifying colors or specifications.

.. _spec-constants:

Specification identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following constants are available for indicating the specification from
which to draw color name choices, in functions which can work with multiple
specifications.

.. data:: CSS2

   Represents the CSS2 specification. Value is ``"css2"``.

.. data:: CSS21

   Represents the CSS2.1 specification. Value is ``"css21"``.

.. data:: CSS3

   Represents the CSS3 specification. Value is ``"css3"``.

.. data:: HTML4

   Represents the HTML 4 specification. Value is ``"html4"``.


.. _mapping-constants:

Color mappings
~~~~~~~~~~~~~~

The following constants are available for direct use in mapping from color
names to values, although it is strongly recommended to use one of the
normalizing conversion functions instead.


Mappings from names to hexadecimal values
+++++++++++++++++++++++++++++++++++++++++

.. data:: HTML4_NAMES_TO_HEX

   A :class:`dict` whose keys are the normalized names of the sixteen named
   HTML 4 colors, and whose values are the normalized hexadecimal values of
   those colors.

.. data:: CSS2_NAMES_TO_HEX

   An alias for :data:`~webcolors.HTML4_NAMES_TO_HEX`, as CSS2 defined the same
   set of colors.

.. data:: CSS21_NAMES_TO_HEX

   A :class:`dict` whose keys are the normalized names of the seventeen named
   CSS2.1 colors, and whose values are the normalized hexadecimal values of
   those colors (sixteen of these are identical to HTML 4 and CSS2; the
   seventeenth color is ``"orange"``, added in CSS2.1).

.. data:: CSS3_NAMES_TO_HEX

   A :class:`dict` whose keys are the normalized names of the 147 named CSS3
   colors, and whose values are the normalized hexadecimal values of those
   colors. These colors are also identical to the 147 named colors of SVG.


Mappings from hexadecimal values to names
+++++++++++++++++++++++++++++++++++++++++

.. data:: HTML4_HEX_TO_NAMES

   A :class:`dict` whose keys are the normalized hexadecimal values of the
   sixteen named HTML 4 colors, and whose values are the corresponding
   normalized names.

.. data:: CSS2_HEX_TO_NAMES

   An alias for :data:`~webcolors.HTML4_HEX_TO_NAMES`, as CSS2 defined the same
   set of colors.

.. data:: CSS21_HEX_TO_NAMES

   A :class:`dict` whose keys are the normalized hexadecimal values of the
   seventeen named CSS2.1 colors, and whose values are the corresponding
   normalized names (sixteen of these are identical to HTML 4 and CSS2; the
   seventeenth color is ``"orange"``, added in CSS2.1).

.. data:: CSS3_HEX_TO_NAMES

   A :class:`dict` whose keys are the normalized hexadecimal values of the 147
   named CSS3 colors, and whose values are the corresponding normalized
   names. These colors are also identical to the 147 named colors of SVG.

   .. note:: **Spelling variants**

      Some values representing named gray colors can map to either of two names
      in CSS3, because it supports both ``"gray"`` and ``"grey"`` spelling
      variants for those colors. This mapping will always return the variant
      spelled ``"gray"`` (such as ``"lightgray"`` instead of
      ``"lightgrey"``). See :ref:`the documentation on name conventions
      <color-name-conventions>` for details.


Normalization functions
-----------------------

.. autofunction:: normalize_hex
.. autofunction:: normalize_integer_triplet
.. autofunction:: normalize_percent_triplet


Conversions from color names to other formats
---------------------------------------------

.. autofunction:: name_to_hex
.. autofunction:: name_to_rgb
.. autofunction:: name_to_rgb_percent


Conversions from hexadecimal color values to other formats
----------------------------------------------------------

.. autofunction:: hex_to_name
.. autofunction:: hex_to_rgb
.. autofunction:: hex_to_rgb_percent


Conversions from integer `rgb()` triplets to other formats
------------------------------------------------------------

.. autofunction:: rgb_to_name
.. autofunction:: rgb_to_hex
.. autofunction:: rgb_to_rgb_percent


Conversions from percentage `rgb()` triplets to other formats
---------------------------------------------------------------

.. autofunction:: rgb_percent_to_name
.. autofunction:: rgb_percent_to_hex
.. autofunction:: rgb_percent_to_rgb


.. _html5-algorithms:

HTML5 color algorithms
----------------------

.. warning:: Previously there were two competing HTML5 standards: one from
   WHATWG, and one from W3C. The WHATWG version is now the sole official HTML5
   standard, and so the functions documented below implement the HTML5 color
   algorithms as given in `section 2.3.6 of the WHATWG HTML5 standard
   <https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#colours>`_.

.. autofunction:: html5_parse_simple_color
.. autofunction:: html5_serialize_simple_color
.. autofunction:: html5_parse_legacy_color
