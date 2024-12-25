from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return 'Webチャットサーバー稼働中'

@socketio.on('connect')
def handle_connect():
    user_id = str(uuid.uuid4())
    users[user_id] = request.sid
    emit('userId', user_id)

@socketio.on('join')
def handle_join(data):
    target_id = data['target_id']
    if target_id in users:
        join_room(target_id)
        join_room(request.sid)
        emit('message', '新しいユーザーが参加しました', room=target_id)

@socketio.on('message')
def handle_message(data):
    target_id = data['target_id']
    message = data['message']
    emit('message', message, room=target_id)

@socketio.on('disconnect')
def handle_disconnect():
    user_id = next((uid for uid, sid in users.items() if sid == request.sid), None)
    if user_id:
        del users[user_id]

if __name__ == '__main__':
    socketio.run(app)
