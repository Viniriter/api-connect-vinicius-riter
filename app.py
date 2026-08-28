from flask import Flask, jsonify
from routes.user_routes import user_bp

app = Flask(__name__)

# Rota base
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "API Connect iniciada com sucesso!"
    }), 200

# Registro das rotas modulares
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
