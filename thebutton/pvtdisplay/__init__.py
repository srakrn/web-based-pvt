from flask import Blueprint

pvtdisplay = Blueprint("pvtdisplay", __name__)

from . import pvt
