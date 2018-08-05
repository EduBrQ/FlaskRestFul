from flask import jsonify, request
from flask_restful import Resource
from src.Models.Comentario import db, Comment, CommentSchema
from src.Models.Categoria import Category

comments_schema = CommentSchema(many=True)
comment_schema = CommentSchema()

class CommentResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema.dump(comments).data
        return {"status":"sucesso", "data":comments}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Nenhum dado de entrada fornecido'}, 400
        # Validar e desserializar entrada
        data, errors = comment_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        category_id = Category.query.filter_by(id=data['category_id']).first()
        if not category_id:
            return {'status': 'error', 'message': 'categoria de comentário não encontrada'}, 400
        comment = Comment(
            category_id=data['category_id'], 
            comment=data['comment']
            )
        db.session.add(comment)
        db.session.commit()

        result = comment_schema.dump(comment).data

        return {'status': "sucesso", 'data': result}, 201

    # Voce pode adicionar outros metodos aqui