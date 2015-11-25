from CRUD import create_connection, get_user
import jwt
import wsLogging

# Returns JWT string
def return_jwt(username):
    try:
        # Create connection to DB
        con = create_connection()

        #Get user and their services and parse out the dict taht is sent back
        user_service_array = get_user(con, username)
        user_service_tuple = user_service_array[0]
        service_unpacked = user_service_tuple[0]
        encoded = jwt.encode({'user_service': service_unpacked},'secret', algorithm='HS256')
        wsLogging.audit_logging("Create_Token", "Toek was created")
        return encoded
    except:
        wsLogging.error_logging("Create_Token","Error when creating token")
