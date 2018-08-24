from flask import Blueprint

bp = Blueprint('healthcheck', url_prefix='/healthcheck', import_name=__name__)

@bp.route('/ping', methods=('GET', ))
def health_check():
   return "pong"


