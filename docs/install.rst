.. _install:


Installation guide
==================

The |release| version of webcolors is officially tested and supported
on the following versions of Python:

* Python 3.7

* Python 3.8

* Python 3.9

* Python 3.10

* Python 3.11


Installing webcolors
--------------------

To install webcolors, run the following command from a command
prompt/terminal:

.. tab:: macOS/Linux/other Unix

   .. code-block:: shell

      python -m pip install webcolors

.. tab:: Windows

   .. code-block:: shell

      py -m pip install webcolors

This will use ``pip``, the standard Python package-installation tool. If you
are using a supported version of Python, your installation of Python should
have come with ``pip`` bundled. If ``pip`` does not appear to be present, you
can try running the following from a command prompt/terminal:

.. tab:: macOS/Linux/other Unix

   .. code-block:: shell

      python -m ensurepip --upgrade

.. tab:: Windows

   .. code-block:: shell

      py -m ensurepip --upgrade

Instructions are also available for `how to obtain and manually install or
upgrade pip <https://pip.pypa.io/en/latest/installation/>`_.

If you don't already have a supported version of Django installed, using
``pip`` to install webcolors will also install the latest supported version of
Django.


Installing from a source checkout
---------------------------------

If you want to work on webcolors, you can obtain a source checkout.

The development repository for webcolors is at
<https://github.com/ubernostrum/webcolors>. If you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the repository by
typing::

    git clone https://github.com/ubernostrum/webcolors.git

From there, you can use git commands to check out the specific revision you
want, and perform an "editable" install (allowing you to change code as you
work on it) by typing:

.. tab:: macOS/Linux/other Unix

   .. code-block:: shell

      python -m pip install -e .

.. tab:: Windows

   .. code-block:: shell

      py -m pip install -e .
