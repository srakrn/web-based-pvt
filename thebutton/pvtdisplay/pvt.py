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


@pvtdisplay.route("/display", methods=["GET"])
def display_screen():
    return render_template("subject_display.html")


@socketio.on("response")
def test_message(message):
    print("Hello")
