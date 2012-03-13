from distutils.core import setup

setup(name='4otaku_zalivator',
      version='1.0.0b',
      py_modules=['main'],
      packages = ['lib', 'lib.send', 'lib.util', 'lib.window', 'lib.action', 'lib.thread']
      )
