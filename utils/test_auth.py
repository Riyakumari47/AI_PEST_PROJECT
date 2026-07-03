from utils.auth import register_user, login_user

register_user("Riya", "riya@gmail.com", "1234")

login_user("riya@gmail.com", "1234")