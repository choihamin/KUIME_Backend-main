from flask import Flask
from flask_login import LoginManager

def create_app():
    # 앱 설정
    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(app)  # app 에 login_manager 연결
    return app



