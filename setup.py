import sys
import os
from distutils.core import setup

if sys.version_info.major >= 3:
    print 'Sorry, currently only supports Python 2. Patches welcome!'
    sys.exit(1)

setup(
    name='browser-cookie', 
    version='0.5',
    packages=['browser_cookie'],
    package_dir={'browser_cookie' : '.'}, # look for package contents in current directory
    author='Richard Penman',
    author_email='richard@webscraping.com',
    description='Loads cookies from your browser into a cookiejar object so can download with urllib and other libraries the same content you see in the web browser.',
    url='https://bitbucket.org/richardpenman/browser_cookie',
    install_requires=['pycrypto', 'keyring'],
    license='lgpl'
)
