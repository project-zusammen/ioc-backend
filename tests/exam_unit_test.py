import unittest
from flask_jwt_extended import create_access_token
from app import db, app, response
from app.models.exam import Exam
from app.models.user import User
from app.models.material import Material
from app.models.category import Category
from datetime import datetime
from werkzeug.security import generate_password_hash

class ExamTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
        app.config['JWT_SECRET_KEY'] = 'your_secret_key_for_testing'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

        with app.app_context():
            hashed_password = generate_password_hash("1234")
            user = User(
                name="Updated John Doe",
                email="jhon@gmail.com",
                password=hashed_password,
                grade="10",
                school="SMKN 1 Jakarta",
                role="Students",
                dob=datetime(year=2002, month=5, day=15),
            )

            category= Category(name='fisika`')
            db.session.add_all([user, category])
            db.session.commit()

            user_id = User.query.first().id

            material = Material(
                title='judul',
                content='content',
                user_id=user_id,
                category_id=category.id,
            )
            db.session.add(material)
            db.session.commit()

            exam1= Exam(question='1+1=?',
                        correct_option='2',
                        option_a='2',
                        option_b='1',
                        option_c='5',
                        option_d='14',
                        user_id=user_id,
                        material_id=material.id
                        )
            exam2= Exam(question='1+1=?',
                        correct_option='2',
                        option_a='2',
                        option_b='1',
                        option_c='5',
                        option_d='14',
                        user_id=user_id,
                        material_id=material.id
                        )
            db.session.add_all([exam1, exam2,])
            db.session.commit()
            

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_exam(self):
            with app.test_request_context():
                user_id = 1
                access_token = create_access_token(identity=user_id)
            headers = {'Authorization': 'Bearer {}'.format(access_token)}
            response = self.client.get('/exam', headers=headers)
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertIn('exams', data)

            if 'exams' in data:
                for exam in data['exams']:
                    self.assertIn('question', exam)
                    self.assertIn('option_a', exam)
                    self.assertIn('option_b', exam)
                    self.assertIn('option_c', exam)
                    self.assertIn('option_d', exam)
                    self.assertIn('user_id', exam)
                    self.assertIn('material_id', exam)

    def test_get_exam_by_id(self):
        with app.test_request_context():
            user_id = 1
            access_token = create_access_token(identity=user_id)
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = self.client.get(f'/exam/{user_id}', headers=headers)
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', data)
        if 'id' in data:
            self.assertEqual(data['id'], user_id)
            self.assertIn('question', data)
            self.assertIn('option_a', data)
            self.assertIn('option_b', data)
            self.assertIn('option_c', data)
            self.assertIn('option_d', data)
            self.assertIn('user_id', data)
            self.assertIn('material_id', data)
    
    def test_delete_exam(self):
        with app.app_context():
            user_id = 1
            exam_id = 1
            access_token = create_access_token(identity=user_id)
            headers = {'Authorization': 'Bearer {}'.format(access_token)}
            exam = Exam.query.filter_by(id=exam_id).first()
            self.assertIsNotNone(exam, "Exam not found")
            response = self.client.delete(f'/exam/{exam.id}', headers=headers)
            data = response.get_json()
            print(data)
            self.assertEqual(response.status_code, 200)

    def test_create_exam(self):
        with app.app_context():
            user_id = 1
            access_token = create_access_token(identity={"id": user_id})
        headers = {'Authorization': 'Bearer {}'.format(access_token)}

        exam_data = {
            'question': 'What is the capital of France?',
            'correct_option': 'Paris',
            'option_a': 'Berlin',
            'option_b': 'London',
            'option_c': 'Madrid',
            'option_d': 'Paris',
            'material_id': 1
        }

        response = self.client.post('/exam', headers=headers, data=exam_data)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('exam', data)
        exam = data['exam']
        self.assertIn("id", exam)
        self.assertEqual(exam["question"], exam_data["question"])
        self.assertEqual(exam["correct_option"], exam_data["correct_option"])
        self.assertEqual(exam["option_a"], exam_data["option_a"])
        self.assertEqual(exam["option_b"], exam_data["option_b"])
        self.assertEqual(exam["option_c"], exam_data["option_c"])
        self.assertEqual(exam["option_d"], exam_data["option_d"])
        self.assertEqual(exam["material_id"], exam_data["material_id"])
        self.assertEqual(exam["user_id"], user_id)
        self.assertIn("created_at", exam)
        self.assertIn("updated_at", exam)

    def test_update_exam(self):
        with app.app_context():
            user_id = 1
            access_token = create_access_token(identity={"id": user_id})
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        exam_id = 1
        data = {
            'option_a': 'Updated option A',
        }

        response = self.client.put(f'/exam/{exam_id}', headers=headers, data=data)
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Exam has been updated")
        
    
            

        
                    

if __name__ == '__main__':
    unittest.main()