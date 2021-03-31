from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment 
from config import Config 
from flask_login import LoginManager


#instantiate the objects first, then create_app function can use them
# delete the (app) move them down to create_app to instantiate the app   
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
login_manager = LoginManager()
login_manager.login_view = 'auth.login' #protect the route being accessed by non-login users
login_manager.login_message = 'You do not have access to this page. Login first, please!'
login_manager.login_message_category = 'warning'

#Application Factory Pattern
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config) 
    
    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login_manager.init_app(app)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    #importing bp instance 
    from app.blueprints.auth import bp as auth_bp 
    # register blueprint to our main app
    app.register_blueprint(auth_bp)

    from app.blueprints.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    # needs app context 
    # with app.app_context():
        # from app import views # no longer have access to app.views since it's moved 
    

    return app 
