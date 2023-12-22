from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from app.models.user import User
from app.resources.user_resources import UserResource

api.add_resource(UserResource, '/users/<int:user_id>')

if __name__ == '__main__':
    migrate.init_app(app, db)
    app.run(debug=True)
