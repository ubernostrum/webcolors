.. _faq:

Frequently asked questions
==========================

The following notes answer common questions, and may be useful to you
when using webcolors.


What versions of Python are supported?
--------------------------------------

On Python 2, webcolors supports and is tested on Python 2.7. On Python
3, webcolors supports and is tested on Python 3.4, 3.5, and 3.6.

These Python version requirements are due to a combination of factors:

* On Python 2, only 2.7 still receives official security support from
  Python's development team. Although some third parties continue to
  provide unofficial security support for earlier Python 2 versions,
  the fact remains that Python 2.6 and earlier have reached their
  official end-of-life and their use should not be encouraged.

* Python 3.4 is the oldest Python 3.x release still receiving upstream
  security support.


How closely does this module follow the standards?
--------------------------------------------------

As closely as is practical (see below regarding floating-point
values), within :ref:`the supported formats <support>`; the
webcolors module was written with the relevant standards documents
close at hand. See :ref:`the conformance documentation <conformance>`
for details.


Why aren't ``rgb_to_rgb_percent()`` and ``rgb_percent_to_rgb()`` precise?
-------------------------------------------------------------------------

This is due to limitations in the representation of floating-point
numbers in programming languages. Python, like many programming
languages, uses `IEEE floating-point
<http://en.wikipedia.org/wiki/IEEE_floating_point>`_, which is
inherently imprecise for some values. This imprecision only appears
when converting between integer and percentage ``rgb()`` triplets.

To work around this, some common values (255, 128, 64, 32, 16 and 0)
are handled as special cases, with hard-coded precise results. For all
other values, conversion to percentage ``rgb()`` triplet uses a
standard Python ``float``, rounding the result to two decimal places.

See :ref:`the conformance documentation <conformance>` for details on
how this affects testing.


Why aren't HSL values supported?
--------------------------------

In the author's experience, actual use of HSL values on the Web is
extremely rare; the overwhelming majority of all colors used on the
Web are specified using sRGB, through hexadecimal color values or
through integer or percentage ``rgb()`` triplets. This decreases the
importance of supporting the ``hsl()`` construct.

Additionally, Python already has `the colorsys module`_ in the
standard library, which offers functions for converting between RGB,
HSL, HSV and YIQ color systems. If you need conversion to/from HSL or
another color system, use ``colorsys``.

.. _the colorsys module: http://docs.python.org/library/colorsys.html


Why not use a more object-oriented design with classes for the colors?
----------------------------------------------------------------------

Representing color values with Python classes would introduce overhead
for no real gain. Real-world use cases tend to involve working
directly with the actual values, so settling on conventions for how to
represent them as Python types, and then offering a function-based
interface, accomplishes everything needed without the addtional
indirection layer of having to instantiate and serialize a
color-wrapping object.

Keeping a function-based interface also maintains consistency with
`Python's built-in colorsys module
<https://docs.python.org/library/colorsys.html>`_, which has the same
style of interface for converting amongst color spaces.

Note that if an object-oriented interface is desired, `the third-party
colormath module <https://pypi.python.org/pypi/colormath/>`_ does have
a class-based interface (and rightly so, as it offers a wider range of
color representation and manipulation options than webcolors).


How am I allowed to use this module?
------------------------------------

The webcolors module is distributed under a `three-clause BSD
license <http://opensource.org/licenses/BSD-3-Clause>`_. This is an
open-source license which grants you broad freedom to use,
redistribute, modify and distribute modified versions of
webcolors. For details, see the file ``LICENSE`` in the source
distribution of webcolors.

.. _three-clause BSD license: http://opensource.org/licenses/BSD-3-Clause


I found a bug or want to make an improvement!
---------------------------------------------

The canonical development repository for webcolors is online at
<https://github.com/ubernostrum/webcolors>. Issues and pull requests
can both be filed there.

