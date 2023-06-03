import bcrypt
from app.models.user import User
from app.users.queries import create_user_query


def create_user_svc(email, password, full_name):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Create a new user instance
    user = User(
        email=email,
        password=hashed_password.decode('utf-8'),
        full_name=full_name,
        # more attributes later
    )
    try:
        create_user_query(user)
        return True
    except:
        return False



