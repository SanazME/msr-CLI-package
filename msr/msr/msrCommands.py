import argparse
import os

def version(args):
    version = 'hard-coded version'
    print(version)


def main():
    parser = argparse.ArgumentParser(
        description='A CLI that performs various measurements on remote web pages with the following flags.'
    )

    parser.add_argument('version', nargs=0, help='Print a semver version')

    args = parser.parse_args()

    if args.version != None:
        version(arfs)

