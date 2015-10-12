__author__ = 'Scott'
import mysql.connector
from mysql.connector import errorcode

try:
    ##This change when uploaded to our server
    cnx = mysql.connector.connect(user='root', password='',database='EBAY')
except mysql.connector.errorcode as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)