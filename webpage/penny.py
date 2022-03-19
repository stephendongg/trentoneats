#-----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team 
#-----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from flask import Flask, request, make_response, redirect,url_for
from flask import render_template
#sfrom database import search
from search import __search__, restaurant_search

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

@app.route('/login', methods = ['GET'])
def login():
    html = render_template('login.html')
    response =  make_response(html)
    return response