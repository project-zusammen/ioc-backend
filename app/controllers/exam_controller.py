from app.models.exam import Exam
from app.models.user import User
from app import response, app, db
from flask import request, jsonify
from flask_jwt_extended import *
import datetime

def format_exam(exam):
    return {
        "id": exam.id,
        "title": exam.title,
        "description": exam.description,
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
                "title": GetExam.title,
                "description": GetExam.description,
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

        title = request.form.get("title")
        description = request.form.get("description")
        user_id =  user.id
        material_id = request.form.get("material_id")

        exam = Exam(
            title=title,
            description=description,
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
        title = request.form.get("title")
        description = request.form.get("description")
        updated_at = datetime.datetime.utcnow()

        exam = Exam.query.filter_by(id=id).first()

        if exam:
            if title is not None:
                exam.title = title
            if description is not None:
                exam.description = description
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