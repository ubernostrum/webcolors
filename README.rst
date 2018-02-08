.. -*-restructuredtext-*-

.. image:: https://travis-ci.org/ubernostrum/webcolors.svg?branch=master
    :target: https://travis-ci.org/ubernostrum/webcolors

``webcolors`` is a Python (2.7, 3.4+) module for working with HTML/CSS
color definitions.

Support is included for normalizing and converting between the
following formats (RGB colorspace only; conversion to/from HSL can be
handled by the ``colorsys`` module in the Python standard library):

* Specification-defined color names

* Six-digit hexadecimal

* Three-digit hexadecimal

* Integer ``rgb()`` triplet

* Percentage ``rgb()`` triplet

For example:

.. code-block:: python

    >>> import webcolors
    >>> webcolors.hex_to_name(u'#daa520')
    u'goldenrod'

Implementations are also provided for the HTML5 color parsing and
serialization algorithms. For example, parsing the infamous
"chucknorris" string into an rgb() triplet:

.. code-block:: python

    >>> import webcolors
    >>> webcolors.html5_parse_legacy_color(u'chucknorris')
    HTML5SimpleColor(192, 0, 0)

Full documentation is `available online <https://webcolors.readthedocs.io/>`_.
