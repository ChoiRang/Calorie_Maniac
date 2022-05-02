from flask import Blueprint, Flask, render_template, request, session
from python_files.food.food_info_service import FoodInfoService

bp = Blueprint('food', __name__, url_prefix='/main/food')
food_info_service = FoodInfoService()


@bp.get('/')
def food_page():
	return render_template('food_page.html')


@bp.post('/search')
def food_search():
	food_name = request.form['food_name']
	food_name = '%' + food_name + '%'
	food_list = food_info_service.retrieve_name(food_name)
	return render_template('loader/food_list.html', food_list=food_list)


@bp.get('/register')
def get_index():
	index = request.args.get('fid')
	print(index)
	return render_template('index.html')