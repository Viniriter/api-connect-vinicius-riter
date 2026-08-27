# Estrutura em memória para persistência temporária dos dados de usuários (MVP)
users = [
    {
        "id": 1,
        "name": "Vinicius Riter",
        "email": "vinicius.riter@email.com"
    },
    {
        "id": 2,
        "name": "Evelin Lubas",
        "email": "evelin.lubas@email.com"
    }
]

# Controle de estado para geração sequencial de identificadores únicos
_current_id = 2

def generate_next_id():
    """Incrementa e retorna um novo ID sequencial único para o cadastro."""
    global _current_id
    _current_id += 1
    return _current_id
