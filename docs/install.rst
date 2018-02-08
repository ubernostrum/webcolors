.. _install:


Installation guide
==================

The webcolors module has no external dependencies other than
Python itself. It's officially tested and supported on the following
versions of Python:

* Python 2.7

* Python 3.4

* Python 3.5

* Python 3.6

These are the versions of Python receiving upstream bugfix or security
support as of the release of webcolors |version|. Use of older
versions of Python is not recommended, and typically will result in
errors.


Normal installation
-------------------

The preferred method of installing webcolors is via ``pip``, the
standard Python package-installation tool. If you don't have ``pip``,
instructions are available for `how to obtain and install it
<https://pip.pypa.io/en/latest/installing.html>`_. If you're using
Python 2.7.9 or later (for Python 2) or Python 3.4 or later (for
Python 3), ``pip`` came bundled with your installation of Python.

Once you have ``pip``, type::

    pip install webcolors


Installing from a source checkout
---------------------------------

If you want to work on webcolors, you can obtain a source checkout.

The development repository for webcolors is at
<https://github.com/ubernostrum/webcolors>. If you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/webcolors.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``pip install -e .`` (the
``-e`` flag specifies an "editable" install, allowing you to change
code as you work on webcolors, and have your changes picked up
automatically).