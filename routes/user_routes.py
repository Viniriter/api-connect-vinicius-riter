from flask import Blueprint
from controllers.user_controller import (
    list_all_users,
    create_new_user,
    get_user_by_id,
    update_user_by_id,
    delete_user_by_id
)

user_bp = Blueprint("users", __name__, url_prefix="/users")

# Rota para listagem geral (GET /users)
@user_bp.route("", methods=["GET"])
def get_users():
    return list_all_users()

# Rota para cadastro de novo usuário (POST /users)
@user_bp.route("", methods=["POST"])
def post_user():
    return create_new_user()

# Rota para busca específica por identificador (GET /users/<int:user_id>)
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return get_user_by_id(user_id)

# Rota para atualização de usuário (PUT /users/<int:user_id>)
@user_bp.route("/<int:user_id>", methods=["PUT"])
def put_user(user_id):
    return update_user_by_id(user_id)

# Rota para remoção de usuário (DELETE /users/<int:user_id>)
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return delete_user_by_id(user_id)
