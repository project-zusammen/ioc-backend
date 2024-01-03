import unittest
from app import app, db
from app.models.user import User
from datetime import datetime
from werkzeug.security import generate_password_hash


class UserTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

        with app.app_context():
            hashed_password = generate_password_hash("1234")
            user1 = User(
                name="Updated John Doe",
                email="jhon@gmail.com",
                password=hashed_password,
                grade="10",
                school="SMKN 1 Jakarta",
                role="Students",
                dob=datetime(year=2002, month=5, day=15),
            )

            hashed_password = generate_password_hash("1234")
            user2 = User(
                name="Jane Doe",
                email="jane@gmail.com",
                password=hashed_password,
                grade="10",
                school="SMKN 1 Jakarta",
                role="Students",
                dob=datetime(year=2002, month=5, day=15),
            )

            hashed_password = generate_password_hash("1234")
            user3 = User(
                name="James Doe",
                email="james@gmail.com",
                password=hashed_password,
                grade="10",
                school="SMKN 1 Jakarta",
                role="Students",
                dob=datetime(year=2002, month=5, day=15),
            )

            hashed_password = generate_password_hash("12345678")
            user4 = User(
                name="Joko",
                email="joko1@gmail.com",
                password=hashed_password,
                grade="10",
                school="SMKN 1 Jakarta",
                role="Students",
                dob=datetime(year=2002, month=5, day=15),
            )

            user1.created_at = (
                user2.created_at
            ) = user3.created_at = user4.created_at = datetime.utcnow()
            user1.updated_at = (
                user2.updated_at
            ) = user3.updated_at = user4.updated_at = datetime.utcnow()
            db.session.add_all([user1, user2, user3, user4])
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login_success(self):
        user_login = {
            "email": "jane@gmail.com",
            "password": "1234",
        }
        response = self.client.post("/login", data=user_login)
        print(response.json)
        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json)
        self.assertIn("access_token", response.json["data"])
        self.assertIn("refresh_token", response.json["data"])
        self.assertEqual(response.json["message"], "Login Success")

    def test_update_user(self):
        with app.app_context():
            user = User.query.filter_by(id=1).first()
            self.assertIsNotNone(user, "Tidak ada pengguna dalam database")

            response = self.client.put(
                f"/user/{user.id}", json={"id": user.id, "name": "Updated Jhon"}
            )

            self.assertEqual(
                response.status_code,
                200,
                f"Kode status yang diharapkan adalah 200, tetapi mendapatkan {response.status_code}",
            )

            updated_user = User.query.get(user.id)
            self.assertEqual(
                updated_user.name,
                "Updated John Doe",
                "Nama pengguna tidak diperbarui dalam database",
            )

    def test_get_all_users(self):
        response = self.client.get("/user")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        self.assertIn("users", data)

        if "users" in data:
            for user in data["users"]:
                self.assertIn("name", user)
                self.assertIn("email", user)
                self.assertIn("school", user)
                self.assertIn("role", user)
                self.assertIn("grade", user)
                self.assertIn("dob", user)
                self.assertIn("created_at", user)
                self.assertIn("updated_at", user)

    def test_get_user_by_id(self):
        id = 1
        response = self.client.get(f"/user/{id}")

        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", data)
        if "id" in data:
            self.assertEqual(data["id"], id)
            self.assertIn("name", data)
            self.assertIn("email", data)
            self.assertIn("school", data)
            self.assertIn("role", data)
            self.assertIn("grade", data)
            self.assertIn("dob", data)
            self.assertIn("created_at", data)
            self.assertIn("updated_at", data)

    def test_add_user(self):
        user_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "password123",
            "school": "SMKN 2 Bandung",
            "role": "Teacher",
            "grade": "-",
        }

        response = self.client.post("/register", data=user_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("user", data)
        user = data["user"]
        self.assertIn("id", user)
        self.assertEqual(user["name"], user_data["name"])
        self.assertEqual(user["email"], user_data["email"])
        self.assertEqual(user["school"], user_data["school"])
        self.assertEqual(user["role"], user_data["role"])
        self.assertEqual(user["grade"], user_data["grade"])
        self.assertIn("created_at", user)
        self.assertIn("updated_at", user)

    def test_delete_user(self):
        with app.app_context():
            user = User.query.filter_by(id=1).first()
            self.assertIsNotNone(user, "user not found")

            response = self.client.delete(f"/user/{user.id}")

            self.assertEqual(response.status_code, 200)

            deleted_user = User.query.get(user.id)
            self.assertIsNone(deleted_user, "user not found")


if __name__ == "__main__":
    unittest.main()
