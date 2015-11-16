import MySQLdb
import pdb

pdb.set_trace()
cnx = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'Team5',
		      db = 'testDB')

cursor = cnx.cursor()
cursor.execute("CREATE TABLE USERS(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY)")
cnx.commit()
cnx.close()
