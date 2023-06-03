import bcrypt
from app.models.user import User
from app.users.queries import create_user_query
from app.payments.services.create_payment_instance import create_payment

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
        # this can be async function call
        # this is creating a payment instance for the customer and registering them in our stripe dashboard.
        create_payment(user.id, user.email, "stripe", "test_plan", "0")
        return True
    except Exception:
        return False



