from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config["SECRET_KEY"] = "supersecret"

    from .pvtdisplay import pvtdisplay as pvtdisplay_bp

    app.register_blueprint(pvtdisplay_bp)

    socketio.init_app(app)
    return app
