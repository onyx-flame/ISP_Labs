from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager, login_manager, current_user
from werkzeug import debug
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

from project.models import *

login_manager = LoginManager()
socketio = SocketIO()
login_manager.login_view = "users.login"

admin = Admin()

class UserView(ModelView):
    column_list = ['id', 'username', 'password', 'sid', 'is_admin']


class ChatView(ModelView):
    column_list = ['id', 'unread_messages_number']
    
    
class MessageView(ModelView):
    column_list = ['id', 'text', 'unread', 'date', 'user', 'chat']
    

class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        return not current_user.is_anonymous and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        abort(404)


def create_app(config_string="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_string)
    
    initialize_extensions(app)
    register_blueprints(app)
    
    admin.init_app(app, url='/', index_view=HomeAdminView(name='Home'))
    admin.add_view(UserView(User, db.session))
    admin.add_view(ChatView(Chat, db.session))
    admin.add_view(MessageView(Message, db.session))
    
    socketio.init_app(app, cors_allowed_origins='*')
    return app


def initialize_extensions(app):
    db.init_app(app)
    
    login_manager.init_app(app)

    from project.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

def register_blueprints(app):
    from project.social import social_blueprint
    from project.users import users_blueprint

    app.register_blueprint(social_blueprint)
    app.register_blueprint(users_blueprint)
