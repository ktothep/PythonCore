from user import User

def authenticate(username,password):
    user=User.findby_username(username)
    if user and user.password==password:
        return user

def identity(payload):
    user_id=payload('identity')
    return User.findby_id(user_id)
