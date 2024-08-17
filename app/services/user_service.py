from app.models.user_model import User

def create_user(data,db):
    email= data.get('email')
    ex_user = db.users.find_one({"email":email})
    if ex_user:
        return None
    return User(
        name=data.get('name'),
        mobile_no=data.get('mobile_no'),
        email=data.get('email'),
        address=data.get('address')
    )
 