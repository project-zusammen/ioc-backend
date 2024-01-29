import unittest
from flask import Flask
from app import db, app
from app.models.score import Score
from app.models.exam import Exam
from app.models.user import User
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime


class ScoreControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask app and configure it
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # Create a test client
        self.client = app.test_client()

        # Set up the test database
        with app.app_context():
            self.jwt_token = create_access_token(identity=1)
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
            exam2 = Exam(id=2, material_id=1, question="Hello Guyss.")
            db.session.add_all([exam1, exam2])
            db.session.commit()

            score1 = Score(id=1, user_id=1, exam_id=1, score=95)
            score2 = Score(id=2, user_id=1, exam_id=1, score=100)
            score3 = Score(id=3, user_id=1, exam_id=2, score=100)
            db.session.add_all([score1, score2, score3])
            db.session.commit()

    def tearDown(self):
        # Clean up the test database
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_score(self):
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        data = {"user_id": 1, "exam_id": 1, "score": 90}

        response = self.client.post("/score", data=data, headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Score for user with id 1 and exam_id 1 successfully added", response.data
        )

    def test_get_all_scores(self):
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get("/score", headers=headers)
        data = response.get_json()
        # print(data)
        self.assertEqual(response.status_code, 200)

        self.assertIn("scores", data)

        if "scores" in data:
            for score in data["scores"]:
                self.assertIn("score", score)

    def test_get_score_by_id(self):
        id = 1
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get(f"/score/{id}", headers=headers)
        data = response.get_json()
        user_data = data["scores"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_data["id"], id)

    def test_get_score_by_id_not_exist(self):
        id = 1000
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get(f"/score/{id}", headers=headers)
        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertEqual(data["message"], f"Score not found for this score id: {id}")

    def test_get_scores_by_user_id(self):
        user_data = {"user_id": 1}
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get(f"/scores_user_id", data=user_data, headers=headers)
        self.assertEqual(response.status_code, 200)

        data = response.get_json()["scores"]
        self.assertIn("score", data[0])
        self.assertEqual(user_data["user_id"], data[0]["user_id"])

    def test_get_scores_by_user_id_not_exist(self):
        user_data = {"user_id": 100}
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get(f"/scores_user_id", data=user_data, headers=headers)
        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertEqual(
            data["message"],
            f"Scores not found for this user id: {user_data['user_id']}",
        )

    def test_get_scores_by_exam_id(self):
        exam_data = {"exam_id": 1}
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get(f"/scores_exam_id", data=exam_data, headers=headers)

        self.assertEqual(response.status_code, 200)
        data = response.get_json()["scores"]

        self.assertEqual(2, len(data))
        self.assertIn("exam_id", data[0])

    def test_get_scores_by_exam_id_not_exist(self):
        exam_data = {"exam_id": 1000}
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.get(f"/scores_exam_id", data=exam_data, headers=headers)

        self.assertEqual(response.status_code, 400)
        data = response.get_json()

        self.assertEqual(
            data["message"], f"Scores with exam_id = {exam_data['exam_id']} not found"
        )

    def test_update_score(self):
        score_id = 2
        score_data = {"user_id": 1, "exam_id": 2, "score": 90}
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.put(
            f"/score/{score_id}", data=score_data, headers=headers
        )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()["Update Success"]

        self.assertEqual(data["id"], score_id)
        self.assertEqual(data["user_id"], score_data["user_id"])
        self.assertEqual(data["exam_id"], score_data["exam_id"])
        self.assertEqual(data["score"], score_data["score"])

    def test_delete_score(self):
        score_id = 3
        headers = {"Authorization": "Bearer {}".format(self.jwt_token)}
        response = self.client.delete(f"/score/{score_id}", headers=headers)

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(
            data["message"], f"Score with id = {score_id} has been deleted"
        )


if __name__ == "__main__":
    unittest.main()
