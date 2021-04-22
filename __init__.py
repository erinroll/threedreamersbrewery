#import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)

#functions for web application
def create_app():
    app.debug= True
    app.secret_key='thisisasecretkey'

    #connect database
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///threedreamersbrewery.sqlite'

    #initialize db with flask app
    db.init_app(app)

    bootstrap = Bootstrap(app)

    #import modules
    from . import views
    app.register_blueprint(views.bp)

    return app

@app.errorhandler(404)
#function for error as parameter
def not_found(e):
    return render_template('404.html')

@app.errorhandler(500) 
def internal_error(e):
    return render_template('500.html')

    