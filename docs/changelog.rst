.. _changelog:


Change log
==========

This document lists the changes between each release of webcolors.


Version 1.11.1, released 2020-02-17
-----------------------------------

Bugs fixed
~~~~~~~~~~

* Corrected an error regarding supported Python versions in the
  README file.


Version 1.11, released 2020-02-17
---------------------------------

No bug fixes or new features.

Other changes
~~~~~~~~~~~~~

* Python 2 has reached the end of its support cycle from the Python
  core team; accordingly, Python 2 support is dropped. Supported
  Python versions are now 3.5, 3.6, 3.7, and 3.8.


Version 1.10, released 2019-09-08
---------------------------------

No bug fixes or new features.

Other changes
~~~~~~~~~~~~~

* Similar to the change in version 1.9 which normalized conversions to
  named colors for `gray`/`grey` to always use the `gray` variant, the
  other named grays of CSS3 now normalize to the `gray` spelling. This
  affects the following colors: `darkgray`/`darkgrey`,
  `darkslategray`/`darkslategrey`, `dimgray`/`dimgrey`,
  `lightgray`/`lightgrey`, `lightslategray`/`lightslategrey`,
  `slategray`/`slategrey`.


Version 1.9.1, released 2019-06-07
----------------------------------

Bugs fixed
~~~~~~~~~~

* The `__version__` attribute of the installed webcolors module,
  although not documented or referenced anywhere, was accidentally not
  updated in the 1.9 release. It has now been updated (and now
  indicates 1.9.1).


Version 1.9, released 2019-06-01
--------------------------------

No bug fixes.

New features
~~~~~~~~~~~~

* Added :ref:`a set of constants to use when referring to
  specifications that define color names <spec-constants>`.

Other changes
~~~~~~~~~~~~~

* When asked to provide a color name, using the CSS3/SVG set of names,
  for the hexadecimal value `#808080`, the integer triplet `rgb(128,
  128, 128)`, or the percentage triplet `rgb(50%, 50%, 50%)`,
  webcolors now always returns `u'gray'`, never `u'grey'`. Previously,
  the behavior could be inconsistent as it depended on the Python
  version in use; `u'gray'` was picked because it was the spelling
  variant used in HTML 4, CSS1, and CSS2.


Version 1.8.1, released 2018-02-12
----------------------------------

The 1.8.1 release is a repackaging of 1.8 to produce both source
(.tar.gz) and binary (.whl) package formats, following reports that
the source-package-only release of 1.8 was causing installation issues
for some users. See `issue 6 in the repository
<https://github.com/ubernostrum/webcolors/issues/6>`_ for details.


Version 1.8, released 2018-02-08
--------------------------------

No bug fixes.

New features
~~~~~~~~~~~~

* Added the :class:`~webcolors.IntegerRGB`,
  :class:`~webcolors.PercentRGB`, and
  :class:`~webcolors.HTML5SimpleColor` named tuples.

Other changes
~~~~~~~~~~~~~

* Drop support for Python 3.3 (Python core team no longer maintains
  3.3).

* Mark support for Python 3.6.

* :ref:`The full verification tests <full-verification>` now run
  correctly on Python 3.


Version 1.7, released 2016-11-25
--------------------------------

No new features or bugfixes.

Other changes
~~~~~~~~~~~~~

* Drop support for Python 2.6 (Python core team no longer maintains
  2.6).

* Mark support for Python 3.4.

* On Python 3, the use of :class:`str` for all functions which take
  string arguments is now mandatory. Attempted use of :class:`bytes`
  will raise an exception. On Python 2, use of bytestrings is still
  permitted.


Version 1.5.1, released 2015-11-23
----------------------------------

No new features.

Bug fixes
~~~~~~~~~

* Corrected multiple typos in documentation.



Version 1.5, released 2015-03-07
--------------------------------

No bug fixes.


New features
~~~~~~~~~~~~

* Python 3 support: webcolors now supports Python 3.3.

* Added :ref:`HTML5 color algorithms <html5-algorithms>`.

Other changes
~~~~~~~~~~~~~

* Packaging improvements.


Version 1.4, released 2012-02-10
--------------------------------

No new features.

Bugs fixed
~~~~~~~~~~

* Integer and percentage `rgb()` triplets now normalized in accordance
  with CSS clipping rules.

Other changes
~~~~~~~~~~~~~

* Packaging fixes.

* Preparatory work for Python 3 support.


Version 1.3.1, released 2009-10-24
----------------------------------

No new features or bugfixes.

Other changes
~~~~~~~~~~~~~

* Documentation expanded.

* Documentation now maintained using `Sphinx
  <http://www.sphinx-doc.org/>`_.


Version 1.3, released 2009-05-08
--------------------------------

No new features or bugfixes.

Other changes
~~~~~~~~~~~~~

* Documentation expanded.


Version 1.2, 2009-03-01
-----------------------

Bugs fixed:
~~~~~~~~~~~

* Corrected the download URL in the `setup.py` script.


Version 1.1, released 2008-12-19
--------------------------------

No new features or bugfixes.

Other changes
~~~~~~~~~~~~~

* Documentation expanded.


Version 1.0, released 2008-10-28
--------------------------------

Initial stable release of webcolors.
