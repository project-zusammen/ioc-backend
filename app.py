from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

@app.route('/user/<int:id>')
def user(id):
    user = db.get_or_404(User, id)
    print('ID = ' + str(user.id) + ', Name = ' + user.name)
    return '<p>Hello, ' + user.name + '</p>\n'
