from flask import Flask
from flask_restful import Api

from controllers.darkweb_scan_api import DarkWebScan

app = Flask(__name__)
api = Api(app)

api.add_resource(DarkWebScan, "/v2/darkweb")

if __name__ == "__main__":
    app.run()
