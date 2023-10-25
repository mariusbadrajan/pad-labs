from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.accounts import bp as accounts_bp
from app.transactions import bp as transactions_bp


def create_app():
    app = Flask(__name__)
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["5/second"],
    )

    # Register blueprints here
    app.register_blueprint(accounts_bp, url_prefix='/accounts')
    app.register_blueprint(transactions_bp, url_prefix='/transactions')

    return app
