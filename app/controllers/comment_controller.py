from app.models.comment import Comment
from app.models.user import User
from app import response, db
from flask import request, jsonify
from flask_jwt_extended import *

def get_all_comments():
    try:
        comments = Comment.query.all()
        comments_data = []
        for comment in comments:
            user = User.query.get(comment.user_id)
            user_name = user.name
        
            comment_data = {
                "id": comment.id,
                "user_name": user_name,
                "material_id": comment.material_id,
                "comment": comment.comment,
                "created_at": comment.created_at
            }
            comments_data.append(comment_data)
        return jsonify({"comments": comments_data})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500
        

def get_all_comments_by_material_id(material_id):
    try:
        comments = Comment.query.filter_by(material_id=material_id).all()
        if not comments:
            return response.badRequest([], "Comments not found")
        comments_data = []
        for comment in comments:
            user = User.query.get(comment.user_id)
            user_name = user.name
        
            comment_data = {
                "id": comment.id,
                "user_name": user_name,
                "material_id": comment.material_id,
                "comment": comment.comment,
                "created_at": comment.created_at
            }
            comments_data.append(comment_data)
        return jsonify({"comments": comments_data})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500

def create_comment(material_id):
    try: 
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])

        comment = request.form.get("comment")
        user_id = user.id

        create_comment = Comment(comment=comment, user_id=user_id, material_id=material_id)
        db.session.add(create_comment)
        db.session.commit()
        return jsonify(
            {
                "comment": {
                    "id": create_comment.id,
                    "comment": create_comment.comment,
                    "user_id": create_comment.user_id,
                    "material_id": create_comment.material_id,
                    "created_at": create_comment.created_at
                }
            }
        )
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500