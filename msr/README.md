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
    
    msr register

**Measure** : returns a pretty-printed table of all of the URLs in the registry along with the size (in bytes) of the body received by making a GET request to that URL.
::
    
    msr measure

**Race** : returns a pretty-printed table of all the domain found in the URLs in the registry, along with the average page load time for the URLs of that domain.

::
    
    msr race



