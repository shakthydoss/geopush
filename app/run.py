from flask import Flask
import rest.rest_controller as rest_controller
import web.web_controller as web_controller

app = Flask(__name__)
app.register_blueprint(rest_controller.blueprint,url_prefix='/rest')
app.register_blueprint(web_controller.blueprint, url_prefix='/web')

if __name__ == '__main__':
    app.run(debug=True)

