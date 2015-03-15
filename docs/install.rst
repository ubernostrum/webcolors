.. _install:


Installation guide
==================

The ``webcolors`` module has no external dependencies other than
Python itself. It's officially tested and supported on the following
versions of Python:

* Python 2.6

* Python 2.7

* Python 3.3

* Python 3.4


Normal installation
-------------------

The preferred method of installing ``webcolors`` is via ``pip``, the
standard Python package-installation tool. If you don't have ``pip``,
instructions are available for `how to obtain and install it
<https://pip.pypa.io/en/latest/installing.html>`_.

Once you have ``pip``, simply type::

    pip install webcolors


Manual installation
-------------------

It's also possible to install ``webcolors`` manually. To do so, obtain
the latest packaged version from `the listing on the Python Package
Index <https://pypi.python.org/pypi/webcolors/>`_. Unpack the
``.tar.gz`` file, and run::

    python setup.py install

Once you've installed ``webcolors``, you can verify successful
installation by opening a Python interpreter and typing ``import
webcolors``.

If the installation was successful, you'll simply get a fresh Python
prompt. If you instead see an ``ImportError``, check the configuration
of your install tools and your Python import path to ensure
``webcolors`` installed into a location Python can import from.


Installing from a source checkout
---------------------------------

The development repository for ``webcolors`` is at
<https://github.com/ubernostrum/webcolors>. Presuming you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/webcolors.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``python setup.py install``.
