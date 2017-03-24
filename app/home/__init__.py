from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
from . import service
from . import cloud
from . import data
from . import temp
