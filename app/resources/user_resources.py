from flask_restful import Resource
from app.models.user import User


class UserResource(Resource):

    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'name': user.name}
