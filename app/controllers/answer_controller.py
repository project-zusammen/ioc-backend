from app.models.question import Question
from app.models.answer import Answer
from app.models.user import User
from app.models.score import Score
from app import response, db
from flask import request, jsonify
from flask_jwt_extended import *


def answer_question_by_question_id(question_id):
    try:
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])
        user_id = user.id
        question = Question.query.get(question_id)
        question_id = question.id
        exam_id = question.exam_id
        answer = request.form.get("answer")
        answers = Answer(answer=answer, question_id=question_id)
        db.session.add(answers)
        db.session.commit()

        score = Score.query.filter_by(user_id=user_id, exam_id=exam_id).first()
        if not score:
            user_id = user.id
            exam_id=exam_id
            score = 0
        
            new_score =  Score(user_id=user_id, exam_id=exam_id,score=score)
            db.session.add(new_score)
            db.session.commit()
        
        if answer == question.correct_option:
            value = 10
            get_score = Score.query.filter_by(user_id=user_id).first()
            get_score.score = get_score.score + value
            get_total_score = User.query.filter_by(id=user_id).first()
            get_total_score.score = get_total_score.score + value
            db.session.commit()
            return response.success("the correct answer is " + question.correct_option, "your answer is correct")
        else:
            return response.success("the answer is " + question.correct_option, "your answer is incorrect")
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500    
    
        
