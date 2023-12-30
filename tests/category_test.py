import unittest
from app import db, app 
from app.models.category import Category
class CategoryTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

        with app.app_context():
            category1= Category(name='Fisika')
            category2= Category(name='Biologi')
            db.session.add_all([category1, category2])
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_category(self):
        response = self.client.get('/category')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('categories', data)

        if 'Categories' in data:
            for category in data['Categories']:
                self.assertIn('name', category)
    
    def test_get_category_by_id(self):
        id = 1 
        response = self.client.get(f'/category/{id}')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', data)
        if 'id' in data:
            self.assertEqual(data['id'], id)
            self.assertIn('name', data)

    def test_add_category(self):
        category_name = {
            'name': 'Fisika'
        }
        response = self.client.post('/category', data=category_name)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('category', data)
        category = data['category']
        self.assertIn('id', category)
        self.assertEqual(category['name'], category_name['name'])

    def test_delete_category(self):
        with app.app_context():
            category = Category.query.filter_by(id=1).first()
            self.assertIsNotNone(category, "Category not found")

            response = self.client.delete(f'/category/{category.id}')

            self.assertEqual(response.status_code, 200)

            deleted_category = Category.query.get(category.id)
            self.assertIsNone(deleted_category, "Category already deleted")
if __name__ == '__main__':
    unittest.main()
