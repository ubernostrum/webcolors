.. _changelog:


Changelog
=========

This document lists the changes in each release of ``webcolors``.


Version numbering
-----------------

This library currently tracks its version numbers using the ``YY.MM.MICRO``
form of `Calendar Versioning <https://calver.org>`_ ("CalVer"), in which the
first two components of the version number are the (two-digit) year and
(non-zero-padded) month of the release date, while the third component is an
incrementing value for releases occurring in that month. For example, the first
release issued in January 2025 would have a version number of 25.1.0; a
subsequent release in the same month would be 25.1.1; a release the following
month (February) would be 25.2.0.

The CalVer system was adopted for this library in 2024, and the first release
to use a CalVer version number was 24.6.0.


API stability and deprecations
------------------------------

The API stability/deprecation policy for this library is as follows:

* The supported stable public API of this library is the set of symbols which
  are exported by its ``__all__`` declaration and which are documented in this
  documentation. For classes exported there, the supported stable public API is
  the set of methods and attributes of those classes whose names do not begin
  with one or more underscore (``_``) characters and which are documented in
  this documentation.

* When a public API is to be removed, or undergo a backwards-incompatible
  change, it will emit a deprecation warning which serves as notice of the
  intended removal or change, and which will give a date -- which will always
  be at least in the next calendar year after the first release which emits the
  deprecation warning -- past which the removal or change may occur without
  further warning.

* Security fixes, and fixes for high-severity bugs (such as those which might
  cause unrecoverable crash or data loss), are not required to emit deprecation
  warnings, and may -- if needed -- impose backwards-incompatible change in any
  release. If this occurs, this changelog document will contain a note
  explaining why the usual deprecation process could not be followed for that
  case.

* This policy is in effect as of the adoption of CalVer versioning, with
  version 24.6.0 of this library.


Releases under CalVer
---------------------

Version 25.10.0
~~~~~~~~~~~~~~~

Released October 2025

* Supported Python versions are now 3.10, 3.11, 3.12, 3.13, and 3.14.

* The package's tests now run with `pytest <https://pytest.org>`_.


Version 24.11.1
~~~~~~~~~~~~~~~

Released November 2024

* Correct an error with specifying the version in the 24.11.0 package. The
  version number of the package was accidentally defined in two places, and
  they were out of sync. The extra definition has been removed. The 24.11.0
  package has been yanked from PyPI to prevent problems.


Version 24.11.0
~~~~~~~~~~~~~~~

Released November 2024

* Supported Python versions are now 3.9, 3.10, 3.11, 3.12, and 3.13.


Version 24.8.0
~~~~~~~~~~~~~~

Released August 2024

* Added the :func:`~webcolors.names` function to allow retrieving lists of
  color names. The underlying mappings of color names/values still are not
  supported API; to obtain the color value corresponding to a name, use the
  appropriate conversion function.


Version 24.6.0
~~~~~~~~~~~~~~

Released June 2024

* Supported Python versions are now 3.8, 3.9, 3.10, and 3.12.

* Running the unit tests no longer uses a third-party test runner; the
  standard-library ``unittest`` module's runner is used instead.

* Documentation of the HTML5 color algorithms has been updated to emphasize
  which HTML5 spec is used (the WHATWG spec, which is now the only canonical
  and maintained HTML5 spec) and comments in the implementations have been
  updated to include the latest prose description of the HTML5 algorithms from
  the spec. These updates do not change the behavior of the HTML5 algorithms,
  and are only for clarity of documentation and explanation.

* Adopted `CalVer versioning <https://calver.org>`_.

* The raw mappings of color names/values are no longer publicly exposed; use
  the appropriate normalizing conversion functions instead of accessing the
  mappings directly.


Releases not under CalVer
-------------------------

Version 1.13
~~~~~~~~~~~~

Released March 2023

* Supported Python versions are now 3.7, 3.8, 3.9, 3.10, and 3.11.

* The codebase was significantly reorganized and modernized. Public API is
  unchanged. Imports should continue to be directly from the top-level
  ``webcolors`` module; attempting to import from submodules is not supported.

* Now packaging declaratively via ``pyproject.toml`` with `PEP 517
  <https://peps.python.org/pep-0517/>`_ support from ``setuptools``.


Version 1.12
~~~~~~~~~~~~

