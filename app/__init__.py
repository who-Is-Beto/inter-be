from flask import Flask
from flask_smorest import Api
from app.resources.user import blueprint

app = Flask(__name__)

app.config["API_TITLE"] = "Inter REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/doc"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(blueprint)