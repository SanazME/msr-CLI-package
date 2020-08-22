import sqlite3


class DbHandler:
    """
    A class to hadle insteratinon with sqlite database. It includes methods
    for insertion and retrieval of data from the database
    """
    
    def __init__(self):
        super().__init__()
        # create or connect to existing database
        self.connectdb = sqlite3.connect('urlLinks.db')
        self.cursor = self.connectdb.cursor()

        # check if the table exists
        tableName = ('urls')
        self.cursor.execute(
            ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?''', (tableName,))

        if self.cursor.fetchone()[0] == 1:
            print('Table already exists')
        else:
            # only need to execute once???
            self.cursor.execute(''' CREATE TABLE urls
            (
            ADDRESS     VARCHAR(2083) PRIMARY KEY NOT NULL); ''')
            print('Table is created successfully!')


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
