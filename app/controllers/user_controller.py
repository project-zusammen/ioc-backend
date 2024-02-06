from app.models.user import User
from app import response, app, db
from flask import request, jsonify
import datetime
from flask_jwt_extended import *

def format_user(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "school": user.school,
        "role": user.role,
        "grade": user.grade,
        "dob": user.dob,
        "created_at": user.created_at,
        "updated_at": user.updated_at,
    }

def get_all_users():
    try:
        users = User.query.all()
        formatted_users = [format_user(user) for user in users]
        return jsonify({"users": formatted_users})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500



def get_user_by_id(id):
    try:
        GetUser = User.query.get(id)
        
        if GetUser:
            user = {
                "id": GetUser.id,
                "name": GetUser.name,
                "email": GetUser.email,
                "school": GetUser.school,
                "role": GetUser.role,
                "grade": GetUser.grade,
                "dob": GetUser.dob,
                "created_at": GetUser.created_at,
                "updated_at": GetUser.updated_at,
              
            return jsonify(user)
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500



def register():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        school = request.form.get("school")
        role = request.form.get("role")
        grade = request.form.get("grade")
        dob = request.form.get("dob")
        if dob is None:
            dob = "-"

        user = User(
            name=name, email=email, school=school, role=role, grade=grade, dob=dob
        )
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()

        return jsonify(
            {
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "school": user.school,
                    "role": user.role,
                    "grade": user.grade,
                    "dob": user.dob,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                }
            }
        )
              
        return response.success("", "User has been created")
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


def update_user(id):
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        school = request.form.get("school")
        role = request.form.get("role")
        grade = request.form.get("grade")
        dob = request.form.get("dob")
        updated_at = datetime.datetime.utcnow()
        updated_at = datetime.utcnow

        user = User.query.filter_by(id=id).first()

        if user:
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            if password is not None:
                user.password = password
                user.setPassword(user.password)
            if school is not None:
                user.school = school
            if role is not None:
                user.role = role
            if grade is not None:
                user.grade = grade
            if dob is not None:
                user.dob = dob
            user.updated_at = updated_at

            db.session.commit()

            return response.success("", "data user has been updated")
        else:
            return response.badRequest([], "Failed updating user data, user not found")

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500



def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")
        db.session.delete(user)
        db.session.commit()

        return response.success("", "Data user has been deleted")

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500



def userData(data):
    data = {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "school": data.school,
        "grade": data.grade,
        "role": data.role,
        "dob": data.dob,
    }

    return data


def login():
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([], "email or password are incorrect")

        if not user.checkPassword(password):
            return response.badRequest([], "email or password are incorrect")

        data = userData(user)

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=10)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success(
            {
                "data": data,
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            "Login Success",
        )

    except Exception as e:
        print(e)
