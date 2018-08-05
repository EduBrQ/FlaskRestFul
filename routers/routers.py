from flask import Blueprint
from flask_restful import Api

from src.Controllers.Categoria import CategoryResource
from src.Controllers.Comentario import CommentResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Rotas
api.add_resource(CategoryResource, '/Categorias')
api.add_resource(CommentResource, '/Comentarios')