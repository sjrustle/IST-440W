__author__ = 'Scott'
import mysql.connector
from mysql.connector import errorcode

def get_Ebay_data(info):
    for key in info.items():
        try:
            ##Make SQL connection
            cnx = mysql.connector.connect(user = 'root',password = '',
                                          database = 'EBAY')
            ##
            cursor = cnx.cursor()
            cursor.execute("DROP TABLE IF EXISTS Ebay")
            cursor.execute("CREATE TABLE Ebay(ItemId INT NOT NULL PRIMARY KEY, TITLE TEXT, ValuePrice INT, ProductId INT)")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()

