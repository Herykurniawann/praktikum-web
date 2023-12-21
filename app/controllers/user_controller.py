from app.models.users import User
from app import response,app,db
from flask import request

def index():
    try :
        users = User.query.all()
        data = multiTransform(users)

        return response.success_response(data,"success")
    
    except Exception as e:
        return response.bad_request_response([],str(e))
    
def show(id):
    try :
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.not_found_response([], 'user not found')

        data = transform(user)
        return response.success_response(data, "success")
    except Exception as e:
        return response.bad_request_response([], str(e))

def create(request):
    try :
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        user = User(username=username, email=email)
        user.hashPassword(password)
        db.session.add(user)
        db.session.commit()

        print("ini tuh jalan")
        return response.success_response(transform(user), "success")

    except Exception as e:
        print(e)
        return response.bad_request_response([], str(e))

def update(id):
    try :
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']

        user = User.query.filter_by(id=id).first()
        if not user:
            return response.not_found_response([], 'user not found')
        
        user.email = email
        user.username = username
        user.hashPassword(password)

        print("ini tuh jalan")
        return response.success_response(None, "success")

    except Exception as e:
        print(e)
        return response.bad_request_response([], str(e))

def delete(id):
    try :
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.not_found_response([], 'user not found')

        db.session.delete(user)
        db.session.commit()

        return response.success_response(None, "success")

    except Exception as e:
        return response.bad_request_response([], str(e))
    

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        print(email)
        print(password)

        user = User.query.filter_by(email=email).first()
        # print(User.password)    
        if not user:
            print("usersnya salah")
            return response.bad_request_response([], 'user not found')
        
        print("usersnya udah bener")
        if not User.checkPassword(user, password):
            print("password salah")
            return response.bad_request_response([], 'invalid password')
        print("ini tuh jalan")
        data = transform(user)
        return response.success_response(data, "success")

    except Exception as e:
        print("ini tuh error")
        return response.bad_request_response([], str(e))


def transform(user):
    data = {
        "id" : user.id,
        "username": user.username,
        "email": user.email,
    }

    return data

def multiTransform(user):
    data = []
    for i in user:
        data.append(transform(i))
    return data

    