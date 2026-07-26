from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [{"id": 1, "titulo": "Estudar Flask", "feita": True}]


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.get_json()

    if (
        not nova_tarefa
        or "titulo" not in nova_tarefa
        or not str(nova_tarefa["titulo"]).strip()
    ):
        return (
            jsonify({"erro": "O campo titulo e obrigatorio e nao pode ser vazio"}),
            400,
        )

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


if __name__ == "__main__":
    app.run(debug=True)
