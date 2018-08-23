from api import bp


@bp.route('/hello', methods=['GET'])
def hello():
    return "Hello World!!!"
