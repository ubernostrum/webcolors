import os

from distutils.core import setup

setup(name='webcolors',
      version='1.3.1',
      description='A library for working with sRGB color specifications as used in HTML and CSS.',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read(),
      author='James Bennett',
      author_email='james@b-list.org',
      url='http://www.bitbucket.org/ubernostrum/webcolors/overview/',
      py_modules=['webcolors'],
      download_url='http://bitbucket.org/ubernostrum/webcolors/downloads/webcolors-1.3.1.tar.gz',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
