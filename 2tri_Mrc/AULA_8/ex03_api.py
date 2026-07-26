from datetime import date
from flask import Flask

app = Flask(__name__)


@app.route("/saudacao")
def saudacao():
    return "Seja muito bem-vindo à nossa API!"


@app.route("/data")
def mostrar_data():
    hoje = date.today()
    # strftime('%d/%m/%Y') formata a data para o padrao Dia/Mes/Ano
    data_formatada = hoje.strftime("%d/%m/%Y")
    return f"A data de hoje é: {data_formatada}"


if __name__ == "__main__":
    app.run(debug=True)