Released May 2022

* Supported Python versions are now 3.7, 3.8, 3.9, and 3.10.


Version 1.11.1
~~~~~~~~~~~~~~

Released February 2020

* Corrected an error regarding supported Python versions in the README file.


Version 1.11
~~~~~~~~~~~~

Released February 2020

* Python 2 has reached the end of its support cycle from the Python core team;
  accordingly, Python 2 support is dropped. Supported Python versions are now
  3.5, 3.6, 3.7, and 3.8.


Version 1.10
~~~~~~~~~~~~

Released September 2019

* Similar to the change in version 1.9 which normalized conversions to named
  colors for ``gray``/``grey`` to always use the ``gray`` variant, the other
  named grays of CSS3 now normalize to the ``gray`` spelling. This affects the
  following colors: ``darkgray``/``darkgrey``,
  ``darkslategray``/``darkslategrey``, ``dimgray``/``dimgrey``,
  ``lightgray``/``lightgrey``, ``lightslategray``/``lightslategrey``,
  ``slategray``/``slategrey``.


Version 1.9.1
~~~~~~~~~~~~~

Released June 2019

* The ``__version__`` attribute of the installed ``webcolors`` module, although
  not documented or referenced anywhere, was accidentally not updated in the
  1.9 release. It has now been updated (and now indicates 1.9.1).


Version 1.9
~~~~~~~~~~~

Released June 2019

* Added :ref:`a set of constants to use when referring to specifications that
  define color names <spec-constants>`.

* When asked to provide a color name, using the CSS3/SVG set of names, for the
  hexadecimal value ``#808080``, the integer triplet ``rgb(128, 128, 128)``, or
  the percentage triplet ``rgb(50%, 50%, 50%)``, ``webcolors`` now always returns
  ``u'gray'``, never ``u'grey'``. Previously, the behavior could be
  inconsistent as it depended on the Python version in use; ``u'gray'`` was
  picked because it was the spelling variant used in HTML 4, CSS1, and CSS2.


Version 1.8.1
~~~~~~~~~~~~~

Released February 2018

* The 1.8.1 release is a repackaging of 1.8 to produce both source (.tar.gz)
  and binary (.whl) package formats, following reports that the
  source-package-only release of 1.8 was causing installation issues for some
  users. See `issue 6 in the repository
  <https://github.com/ubernostrum/webcolors/issues/6>`_ for details.


Version 1.8
~~~~~~~~~~~

Released February 2018

* Added the :class:`~webcolors.IntegerRGB`, :class:`~webcolors.PercentRGB`, and
  :class:`~webcolors.HTML5SimpleColor` named tuples.

* Drop support for Python 3.3 (Python core team no longer maintains 3.3).

* Mark support for Python 3.6.

* :ref:`The full verification tests <full-verification>` now run correctly on
  Python 3.


Version 1.7
~~~~~~~~~~~

Released November 2016

* Drop support for Python 2.6 (Python core team no longer maintains 2.6).

* Mark support for Python 3.4.

* On Python 3, the use of :class:`str` for all functions which take string
  arguments is now mandatory. Attempted use of :class:`bytes` will raise an
  exception. On Python 2, use of bytestrings is still permitted.


Version 1.5.1
~~~~~~~~~~~~~

Released November 2015

* Corrected multiple typos in documentation.


Version 1.5
~~~~~~~~~~~

Released March 2015

* Python 3 support: ``webcolors`` now supports Python 3.3.

* Added :ref:`HTML5 color algorithms <html5-algorithms>`.


Version 1.4
~~~~~~~~~~~

Released February 2012

* Integer and percentage ``rgb()`` triplets now normalized in accordance with
  CSS clipping rules.

* Preparatory work for Python 3 support.


Version 1.3.1
~~~~~~~~~~~~~

Released October 2009

* Documentation expanded.

* Documentation now maintained using `Sphinx <http://www.sphinx-doc.org/>`_.


Version 1.3
~~~~~~~~~~~

* Documentation expanded.


Version 1.2
~~~~~~~~~~~

Released March 2009

* Corrected the download URL in the ``setup.py`` script.


Version 1.1
~~~~~~~~~~~

Released December 2008

* Documentation expanded.


Version 1.0
~~~~~~~~~~~

Released October 2008

* Initial stable release of ``webcolors``.
