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


@pvtdisplay.route("/button", methods=["GET"])
def display_button():
    return render_template("tapper.html")


@socketio.on("button")
def test_message(message):
    print(message)
    if message == "tapped":
        print("Tapped, emitting screen")
        emit("screen", "tapped", broadcast=True)
