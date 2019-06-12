from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from . import pvtdisplay
from .. import socketio
from flask_socketio import send, emit


@pvtdisplay.route("/display", methods=["GET"])
def display_screen():
    return render_template("subject_display.html")


@pvtdisplay.route("/button", methods=["get"])
def display_button():
    return render_template("tapper.html")


@pvtdisplay.route("/control", methods=["get"])
def display_control():
    return render_template("control.html")


@socketio.on("button")
def test_message(message):
    print(message)
    if message == "tapped":
        emit("screen", {"action": "tapped"}, broadcast=True)


@socketio.on("control")
def control(message):
    print(message)
    to, action = message["to"], message["action"]
    if to == "pvt":
        if action == "start":
            emit(
                "screen",
                {"action": "show", "duration": message["duration"]},
                broadcast=True,
            )
