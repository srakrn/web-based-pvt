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

bp = Blueprint("pvt", __name__, url_prefix="/pvt")


@bp.route("/display", methods=["GET"])
def display_screen():
    return render_template("subject_display.html")
