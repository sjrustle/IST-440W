from CRUD import create_connection, get_user
import jwt

# Returns JWT string
def return_jwt(username):
    con = create_connection()
    service = get_user(con, username)
    encoded = jwt.encode({'user_service': service},'secret', algorithm='HS256')
    return encoded
