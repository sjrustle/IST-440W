__author__ = 'Scott'
import mysql
from mysql.connector import errorcode

def get_Ebay_data(info):

        try:
            ##Make SQL connection
            cnx = mysql.connector.connect(user = 'root',password = '',
                                          database = 'EBAY')
            ##
            cursor = cnx.cursor()
            cursor.execute("DROP TABLE IF EXISTS Ebay")
            cursor.execute("CREATE TABLE EBAY(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,ItemId INT NOT NULL, TITLE VARCHAR(255), ValuePrice INT, ProductId INT)")
            for key in info.items():
                for values in key:
                    for value in values:
                        if len(value) > 1:
                            print type(value['itemId'])
                            print type(value['title'])
                            cursor.execute("INSERT INTO EBAY (ItemId,TITLE,ValuePrice,ProductId) VALUES (%s,%s,%s,%s)",(value['itemId'],value['title'],'100','100'))
                            cnx.commit()
                        else:
                            continue
                        ##cursor.execute("INSERT INTO Ebay (ItemId,TITLE,ValuePrice,ProductId) VALUES ({},{},{},{})".format(value['itemId'],value['title'],100,100))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()

