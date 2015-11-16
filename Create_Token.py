from CRUD import create_connection, get_user
import jwt

# Returns JWT string
def return_jwt(username):
    con = create_connection()
