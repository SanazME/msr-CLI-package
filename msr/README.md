msr
====

A CLI that performs various measurements on remote web pages. We'll call this CLI msr. There will be several subcommands to msr, each of which might take some arguments.

The code is Python 3 compatible.

Installation
------------
::
    
    pip  install msr


Commands
-----------

**Version** : prints a semver string of the package.
::

    msr version

**Register** : take a URL and add the validate URL to an internal, persistent registry.
::
    
    msr register <url>

**Measure** : returns a pretty-printed table of all of the URLs in the registry along with the size (in bytes) of the body received by making a GET request to that URL.
::
    
    msr measure

**Race** : returns a pretty-printed table of all the domain found in the URLs in the registry, along with the average page load time for the URLs of that domain.

::
    
    msr race



**Note to myself**
- install `pipenv` to define the correct python and pip version for the vitual env. (checkout https://towardsdatascience.com/python-environment-101-1d68bda3094d): `pipenv --python 3.7 install`
- you can then run `pipenv shell` to work in virtual env shell.
- to test package, you can install the package locally using pip:
    - first create built distribution (`.whl`) and source files (`tar.gz`) files (optional for locall pip testing I think!): `python setup.py sdist bdist_wheel`
    - then run pip : `pip install -e .`
    - now you can test different msr commands: `msr -h`, `msr --version`, `msr --register 'https://examples.com`