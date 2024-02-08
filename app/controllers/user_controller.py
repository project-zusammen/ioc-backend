from app.models.user import User
from app import response, app, db
from flask import request, jsonify
import datetime
from flask_jwt_extended import *

def get_all_users():
    try:
        users = User.query.all()
        return jsonify({'users': [
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'school': user.school,
                'role': user.role,
                'grade': user.grade,
                'dob': user.dob,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            } for user in users
        ]})
    except Exception as e:
        print(e)

def get_user_by_id(id):
    try:
        user = User.query.get(id)

        if user:
            data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'school': user.school,
                'role': user.role,
                'grade': user.grade,
                'dob': user.dob,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            }
            return jsonify(data)
        else:
            return jsonify({'error': 'User not found'}), 404
        
    except Exception as e:
        print(e)

def register():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        school = request.form.get('school')
        role = request.form.get('role')
        grade = request.form.get('grade')
        dob = request.form.get('dob')
        if dob is None:
            dob = '-'

        user = User(
            name=name,
            email=email,
            school=school,
            role = role,
            grade=grade,
            dob=dob
            )
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()
        
        return response.success(user, 'User has been created')
    except Exception as e:
            print(e)
            return jsonify({user})

def update_user(id):
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        school = request.form.get('school')
        role = request.form.get('role')
        grade = request.form.get('grade')
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
            user.updated_at = updated_at

            db.session.commit()

            return 'Data user has been updated'

        else:
            return 'Update data failed'
    
    except Exception as e:
        print(e)

def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'User not found')
        db.session.delete(user)
        db.session.commit()

        return response.success('', 'Data user has been deleted')
    
    except Exception as e:
        print(e)

def userData(data):
    data = {
        'name': data.name,
        'email': data.email,
        'school': data.school,
        'grade': data.grade,
        'role': data.role,
        'dob': data.dob,
    }

    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([], 'email or password are incorrect')
        
        if not user.checkPassword(password):
            return response.badRequest([], 'email or password are incorrect')
        
        data = userData(user)

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=10)

        access_token = create_access_token(data, fresh=True, expires_delta= expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            'data': data,
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 'Login Success')

    except Exception as e:
        print(e)

