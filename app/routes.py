from app import app
from app.controllers import user_controller, category_controller
from flask import request, jsonify
from flask_jwt_extended import *


@app.route('/')
def index():
    return 'hello world'

@app.route('/user', methods=['GET'])
@jwt_required()
def users():
    return user_controller.get_all_users()

@app.route('/register', methods=['POST'])
def register():
    return user_controller.register()

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def userRoute(id):
    if request.method == 'GET':
        return user_controller.get_user_by_id(id)
    elif request.method == 'PUT':
        return user_controller.update_user(id)
    elif request.method == 'DELETE':
        return user_controller.delete_user(id)

@app.route('/login', methods=['POST'])
def logins():
    return user_controller.login()

@app.route('/category', methods=['GET', 'POST'])
@jwt_required()
def category():
    if request.method == 'GET':
        return category_controller.get_all_category()
    elif request.method == 'POST':
        return category_controller.create_category()
    
@app.route('/category/<id>', methods=['GET', 'DELETE'])
@jwt_required()
def categoryRoute(id):
    if request.method == 'GET':
        return category_controller.get_category_by_id(id)
    elif request.method == 'DELETE':
        return category_controller.delete_category(id)