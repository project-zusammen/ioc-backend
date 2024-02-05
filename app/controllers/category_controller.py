from app.models.category import Category
from app import response, app, db
from flask import request, jsonify


def get_all_category():
    try:
        categories = Category.query.all()
        return jsonify(
            {
                "categories": [
                    {"id": category.id, "name": category.name}
                    for category in categories
                ]
            }
        )
    except Exception as e:
        print(e)


def get_category_by_id(id):
    try:
        category = Category.query.get(id)

        if category:
            data = {"id": category.id, "name": category.name}
            return jsonify(data)
        else:
            return jsonify({"error": "Category not found"})
    except Exception as e:
        print(e)


def create_category():
    try:
        name = request.form.get("name")
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return response.success("", "Category has been created")
    except Exception as e:
        print(e)


def delete_category(id):
    try:
        category = Category.query.filter_by(id=id).first()
        if not category:
            return response.badRequest([], "Category not found")
        db.session.delete(category)
        db.session.commit()

        return response.success("", "Category has been deleted")
    except Exception as e:
        print(e)
