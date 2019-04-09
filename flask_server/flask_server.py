
# add parent directory to python modules path.
import sys
sys.path.append("..")

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database.db_setup import Base, Restaurant, MenuItem

# connect to DB and DB tables
engine = create_engine('sqlite:///../database/restaurantmenu.db')
Base.metadata.bind = engine
# establish 'session' connection for CRUD executions
session = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants/')
def index():
    return render_template('index.html')


@app.route('/restaurants/add/')
def add_restaurant():
	return render_template('add_restaurant.html')


@app.route('/restaurants/<int:restaurant_id>/edit')
def edit_restaurant(restaurant_id):
	return render_template('edit_restaurant.html')


@app.route('/restaurants/<int:restaurant_id>/delete')
def delete_restaurant(restaurant_id):
	return render_template('delete_restaurant.html')


@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurant_menu(restaurant_id):
	return render_template('restaurant_menu.html')


@app.route('/restaurants/<int:restaurant_id>/menu/add')
def add_menu_item(restaurant_id):
	return render_template('add_menu_item.html')


@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/edit')
def edit_menu_item(restaurant_id, item_id):
	return render_template('edit_menu_item.html')


@app.route('/restaurants/<int:restaurant_id>/menu/<int:item_id>/delete')
def delete_menu_item(restaurant_id, item_id):
	return render_template('delete_menu_item.html')



if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
