import argparse
import validators
import sys
from tabulate import tabulate
from ._version import __version__
from .DbHandler import DbHandler
from .UrlHandler import UrlHandler

# install package locally:
# python setup.py sdist bdist_wheel
# pip install -e .


def version(args):
    print(args)


def register(args):
    isUrlValid = validators.url(args.register[0])

    if isUrlValid:
        url = args.register[0]

        # insert to database
        db = DbHandler.createDB()
        db.insert(url)
        return

    print('wrong url')
    return sys.exit(1)

def measure(args):
    # get a list if urls from db
    db = DbHandler.createDB()
    address_list = db.getUrlList()

    urlByteSize = UrlHandler(address_list).getRequestSize()

    print(urlByteSize)
    headers = ['URL', 'Size(bytes)']
    print(tabulate(urlByteSize, headers, tablefmt='fancy_grid'))


def race(args):
    db = DbHandler.createDB()
    address_list = db.getUrlList()

    domainList = UrlHandler(address_list).getAvgLoadTime()
    headers = ['Domain', 'Average Load Time(s)']
    print(tabulate(domainList, headers, tablefmt='fancy_grid'))
    




def main():
    parser = argparse.ArgumentParser(
        description='A CLI that performs various measurements on remote web pages with the following flags.'
    )

    parser.add_argument('--version', nargs='*', help='Print a semver version')
    parser.add_argument('--register', nargs=1, metavar='URL',
                        help='Take a URL and if the URL is valid, add it to an internal, persistent registry')
    parser.add_argument('--measure', nargs='*', help='Pretty print table of all of the URLs in the registry, along with the size (in bytes) of the body received by making a GET request to that URL.')
    parser.add_argument('--race', nargs='*', help='Pretty print table of all the domains found in the URLs in the registry, along with the average page load time for the URLs of that domain')

    args = parser.parse_args()

    if args.version != None:
        version(__version__)
    elif args.register != None:
        register(args)
    elif args.measure != None:
        measure(args)
    elif args.race != None:
        race(args)
