from flask import render_template
from . import main_blueprint as main
#from .. import db
#from ..models import TableName

@main.route('/')
def index():
    return render_template('index.html')
