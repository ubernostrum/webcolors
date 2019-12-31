.. _install:


Installation guide
==================

The |release| version of webcolors is officially tested and supported
on the following versions of Python:

* Python 3.5

* Python 3.6

* Python 3.7

* Python 3.8


Normal installation
-------------------

The preferred method of installing webcolors is via `pip`, the
standard Python package-installation tool. If you don't have `pip`,
instructions are available for `how to obtain and install it
<https://pip.pypa.io/en/latest/installing.html>`_. If you're using a
supported version of Python, `pip` came bundled with your installation
of Python.

Once you have `pip`, type::

    pip install webcolors


Installing from a source checkout
---------------------------------

If you want to work on webcolors, you can obtain a source checkout.

The development repository for webcolors is at
<https://github.com/ubernostrum/webcolors>. If you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/webcolors.git

From there, you can use git commands to check out the specific
revision you want, and perform an "editable" install (allowing you to
change code as you work on it) by typing::

    pip install -e .
