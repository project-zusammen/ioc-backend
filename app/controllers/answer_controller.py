from app.models.exam import Exam
from app.models.answer import Answer
from app.models.user import User
from app import response, db
from flask import request, jsonify
from flask_jwt_extended import *


def answer_question(id):
    try:
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])
        user_id = user.id
        exam = Exam.query.get(id)
        answer = request.form.get("answer")
        answers = Answer(answer=answer, exam_id=exam.id)
        db.session.add(answers)
        db.session.commit()
        
        if answer == exam.correct_option:
            score = 10
            get_user = User.query.filter_by(id=user_id).first()
            get_user.score = get_user.score + score
            db.session.commit()
            return response.success("the correct answer is" + exam.correct_option, "your answer is correct")
        else:
            return response.success("the answer is " + exam.correct_option, "your answer is incorrect")
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500    
    
        
