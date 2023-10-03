from flask import Flask, request, render_template

app = Flask(__name__)


respostas = ['Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5']

@app.route('/')
def index():
    return render_template('lista.html', titulo='webAPP')

@app.route('/processar_pergunta', methods=['POST'])
def processar_pergunta():
    pergunta_do_usuario = request.form['perguntas']
    # xao aqui vc pode processar a pergunta do usuário e gerar uma resposta usando a variável 'respostas'.
    # Por exemplo, você pode usar a pergunta para determinar o índice da resposta a ser exibida.
    resposta = respostas[0]  # Exemplo simples, assumindo que a primeira resposta seja a correta.

    return render_template('resultado.html', resposta=resposta)

if __name__ == '__main__':
    app.run()
