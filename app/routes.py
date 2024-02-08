from app import app
from app.controllers import user_controller, category_controller, comment_controller
from flask import request, jsonify
from flask_jwt_extended import *
from flask_swagger_ui import get_swaggerui_blueprint

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static',path)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json' 
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "IOC-BE"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
##app.register_blueprint(request_api.get_blueprint())


##@app.route('/')
##def index():
  ##  return 'hello world'

@app.route('/user', methods=['GET'])
##@jwt_required()
def users():
    return user_controller.get_all_users()

@app.route('/register', methods=['POST'])
def register():
    return user_controller.register()

@app.route('/user/<id>', methods=['GET', 'PUT', 'DELETE'])
##@jwt_required()
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

@app.route('/comment', methods=['GET', 'POST'])
##@jwt_required()
def comment():
    if request.method == 'GET':
        return comment_controller.getCommentAll()
    elif request.method == 'POST':
        return comment_controller.addComment()
    
@app.route('/comment/<id>', methods=['GET', 'DELETE'])
##@jwt_required()
def commentRoute(id):
    if request.method == 'GET':
        return comment_controller.getCommentById(id)
    elif request.method == 'DELETE':
        return comment_controller.deleteComment(id)