from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes.Movie import main

app = Flask(__name__)

#members API Route

@app.route("/members")
def members():
    return {"members":["Member1","Member2","Member3"]}

#CORS(app, resources={"*": {"origins": "http://localhost:9300"}}) #toda la app habilitada con esto


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(main, url_prefix='/api/movies')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()