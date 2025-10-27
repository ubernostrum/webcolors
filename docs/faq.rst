.. _faq:

Frequently asked questions
==========================

The following notes answer common questions, and may be useful to you when
using ``webcolors``.


General
-------

What versions of Python are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version |release| of ``webcolors`` supports and is tested on Python 3.10, 3.11,
3.12, 3.13, and 3.14.


How am I allowed to use this module?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``webcolors`` module is distributed under a `three-clause BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_. This is an open-source license
which grants you broad freedom to use, redistribute, modify and distribute
modified versions of ``webcolors``. For details, see the file ``LICENSE`` in
the source distribution of ``webcolors``.

.. _three-clause BSD license: http://opensource.org/licenses/BSD-3-Clause


I found a bug or want to make an improvement!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The canonical development repository for ``webcolors`` is online at
<https://github.com/ubernostrum/webcolors>. Issues and pull requests can both
be filed there.


How closely does this module follow the standards?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As closely as is practical (see below regarding floating-point values), within
:ref:`the supported formats <support>`; the ``webcolors`` module was written
with the relevant standards documents close at hand. See :ref:`the conformance
documentation <conformance>` for details.


Design choices and technical details
------------------------------------


Why not use a more object-oriented design with classes for the colors?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Representing color values with Python classes would introduce overhead for no
real gain. Real-world use cases tend to involve working directly with the
actual values, so settling on conventions for how to represent them as Python
types, and then offering a function-based interface, accomplishes everything
needed without the additional indirection layer of having to instantiate and
serialize a color-wrapping object.

Keeping a function-based interface also maintains consistency with Python's
built-in :mod:`colorsys` module which has the same style of interface for
converting amongst color spaces.

Note that if an object-oriented interface is desired, `the third-party
colormath module <https://pypi.org/project/colormath/>`_ does have a
class-based interface (and rightly so, as it offers a wider range of color
representation and manipulation options than ``webcolors``).


Why does ``webcolors`` prefer American spellings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In CSS3, several color names are defined multiple times with identical values,
to support both American and British spelling variants for
``"gray"``/``"grey"``. These colors are: ``"darkgray"``/``"darkgrey"``,
``"darkslategray"``/``"darkslategrey"``, ``"dimgray"``/``"dimgrey"``,
``"gray"``/``"grey"``, ``"lightgray"``/``"lightgrey"``,
``"lightslategray"``/``"lightslategrey"``, ``"slategray"``/``"slategrey"``.

Using any of the conversions from names to other formats
(:func:`~webcolors.name_to_hex`, :func:`~webcolors.name_to_rgb`, or
:func:`~webcolors.name_to_rgb_percent`) will accept either spelling provided
the `spec` argument is :data:`~webcolors.CSS3`.

However, converting from other formats to a name requires choosing which
spelling to return, and should return the same choice each time. So
``webcolors`` chooses the ``gray`` variants, for consistency with HTML 4, CSS1,
and CSS2, each of which only allowed `gray`.


Why aren't HSL values supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :mod:`colorsys` module in the standard library contains functions for
converting between RGB, HSL, HSV and YIQ color systems, so you can convert
integer RGB triplets from ``webcolors`` to HSL triplets, or vice-versa, using
:mod:`colorsys`, without ``webcolors`` needing to provide its own conversion
functions.


Why aren't ``rgb_to_rgb_percent()`` and ``rgb_percent_to_rgb()`` precise?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is due to limitations in the representation of floating-point numbers in
programming languages. Python, like many programming languages, uses `IEEE
floating-point <https://en.wikipedia.org/wiki/IEEE_754>`_, which is inherently
imprecise for some values. This imprecision only appears when converting
between integer and percentage ```rgb()``` triplets, as in
:func:`~webcolors.rgb_to_rgb_percent` and
:func:`~webcolors.rgb_percent_to_rgb`.

To work around this, some common values (255, 128, 64, 32, 16 and 0) are
handled as special cases, with hard-coded precise results. For all other
values, conversion to percentage ``rgb()`` triplet uses a standard Python
:class:`float`, rounding the result to two decimal places.

See :ref:`the conformance documentation <conformance>` for details on how this
affects testing.


Are alpha-channel constructs like ``rgba()`` supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While this decision may be re-evaluated in the future, ``webcolors`` currently
does *not* support constructs which carry alpha-channel information (the
``rgba()`` and ``hsla()`` constructs of CSS3, or the ``#rrggbbaa`` construct of
the CSS Colors Level 4 module).

There are two main reasons for this:

1. ``webcolors`` does not yet support the CSS Color Module Level 4 in any way,
   which means the only supported construct would be ``rgba()`` (since
   ``webcolors`` only handles RGB color constructs, not HSL), and there would
   be no other alpha-channel construct to convert to or from.

2. Once support for the CSS Color Module Level 4 is finalized, it's still not
   clear that converting between ``rgba()`` and ``#rrggbbaa`` constructs would
   be useful enough on its own to justify the support. Converting to
   non-alpha-channel constructs would not require specialized functions since
   the alpha-channel component could simply be sliced off, and converting
   _from_ non-alpha-channel constructs to alpha-channel constructs similarly
   does not seem to require additional functions -- the desired alpha-channel
   information could be appended onto a non-alpha-channel construct easily
   enough.
