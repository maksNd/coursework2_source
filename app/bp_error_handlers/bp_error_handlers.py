from flask import Blueprint, render_template

bp_error_handlers = Blueprint('bp_error_handlers', __name__, template_folder='templates')


@bp_error_handlers.app_errorhandler(404)
def page_not_found(error):
    return render_template('no_page_404.html'), 404


@bp_error_handlers.app_errorhandler(500)
def page_server_error(error):
    return render_template('server_error_500.html'), 500
