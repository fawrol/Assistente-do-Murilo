from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo123'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    nome = request.remote_addr  # IP como nome básico
    mensagem_formatada = f"{nome}: {msg}"
    send(mensagem_formatada, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
