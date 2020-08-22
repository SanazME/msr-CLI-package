import argparse
import validators
import sys
import sqlite3
from ._version import __version__

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
        handleDB(url)

        return
    print('wrong url')
    return sys.exit(1)


# create a new database
def handleDB(url):

    try:
        # create or connect to existing database
        connectdb = sqlite3.connect('urlLinks.db')
        cursor = connectdb.cursor()

        # check if table exists
        tableExist = isTableExists(cursor, 'urls')

        if tableExist: 
            print('Table already exists')
        else:
            # only need to execute once???
            cursor.execute(''' CREATE TABLE urls
            (
            ADDRESS     VARCHAR(2083) PRIMARY KEY NOT NULL); ''')
            print('Table is created successfully!')

        # insert to table
        cursor.execute('INSERT INTO urls VALUES (?)', (url,))

        # save (commint) the changes
        connectdb.commit()
        print('Record created successfully!')

    except sqlite3.Error as error:
        print("Failed to handle DB with error: ", error)
    
    finally:
        if (connectdb):
            # close the db connection
            connectdb.close()
            print('Connection to db is closed.')


def isTableExists(cursor, tableName):
    cursor.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?''', (tableName,))

    return cursor.fetchone()[0] == 1      


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
