from setuptools import setup
import setuptools
import sys
import wincopper.metadata as md

assert sys.version[0] == '2', "This package currently works in Python 2.x, soon will be port to Python 3.x"

requires = []
if sys.platform == 'win32':
    requires = ['wheel', 'pandas', 'psutil', 'numpy']
elif sys.platform in ['linux', 'linux2', 'darwin', 'freebsd7', 
                      'freebsd8', 'freebsdN', 'openbsd6']:
    requires = ['wheel', 'pandas', 'psutil', 'numpy', 'resource']
else:
    assert requires != [], "OS not supported, Only supported in Windows and Unix-like"
    
setup(
    name='wincopper',
    version=md.__version__,
    description='WinCopper Algorithm Implementation',
    url='https://github.com/bitmapup/prefixspanr',
    author=md.__author__,
    author_email=md.__author_email__,
    maintainer=md.__maintainer__,
    maintainer_email=md.__maintainer_email__,
    packages=setuptools.find_packages(),
    license=md.__license__,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU Public License",
    ],
    python_requires='>=2.7'
)
