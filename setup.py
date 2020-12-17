from setuptools import setup
import setuptools
import sys
import copper.metadata as md

assert sys.version[0] == '2', "This package currently works in Python 2.x, soon will be port to Python 3.x"

requires = []
if sys.platform == 'win32':
    requires = ['copper', 'pandas', 'psutil', 'numpy']
elif sys.platform in ['linux', 'linux2', 'darwin', 'freebsd7', 
                      'freebsd8', 'freebsdN', 'openbsd6']:
    requires = ['copper', 'pandas', 'psutil', 'numpy', 'resource']
else:
    assert requires != [], "OS not supported, Only supported in Windows and Unix-like"
    
setup(
    name='copper',
    version='1.0.0',
    description='Copper Algorithm Implementation',
    url='git@github.com:bitmapup/prefixspanr.git',
    author=md.__author__,
    author_email='@pucp.edu.pe',
    maintainer=md.__maintainer__,
    maintainer_email='ye.maehara@up.edu.pe',
    packages=setuptools.find_packages(),
    license="GPL",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU Public License",
    ],
    python_requires='>=2.7'
)
