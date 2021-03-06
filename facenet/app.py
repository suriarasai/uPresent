from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger
from src.routes import initialize_routes
import os
import logging
from src.custom_logger import LogHandler

# Initializing custom logger
log = logging.getLogger("root")
log.setLevel(logging.INFO)
log.addHandler(LogHandler())

app = Flask(__name__)
app.config.from_object("config.Config")

apm = ElasticAPM(app)
api = Api(app)
api = swagger.docs(Api(app), apiVersion="0.1")

initialize_routes(api)
app.run(host="0.0.0.0")

