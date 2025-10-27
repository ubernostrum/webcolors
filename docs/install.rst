.. _install:


Installation guide
==================

Version |release| of ``webcolors`` is officially tested and supported on the
following versions of Python:

* Python 3.10

* Python 3.11

* Python 3.12

* Python 3.13

* Python 3.14


Installing ``webcolors``
------------------------

To install the latest stable released version of ``webcolors``, run the following
command from a command prompt/terminal:

.. tab:: macOS/Linux/other Unix

   .. code-block:: shell

      python -m pip install --upgrade webcolors

.. tab:: Windows

   .. code-block:: shell

      py -m pip install --upgrade webcolors

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


Installing from a source checkout
---------------------------------

If you want to work on ``webcolors``, you can obtain a source checkout.

The development repository for ``webcolors`` is at
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
