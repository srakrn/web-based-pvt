import os
from flask import Flask
from flask_socketio import SocketIO
import pvt

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY="dev")
app.register_blueprint(pvt.bp)

socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app)
