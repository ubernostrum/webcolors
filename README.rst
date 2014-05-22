``webcolors`` is a simple Python module for working with HTML/CSS
colors.

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
    >>> webcolors.hex_to_name('#daa520')
    'goldenrod'

