from app.models import category
from app.models.material import Material
from app.models.user import User
from app import response, app, db
from flask import request, jsonify
from flask_jwt_extended import *
import datetime

def format_material(material):
    return {
        "id": material.id,
        "title": material.title,
        "content": material.content,
        "user_id": material.user_id,
        "category_id": material.category_id,
        "created_at": material.created_at,
        "updated_at": material.updated_at
    }

def get_all_materials():
    try:
        materials = Material.query.all()
        formated_materials = [format_material(material) for material in materials]
        return jsonify({"materials": formated_materials})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def get_material_by_id(id):
    try:
        GetMaterial = Material.query.get(id)
        if GetMaterial:
            material = {
                "id": GetMaterial.id,
                "title": GetMaterial.title,
                "content": GetMaterial.content,
                "user_id": GetMaterial.user_id,
                "category_id": GetMaterial.category_id,
                "created_at": GetMaterial.created_at,
                "updated_at": GetMaterial.updated_at
            }
            return jsonify(material)
        else:
            return jsonify({"error": "Material not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def create_material():
    try:
        current_user_data = get_jwt_identity()
        user = User.query.get(current_user_data["id"])

        title = request.form.get("title")
        content = request.form.get("content")
        user_id = user.id
        category_id = request.form.get("category_id")

        material = Material(
            title=title,
            content=content,
            user_id=user_id,
            category_id = category_id
        )
        db.session.add(material)
        db.session.commit()
        return jsonify({"material": format_material(material)})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def update_material(id):
    try: 
        title = request.form.get("title")
        content = request.form.get("content")
        category_id = request.form.get("category_id")
        updated_at = datetime.datetime.utcnow()

        material = Material.query.filter_by(id=id).first()

        if material:
            if title is not None:
                material.title = title
            if content is not None:
                material.content = content
            if category_id is not None:
                material.category_id = category_id
            material.updated_at = updated_at

            db.session.commit()
            return response.success("", "Material has been updated")
        else:
            return "Update material is failed"
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def delete_material(id):
    try:
        material = Material.query.filter_by(id=id).first()
        if not material:
            return response.badRequest([], "Material not found")
        db.session.delete(material)
        db.session.commit()
        
        return response.success("", "Data material has been deleted")
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500