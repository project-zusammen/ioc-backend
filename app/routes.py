from app import app
from app.blacklist import blacklist
from app.controllers import UserController
from flask import request, jsonify
from flask_jwt_extended import *


@app.route('/')
def index():
    return 'hello world'

@app.route('/user', methods=['GET'])
@jwt_required()
def users():
    user = get_jwt_identity()
    return UserController.getAllUsers()

@app.route('/register', methods=['POST'])
def register():
    return UserController.register()

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
def userRoute(id):
    if request.method == 'GET':
        return UserController.getUserByID(id)
    elif request.method == 'PUT':
        return UserController.updateUser(id)
    elif request.method == 'DELETE':
        return UserController.deleteUser(id)

@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return UserController.logout()