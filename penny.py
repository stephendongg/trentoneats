#-----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team
#-----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from flask import Flask, request, make_response, redirect,url_for
from flask import render_template
#sfrom database import search
from search import restaurant_search, get_restaurant_info
from add_restaurant import add_restaurant

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods = ['GET'])
@app.route('/searchform', methods=['GET'])
def search_form():

    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    #Temp  ------- initial restaurant value
    restaurant = ""
    restaurantinfo = restaurant_search(restaurant) #Exception handling omitted

    html = render_template('searchform.html',
        #ampm = get_ampm(),
        # current_time = get_current_time(),
        restaurantinfo = restaurantinfo,
        error_msg = error_msg)
    response = make_response(html)
    return response

#---------------------------------------------------------

@app.route('/searchresults', methods = ['GET'])
def search_results():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    restaurant = request.args.get('restaurant')

    restaurantinfo = restaurant_search(restaurant)

    html = render_template('searchform.html',
        restaurantinfo = restaurantinfo
        )
    response = make_response(html)

    return response

# Under Construction WebPages! These will be the ones that we will modify!
#---------------------------------------------------------

@app.route('/about', methods = ['GET'])
def about():
    html = render_template('about.html')
    response =  make_response(html)
    return response

#---------------------------------------------------------
@app.route('/joinrestaurant', methods = ['GET'])
def joinrestaurant():
    html = render_template('joinrestaurant.html')
    response =  make_response(html)
    return response

#---------------------------------------------------------

@app.route('/addrestaurant', methods = ['GET'])
def addrestaurant():
    restaurantName = request.args.get('restaurantName')
    restaurantAddress = request.args.get('restaurantAddress')
    restaurantHours = request.args.get('restaurantHours')
    restaurantMenu = request.args.get('restaurantMenu')
    restaurantMedia = request.args.get('restaurantMedia')
    restaurantTags = request.args.get('restaurantTags')
    add_restaurant(restaurantName = restaurantName,
        restaurantAddress = restaurantAddress,
        restaurantHours = restaurantHours,
        restaurantMenu = restaurantMenu,
        restaurantMedia = restaurantMedia,
        restaurantTags = restaurantTags)
    html = render_template('joinrestaurant.html')
    response = make_response(html)
    return response

#---------------------------------------------------------
@app.route('/resdetails', methods = ['GET'])
def resdetails():
    name = request.args.get('name')
    id = request.args.get('id')
    info = get_restaurant_info(id)
    html = render_template('resdetails.html', info = info)
    response =  make_response(html)
    return response

#---------------------------------------------------------


@app.route('/login', methods = ['GET'])
def login():
    html = render_template('login.html')
    response =  make_response(html)
    return response
