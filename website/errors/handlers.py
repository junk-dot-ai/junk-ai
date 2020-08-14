from flask import Blueprint, render_template


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def error_403(error):
    print("HANDLING ERROR 403");
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def error_404(error):
    print("HANDLING ERROR 404");
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def error_500(error):
    print("HANDLING ERROR 500");
    return render_template('errors/500.html'), 500


@errors.app_errorhandler(502)
def error_502(error):
    print("HANDLING ERROR 502");
    return render_template('errors/502.html'), 502