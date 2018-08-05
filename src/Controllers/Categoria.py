from flask import request
from flask_restful import Resource
from src.Models.Categoria import db, Category, CategorySchema

categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        categories = categories_schema.dump(categories).data
        return {'status': 'sucesso', 'data': categories}, 200
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Nenhum dado de entrada fornecido'}, 400
        # Validar e desserializar entrada
        data, errors = category_schema.load(json_data)
        if errors:
            return errors, 422
        category = Category.query.filter_by(name=data['name']).first()
        if category:
            return {'message': 'Categoria já existe'}, 400
        category = Category(
            name=json_data['name']
            )

        db.session.add(category)
        db.session.commit()

        result = category_schema.dump(category).data

        return { "status": 'sucesso', 'data': result }, 201