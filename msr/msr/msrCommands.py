import argparse
import validators
import sys
from ._version import __version__
from .DbHandler import DbHandler

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


def main():
    parser = argparse.ArgumentParser(
        description='A CLI that performs various measurements on remote web pages with the following flags.'
    )

    parser.add_argument('--version', nargs='*', help='Print a semver version')
    parser.add_argument('--register', nargs=1, metavar='URL',
                        help='Take a URL and if the URL is valid, add it to an internal, persistent registry')

    args = parser.parse_args()

    if args.version != None:
        version(__version__)
    elif args.register != None:
        register(args)
