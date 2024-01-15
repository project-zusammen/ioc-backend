import unittest
from flask import Flask
from app import db, app
from app.models.score import Score
from app.models.exam import Exam
from app.models.user import User
from werkzeug.security import generate_password_hash
from datetime import datetime


class ScoreControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app and configure it
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Create a test client
        self.client = app.test_client()

        # Set up the test database
        with app.app_context():
            db.create_all()

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

    # Your test methods...
    def test_create_score(self):
        # Write your test for create_score here
        pass


if __name__ == '__main__':
    unittest.main()
