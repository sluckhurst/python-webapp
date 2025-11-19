from flask import Flask

from flask_wtf.crsf import CSRFProtect

app = Flask(__name__)

crsf = CSRFProtect
crsf.init_app(app)git status

from application import routes


