webcolors
=========

This module provides utility functions for working with the color
names and color value formats defined by the HTML and CSS
specifications for use in documents on the Web.

Support is included for normalizing and converting between the
following formats (RGB colorspace only; conversion to/from HSL can be
handled by the ``colorsys`` module in the Python standard library):

* Specification-defined color names

* Six-digit hexadecimal

* Three-digit hexadecimal

* Integer ``rgb()`` triplet

* Percentage ``rgb()`` triplet

For example::

    >>> import webcolors
    >>> webcolors.hex_to_name(u'#daa520')
    u'goldenrod'

Implementations are also provided for the HTML5 color parsing and
serialization algorithms. For example, parsing the infamous
"chucknorris" string into an rgb() triplet::

    >>> import webcolors
    >>> webcolors.html5_parse_legacy_color(u'chucknorris')
    HTML5SimpleColor(red=192, blue=0, green=0)


Documentation contents
----------------------

.. toctree::
   :maxdepth: 1

   install
   colors
   conventions
   contents
   conformance
   faq

.. seealso::

  * `The sRGB color space <http://www.w3.org/Graphics/Color/sRGB>`_
  * `HTML 4: Colors <http://www.w3.org/TR/html401/types.html#h-6.5>`_
  * `CSS 1: Color units <http://www.w3.org/TR/CSS1/#color-units>`_
  * `CSS 2: Colors <http://www.w3.org/TR/CSS2/syndata.html#color-units>`_
  * `CSS 3 color module <http://www.w3.org/TR/css3-color/>`_
  * `HTML5: Colors <http://www.w3.org/TR/html5/infrastructure.html#colors>`_