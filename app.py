from flask import Flask, jsonify, request
from routes.user_routes import user_bp

app = Flask(__name__)

# Middleware para validar e preparar o parsing de JSON
@app.before_request
def processar_json():
    if request.method in ["POST", "PUT", "PATCH"] and request.is_json:
        request.parsed_data = request.get_json()

# Rota base
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "API Connect iniciada com sucesso!"
    }), 200

# Registro das rotas modulares de usuários
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
