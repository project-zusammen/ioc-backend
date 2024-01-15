import unittest
from flask import Flask
from app import db, app
from app.models.score import Score
from app.models.exam import Exam
from app.models.user import User
from werkzeug.security import generate_password_hash
from datetime import datetime
from app.controllers.score_controller import create_score, get_all_scores, get_score_by_id, get_scores_by_user_id, get_scores_by_exam_id, update_score, delete_score


class ScoreControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app and configure it
        # self.app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Create a test client
        self.client = app.test_client()

        # Set up the test database
        # db.init_app(self.app)
        with app.app_context():
            db.create_all()

        with app.app_context():
            hashed_password = generate_password_hash("1234")
            user1 = User(
                id=1,
                name="John Doe",
                email="jhon@gmail.com",
                password=hashed_password,
                grade="10",
                school="SMKN 1 Jakarta",
                role="Students",
                dob=datetime(year=2002, month=5, day=15),
            )
            user1.created_at = datetime.utcnow()
            db.session.add(user1)
            db.session.commit()

            exam1 = Exam(id=1, material_id=1, question="Hello Mom dan Dad.")
            db.session.add(exam1)
            db.session.commit()

            score1 = Score(id=1, user_id=1, exam_id=1, score=95)
            score2 = Score(id=2, user_id=1, exam_id=1, score=100)
            db.session.add_all([score1, score2])
            db.session.commit()

    def tearDown(self):
        # Clean up the test database
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_score(self):
        # Write your test for create_score here
        pass

    def test_get_all_scores(self):
        response = self.client.get('/score')
        data = response.get_json()
        print(data)
        self.assertEqual(response.status_code, 200)
        # self.assertIn('categories', data)

        # if 'Categories' in data:
        #     for category in data['Categories']:
        #         self.assertIn('name', category)

    def test_get_score_by_id(self):
        # Write your test for get_score_by_id here
        pass

    def test_get_scores_by_user_id(self):
        # Write your test for get_scores_by_user_id here
        pass

    def test_get_scores_by_exam_id(self):
        # Write your test for get_scores_by_exam_id here
        pass

    def test_update_score(self):
        # Write your test for update_score here
        pass

    def test_delete_score(self):
        # Write your test for delete_score here
        pass


if __name__ == '__main__':
    unittest.main()
