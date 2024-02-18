from app.models.user import User
from app.models.question import Question
from app.models.exam import Exam
from app import response, db
from flask import request, jsonify
from flask_jwt_extended import *
import datetime

def format_question(question):
    return {
        "id": question.id,
        "question_text": question.question_text,
        "question_number" : question.question_number,
        "correct_option" : question.correct_option,
        "option_a": question.option_a,
        "option_b": question.option_b,
        "option_c": question.option_c,
        "option_d": question.option_d,
        "user_id": question.user_id,
        "exam_id": question.exam_id,
        "created_at": question.created_at,
        "updated_at": question.updated_at
    }

def get_all_questions():
    try:
        questions = Question.query.all()
        formated_questions = [format_question(question) for question in questions]
        return jsonify({"questions": formated_questions})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500

def get_all_questions_by_exam_id(exam_id):
    try: 
        questions = Question.query.filter_by(exam_id=exam_id).all()
        if not questions:
            return response.badRequest([], "Question not found")
        formated_questions = [format_question(question) for question in questions]
        return jsonify({"question": formated_questions})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500

def get_question_by_id(id):
    try:
        GetQuestion = Question.query.get(id)
        if GetQuestion:
            question = {
                "id": GetQuestion.id,
                "question_text": GetQuestion.question_text,
                "question_number" : GetQuestion.question_number,
                "correct_option" : GetQuestion.correct_option,
                "option_a": GetQuestion.option_a,
                "option_b": GetQuestion.option_b,
                "option_c": GetQuestion.option_c,
                "option_d": GetQuestion.option_d,
                "user_id": GetQuestion.user_id,
                "exam_id": GetQuestion.exam_id,
                "created_at": GetQuestion.created_at,
                "updated_at": GetQuestion.updated_at,
            }
            return jsonify(question)
        else:
            return jsonify({"error": "Question not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An erro occured: {e}"}), 500
    
def create_question():
    try:
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])

        question_text = request.form.get("question_text")
        question_number = request.form.get("question_number")
        correct_option = request.form.get("correct_option")
        option_a = request.form.get("option_a")
        option_b = request.form.get("option_b")
        option_c = request.form.get("option_c")
        option_d = request.form.get("option_d")
        user_id = user.id
        exam_id = request.form.get("exam_id")

        question = Question(
            question_text=question_text,
            question_number=question_number,
            correct_option=correct_option,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            user_id=user_id,
            exam_id=exam_id
        )
        db.session.add(question)
        db.session.commit()
        return jsonify({"question": format_question(question)})
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500
    
def update_question(id):
    try:
        question_text = request.form.get("question_text")
        question_number = request.form.get("question_number")
        correct_option = request.form.get("correct_option")
        option_a = request.form.get("option_a")
        option_b = request.form.get("option_b")
        option_c = request.form.get("option_c")
        option_d = request.form.get("option_d")
        exam_id = request.form.get("exam_id")
        updated_at = datetime.datetime.utcnow()

        question = Question.query.filter_by(id=id).first()

        if question:
            if question_text is not None:
                question.question_text = question_text
            if question_number is not None:
                question.question_number = question_number
            if correct_option is not None:
                question.correct_option = correct_option
            if option_a is not None:
                question.option_a = option_a
            if option_b is not None:
                question.option_b = option_b
            if option_c is not None:
                question.option_c = option_c
            if option_d is not None:
                question.option_d = option_d
            if exam_id is not None:
                question.exam_id = exam_id
            question.updated_at = updated_at

            db.session.commit()
            return response.success("", "Question has been updated")
        else:
            return response.badRequest("error", "Update question is failed")
    except Exception as e:
        return jsonify({"error": f"An error occured: {e}"}), 500
    
def delete_question(id):
    try:
        question = Question.query.filter_by(id=id).first()
        if not question:
            return response.badRequest([], "Question not found")
        db.session.delete(question)
        db.session.commit()

        return response.success([], "Question has been deleted")
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500