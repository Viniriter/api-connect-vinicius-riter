from flask import request, jsonify
from data.database import users, generate_next_id

def list_all_users():
    """Recupera e retorna a lista completa de usuários cadastrados."""
    return jsonify(users), 200

def create_new_user():
    """Cadastra um novo usuário com validação de campos e resposta padronizada."""
    data = request.get_json()

    # 1. Trava: Verifica se o corpo da requisição existe e é um JSON válido
    if not data or not isinstance(data, dict):
        return jsonify({
            "error": "Corpo da requisição vazio ou formato JSON inválido."
        }), 400

    name = data.get("name")
    email = data.get("email")

    # 2. Trava: Garante que 'name' existe, é texto e não está em branco
    if not name or not isinstance(name, str) or not name.strip():
        return jsonify({
            "error": "O campo 'name' é obrigatório e deve ser preenchido."
        }), 400

    # 3. Trava: Garante que 'email' existe, é texto e não está em branco
    if not email or not isinstance(email, str) or not email.strip():
        return jsonify({
            "error": "O campo 'email' é obrigatório e deve ser preenchido."
        }), 400

    # 4. Processamento: Criação do registro com dados limpos
    new_user = {
        "id": generate_next_id(),
        "name": name.strip(),
        "email": email.strip()
    }
    users.append(new_user)

    # 5. Resposta de sucesso padronizada no envelope 'data'
    return jsonify({
        "data": new_user,
        "message": "Usuário cadastrado com sucesso."
    }), 201

def get_user_by_id(user_id):
    """Busca e retorna um único usuário pelo ID recebido via parâmetro de rota."""
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({
            "error": f"Usuário com ID {user_id} não encontrado."
        }), 404

    return jsonify(user), 200

def update_user_by_id(user_id):
    """Atualiza dados do usuário garantindo que campos enviados não sejam vazios."""
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": f"Usuário com ID {user_id} não encontrado."}), 404

    data = request.get_json()
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Corpo da requisição vazio ou formato JSON inválido."}), 400

    # Validação condicional: só valida se a chave existir no payload
    if "name" in data:
        name = data.get("name")
        if not isinstance(name, str) or not name.strip():
            return jsonify({"error": "O campo 'name' não pode ser vazio."}), 400
        user["name"] = name.strip()

    if "email" in data:
        email = data.get("email")
        if not isinstance(email, str) or not email.strip():
            return jsonify({"error": "O campo 'email' não pode ser vazio."}), 400
        user["email"] = email.strip()

    return jsonify({
        "data": user,
        "message": "Usuário atualizado com sucesso."
    }), 200

def delete_user_by_id(user_id):
    """Remove um usuário do sistema com base no ID."""
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({
            "error": f"Usuário com ID {user_id} não encontrado."
        }), 404

    users.remove(user)
    return "", 204
