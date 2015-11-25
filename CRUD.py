import MySQLdb
import wsLogging

# Creates connection with DB
def create_connection():
    try:
     cnx = MySQLdb.connect(host = "localhost", user = "root", passwd = "Team5", db = "testDB")
     cur = cnx.cursor()
     wsLogging.audit_logging("CRUD", "String created")
     return cur
    except:
        wsLogging.error_logging("CRUD","Error during Connection")

# Sends services to client
def get_user(connection, user_name):
    try:
        cur = create_connection()
        cur.execute("SELECT user_service FROM user WHERE username = %s", user_name)
        user_service =  cur.fetchall()
        return user_service
    except:
        wsLogging.error_logging("Get User", "Couldn't send user token")
