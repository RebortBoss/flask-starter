from flask import render_template

from . import app, log


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    """
    Allow Flask debug to render exceptions when we're not in production.

    """
    @app.errorhandler(Exception)
    def unhandled_exception(e):
        log.exception(e)
        return server_error(str(e))
