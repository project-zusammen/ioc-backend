from app.models.comments import Comments
from app import response, app, db
from flask import request, jsonify

def getCommentAll():
    try:
        comments = Comments.query.all()
        return jsonify({'Comment': {
            {
                'id' : comment.id,
                'comment' : comment.comment,
                'user_id' : comment.user_id,
                'replyTo' : comment.replyTo
            } for comment in comments
        }})
    except Exception as e:
        print(e)

def getCommentById(id):
    try:
        comment = Comments.query.get(id)

        if comment:
            data = {
                'id' : comment.id,
                'comment' : comment.comment,
                'user_id' : comment.user_id,
                'replyTo' : comment.replyTo
            }
            return jsonify(data)
        else : 
            return jsonify({'error': 'Comment not found!'})
    except Exception as e:
        print(e)

def addComment():
    try:
        comment = request.form.get('name')
        replyTo = request.form.get('replyTo')
        user_id = request.form.get('user_id')
        comment = Comments(
            comment = comment,
            replyTo = replyTo,
            user_id = user_id
        )
        db.session.add(comment)
        db.session.commit()
        return response.success('', 'Your Comment has been added')
    except Exception as e:
        print(e)

def deleteComment(id):
    try:
        comment = Comments.query.filter_by(id=id).first()
        if not comment:
            return jsonify({'error': 'Comment not found!'})
        db.session.delete(comment)
        db.session.commit()
        return response.success('', 'The Comment has been deleted')
    except Exception as e:
        print(e)
