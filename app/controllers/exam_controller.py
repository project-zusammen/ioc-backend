from app.models.exam import Exam
from app.models.user import User
from app import response, app, db
from flask import request, jsonify
from flask_jwt_extended import *
import datetime

def format_exam(exam):
    return {
        "id": exam.id,
        "question": exam.question,
        "correct_option": exam.correct_option,
        "option_a": exam.option_a,
        "option_b": exam.option_b,
        "option_c": exam.option_c,
        "option_d": exam.option_d,
        "user_id": exam.user_id,
        "material_id" : exam.material_id,
        "created_at": exam.created_at,
        "updated_at": exam.updated_at
    }

def get_all_exam():
    try:
        exams = Exam.query.all()
        formated_exams = [format_exam(exam) for exam in exams]
        return jsonify({"exams": formated_exams})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def get_exam_by_id(id):
    try:
        GetExam = Exam.query.get(id)
        if GetExam :
            exam = {
                 "id": GetExam.id,
                "question": GetExam.question,
                "correct_option": GetExam.correct_option,
                "option_a": GetExam.option_a,
                "option_b": GetExam.option_b,
                "option_c": GetExam.option_c,
                "option_d": GetExam.option_d,
                "user_id": GetExam.user_id,
                "material_id" : GetExam.material_id,
                "created_at": GetExam.created_at,
                "updated_at": GetExam.updated_at
            }
            return jsonify(exam)
        else:
            return jsonify({"error": "Exam not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def create_exam():
    try:
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])

        question = request.form.get("question")
        correct_option = request.form.get("correct_option")
        option_a = request.form.get("option_a")
        option_b = request.form.get("option_b")
        option_c = request.form.get("option_c")
        option_d = request.form.get("option_d")
        user_id =  user.id
        material_id = request.form.get("material_id")

        exam = Exam(
            question=question,
            correct_option=correct_option,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            user_id=user_id,
            material_id=material_id
        )
        db.session.add(exam)
        db.session.commit()
        return jsonify({"exam": format_exam(exam)})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def update_exam(id):
    try:
        question = request.form.get("question")
        correct_option = request.form.get("correct_option")
        option_a = request.form.get("option_a")
        option_b = request.form.get("option_b")
        option_c = request.form.get("option_c")
        option_d = request.form.get("option_d")
        updated_at = datetime.datetime.utcnow()

        exam = Exam.query.filter_by(id=id).first()

        if exam:
            if question is not None:
                exam.question = question
            if correct_option is not None:
                exam.correct_option = correct_option
            if option_a is not None:
                exam.option_a = option_a
            if option_b is not None:
                exam.option_b = option_b
            if option_c is not None:
                exam.option_c = option_c
            if option_d is not None:
                exam.option_d = option_d
            exam.updated_at = updated_at


            db.session.commit()

            return response.success("", "Exam has been updated")
        else:
            return "Update exam is failed"
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def delete_exam(id):
    try:
        exam = Exam.query.filter_by(id).first()
        if not exam:
            return response.badRequest([], "Exam not found")
        db.session.delete(exam)
        db.session.commit()

        return response.success("", "Data Exam has been deleted")
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500