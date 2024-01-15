from app.models.score import Score
from app.models.exam import Exam
from app import response, app, db
from flask import request, jsonify
from flask_jwt_extended import *


def create_score():
    try:
        # id = request.form.get('id')
        user_id = request.form.get('user_id')
        exam_id = request.form.get('exam_id')
        score = request.form.get('score')

        new_score = Score(
            # id=id,
            user_id=user_id,
            exam_id=exam_id,
            score=score,
        )

        db.session.add(new_score)
        db.session.commit()

        return response.success('', f'Score for user with id {user_id} and exam_id {exam_id} successfully added')
    except Exception as e:
        print(e)
        return response.internal_server_error()


def get_all_scores():
    try:
        scores = Score.query.all()
        return jsonify({'scores': [
            {
                'id': score.id,
                'user_id': score.user_id,
                'exam_id': score.exam_id,
                'score': score.score,
                'created_at': score.created_at,
            } for score in scores
        ]})
    except Exception as e:
        print(e)
        return response.internal_server_error()


def get_score_by_id(id):
    try:
        score = Score.query.filter_by(id=id).first()
        if score:
            return jsonify({'scores': {
                'id': score.id,
                'user_id': score.user_id,
                'exam_id': score.exam_id,
                'score': score.score,
                'created_at': score.created_at,
            }})
        else:
            return response.badRequest([], f'Score not found for this score id: {id}')

    except Exception as e:
        print(e)
        return response.internal_server_error()


def get_scores_by_user_id():
    try:
        user_id = request.form.get('user_id')

        scores = Score.query.filter_by(user_id=user_id).all()

        if scores:
            return jsonify({'scores': [
                {
                    'id': score.id,
                    'user_id': score.user_id,
                    'exam_id': score.exam_id,
                    'score': score.score,
                    'created_at': score.created_at,
                } for score in scores
            ]})
        else:
            return response.badRequest([], f'Scores not found for this user id: {user_id}')

    except Exception as e:
        print(e)
        return response.internal_server_error()


def get_scores_by_exam_id():
    try:
        exam_id = request.form.get('exam_id')

        scores = Score.query.filter_by(exam_id=exam_id).all()

        if scores:
            return jsonify({'scores': [
                {
                    'id': score.id,
                    'user_id': score.user_id,
                    'exam_id': score.exam_id,
                    'score': score.score,
                    'created_at': score.created_at,
                } for score in scores
            ]})
        else:
            return response.badRequest([], f'Scores with exam_id = {exam_id} not found')

    except Exception as e:
        print(e)
        return response.internal_server_error()


def update_score(id):
    try:
        new_score = request.form.get('score')
        user_id = request.form.get('user_id')
        exam_id = request.form.get('exam_id')

        score = Score.query.filter_by(id=id).first()

        if score:
            # make sure the updating process on database not messing up
            try:
                if new_score is not None:
                    score.score = new_score
                if user_id is not None:
                    score.user_id = user_id
                if exam_id is not None:
                    score.exam_id = exam_id

                db.session.commit()

                updated_data = Score.query.filter_by(id=id).first()

                return jsonify({"Update Success": {
                    "id": updated_data.id,
                    "score": updated_data.score,
                    "user_id": updated_data.user_id,
                    "exam_id": updated_data.exam_id,
                }})

            except Exception as e:
                print(e)
                return jsonify({"Error": "There are problems in updating score data."})

        else:
            return response.badRequest([], f'Score with id = {id} not found')

    except Exception as e:
        print(e)
        return jsonify({"Error": "There are problems in updating score data."})


def delete_score(id):
    try:
        score = Score.query.filter_by(id=id).first()
        if not score:
            return response.badRequest([], f'Score with id = {id} not found')
        db.session.delete(score)
        db.session.commit()

        return response.success('', f'Score with id = {id} has been deleted')

    except Exception as e:
        print(e)
        return jsonify({"Error": "There are problems in deleting score data."})
