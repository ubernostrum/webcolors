from setuptools import setup


# setuptools is built on the assumption that everything is a package
# in a directory, not a single file, so we have to pass py_modules
# here to get distutils behavior, and can't set this option in
# setup.cfg.
setup(py_modules=['webcolors'])
