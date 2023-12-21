from app import app
from app.controllers import user_controller
from flask import request

@app.route('/')

def index():
    return 'Hello, World!'


@app.route('/users',methods=['GET','POST'])
def users():
    if request.method == 'POST':
        return user_controller.create(request)
    else:
        return user_controller.index()

@app.route('/users/<id>',methods=['PUT','GET','DELETE'])
def userById(id):
    if request.method == 'GET':
        return user_controller.show(id)
    elif request.method == 'PUT':
        return user_controller.update(id)
    elif request.method == 'DELETE':
        return user_controller.delete(id)
    else:
        return user_controller.index()
    

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        return user_controller.login()