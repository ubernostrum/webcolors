.. _faq:

Frequently asked questions
==========================

The following notes answer common questions, and may be useful to you
when using webcolors.


What versions of Python are supported?
--------------------------------------

The webcolors module supports and is tested on Python 3.5, 3.6, 3.7,
and 3.8. As of the release of webcolors |release|, these are the only
versions of Python receiving upstream security support from the Python
core team.


How closely does this module follow the standards?
--------------------------------------------------

As closely as is practical (see below regarding floating-point
values), within :ref:`the supported formats <support>`; the
webcolors module was written with the relevant standards documents
close at hand. See :ref:`the conformance documentation <conformance>`
for details.


Why aren't `rgb_to_rgb_percent()` and `rgb_percent_to_rgb()` precise?
-------------------------------------------------------------------------

This is due to limitations in the representation of floating-point
numbers in programming languages. Python, like many programming
languages, uses `IEEE floating-point
<https://en.wikipedia.org/wiki/IEEE_754>`_, which is inherently
imprecise for some values. This imprecision only appears when
converting between integer and percentage `rgb()` triplets, as in
:func:`~webcolors.rgb_to_rgb_percent` and
:func:`~webcolors.rgb_percent_to_rgb`.

To work around this, some common values (255, 128, 64, 32, 16 and 0)
are handled as special cases, with hard-coded precise results. For all
other values, conversion to percentage `rgb()` triplet uses a standard
Python :class:`float`, rounding the result to two decimal places.

See :ref:`the conformance documentation <conformance>` for details on
how this affects testing.


Why does webcolors prefer American spellings?
---------------------------------------------

In CSS3, several color names are defined multiple times with identical
values, to support both American and British spelling variants for
`gray`/`grey`. These colors are: `darkgray`/`darkgrey`,
`darkslategray`/`darkslategrey`, `dimgray`/`dimgrey`, `gray`/`grey`,
`lightgray`/`lightgrey`, `lightslategray`/`lightslategrey`,
`slategray`/`slategrey`.

Using any of the conversions from names to other formats
(:func:`~webcolors.name_to_hex`, :func:`~webcolors.name_to_rgb`, or
:func:`~webcolors.name_to_rgb_percent`) will accept either spelling
provided the `spec` argument is :data:`~webcolors.CSS3`.

However, converting from other formats to a name requires picking one
of these spellings. Since webcolors uses a Python :class:`dict` to
store its :ref:`name-to-value mappings <mapping-constants>`, simply
reversing those mappings risks inconsistency: swapping the keys and
values of a :class:`dict` in Python depends on the key order, which
varies from one version of Python to another and in several supported
Python versions is not guaranteed to be consistent and/or is
documented as an implementation detail not to be relied on. So
webcolors must manually pick a spelling to normalize to, and chooses
`gray`. This choice was made for consistency with HTML 4, CSS1, and
CSS2, each of which only allowed `gray`.


Why aren't HSL values supported?
--------------------------------

In the author's experience, actual use of HSL values on the Web is
extremely rare; the overwhelming majority of all colors used on the
Web are specified using sRGB, through hexadecimal color values or
through integer or percentage `rgb()` triplets. This decreases the
importance of supporting the `hsl()` construct.

Additionally, Python already has the :mod:`colorsys` module in the
standard library, which offers functions for converting between RGB,
HSL, HSV and YIQ color systems. If you need conversion to/from HSL or
another color system, use :mod:`colorsys`.


Why not use a more object-oriented design with classes for the colors?
----------------------------------------------------------------------

Representing color values with Python classes would introduce overhead
for no real gain. Real-world use cases tend to involve working
directly with the actual values, so settling on conventions for how to
represent them as Python types, and then offering a function-based
interface, accomplishes everything needed without the additional
indirection layer of having to instantiate and serialize a
color-wrapping object.

Keeping a function-based interface also maintains consistency with
Python's built-in :mod:`colorsys` module which has the same style of
interface for converting amongst color spaces.

Note that if an object-oriented interface is desired, `the third-party
colormath module <https://pypi.org/project/colormath/>`_ does have a
class-based interface (and rightly so, as it offers a wider range of
color representation and manipulation options than webcolors).


How am I allowed to use this module?
------------------------------------

The webcolors module is distributed under a `three-clause BSD
license <http://opensource.org/licenses/BSD-3-Clause>`_. This is an
open-source license which grants you broad freedom to use,
redistribute, modify and distribute modified versions of
webcolors. For details, see the file `LICENSE` in the source
distribution of webcolors.

.. _three-clause BSD license: http://opensource.org/licenses/BSD-3-Clause


I found a bug or want to make an improvement!
---------------------------------------------

The canonical development repository for webcolors is online at
<https://github.com/ubernostrum/webcolors>. Issues and pull requests
can both be filed there.

