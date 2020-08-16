import argparse
import os
from ._version import __version__

def version(args):
    print(args)


def main():
    parser = argparse.ArgumentParser(
        description='A CLI that performs various measurements on remote web pages with the following flags.'
    )

    parser.add_argument('version', help='Print a semver version')

    args = parser.parse_args()

    if args.version != None:
        version(__version__)

