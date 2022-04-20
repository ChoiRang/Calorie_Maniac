from flask import Flask, render_template, request, blueprints
from routes.food_reg_route import bp as food_reg_bp

app = Flask(__name__)
app.register_blueprint(food_reg_bp)

@app.route('/')
def hello_world():  # put application's code here
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
