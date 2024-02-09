from app.models.exam import Exam
from app.models.answer import Answer
from app import response, db
from flask import request, jsonify
from flask_jwt_extended import *


def answer_question(id):
    try:
        exam = Exam.query.get(id)
        answer = request.form.get("answer")
        answers = Answer(answer=answer, exam_id=exam.id)
        db.session.add(answers)
        db.session.commit()
        
        if answer == exam.correct_option:
            return response.success("", "your answer is correct")
        else:
            return response.success("", "your answer is incorrect")
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500    
    
        
