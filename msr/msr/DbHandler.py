import sqlite3



class DbHandler:
    """
    A class to handle interaction with sqlite database. It includes methods
    for insertion and retrieval of data from the database
    """

    @staticmethod
    def createDB():
        # create or connect to existing database
        connectdb = sqlite3.connect('urlLinks.db')
        cursor = connectdb.cursor()

        # check if the table exists
        tableName = ('urls')
        cursor.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?''', (tableName,))

        if cursor.fetchone()[0] == 1:
            print('Table already exists')
        else:
            # only need to execute once???
            cursor.execute(''' CREATE TABLE urls
            (
            ADDRESS     VARCHAR(2083) PRIMARY KEY NOT NULL); ''')
            print('Table is created successfully!')

        return DbHandler(connectdb, cursor)

    def __init__(self, connectdb, cursor):
        super().__init__()
        self.connectdb = connectdb
        self.cursor = cursor

    def insert(self, url):
        """ insert a url"""
        try:
            self.cursor.execute('INSERT INTO urls VALUES (?)', (url,))

            # save (commint) the changes
            self.connectdb.commit()
            print('Record created successfullsy!')

        except sqlite3.Error as error:
            print("Failed to handle DB with error: ", error)

        finally:
            if (self.connectdb):
                # close the db connection
                self.connectdb.close()
                print('Connection to db is closed.')

    def getUrlList(self):
        urlList = []
        try:
            for address in self.cursor.execute('SELECT * FROM urls'):
                urlList.append(address)
    
        except sqlite3.Error as error:
            print("Failed to get a list of urls from databaes: ", error)
        finally:
            return urlList
