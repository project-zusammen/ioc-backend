from app.models.comment_reply import CommentReply
from app.models.user import User
from app import response, db
from flask import request, jsonify
from flask_jwt_extended import *

def get_all_comment_replies():
    try:
        replies = CommentReply.query.all()
        replies_data = []
        for reply in replies:
            user = User.query.get(reply.user_id)
            user_name = user.name

            reply_data = {
                "id": reply.id,
                "user_name": user_name,
                "reply": reply.reply,
                "comment_id": reply.comment_id,
                "created_at": reply.created_at          
            }
            replies_data.append(reply_data)
        return jsonify({"replies": replies_data})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500

def get_all_replies_by_comment_id(comment_id):
    try:
        replies = CommentReply.query.filter_by(comment_id=comment_id).all()
        if not replies:
            return response.badRequest([], "Replies not found")
        replies_data = []
        for reply in replies:
            user = User.query.get(reply.user_id)
            user_name = user.name

            reply_data = {
                "id": reply.id,
                "user_name": user_name,
                "comment_id": reply.comment_id,
                "reply": reply.reply,
                "created_at": reply.created_at
            }
            replies_data.append(reply_data)
        return jsonify({"replies": replies_data})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500

def create_reply(comment_id):
    try:
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])

        reply = request.form.get("reply")
        user_id = user.id

        create_reply = CommentReply(reply=reply, user_id=user_id, comment_id=comment_id)
        db.session.add(create_reply)
        db.session.commit()
        return jsonify(
            {
                "reply": {
                    "id": create_reply.id,
                    "reply": create_reply.reply,
                    "user_id": create_reply.user_id,
                    "comment_id": create_reply.comment_id,
                    "created_at": create_reply.created_at
                }
            }
        )
    except Exception as e:
        return jsonify({"error": f"An error occured : {e}"}), 500
    