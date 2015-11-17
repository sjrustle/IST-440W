from CRUD import create_connection, get_user
import jwt

# Returns JWT string
def return_jwt(username):
    con = create_connection()
    user_service_array = get_user(con, username)
    user_service_tuple = user_service_array[0]
    service_unpacked = user_service_tuple[0]
    encoded = jwt.encode({'user_service': service_unpacked},'secret', algorithm='HS256')
    return encoded
