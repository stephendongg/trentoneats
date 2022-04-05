#-----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team
#-----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from flask import Flask, request, make_response, redirect,url_for
from flask import render_template
#sfrom database import search
from search import restaurant_search
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
    tags = ""
    restaurantinfo = restaurant_search(restaurant, tags) #Exception handling omitted

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
    tags = request.args.get('tags')

    restaurantinfo = restaurant_search(restaurant, tags)

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
    if restaurantName is None or restaurantName.split()=="":
        restaurantName = ""
    restaurantAddress = request.args.get('restaurantAddress')
    if restaurantAddress is None or restaurantAddress.split()=="":
        restaurantAddress = ""
    restaurantHours = request.args.get('restaurantHours')
    if restaurantHours is None or restaurantHours.split()=="":
        restaurantHours = ""
    restaurantMenu = request.args.get('restaurantMenu')
    if restaurantMenu is None or restaurantMenu.split()=="":
        restaurantMenu = ""
    restaurantMedia = request.args.get('restaurantMedia')
    if restaurantMedia is None or restaurantMedia.split()=="":
        restaurantMedia = ""
    restaurantTags = request.args.get('restaurantTags')
    if restaurantTags is None or restaurantTags.split()=="":
        restaurantTags = ""

    type= request.args.getlist('type')
    for i in range(len(type)):
        if type[i] is None or type[i].split()=="":
            type[i] = ""
    cuisine = request.args.getlist('cuisine')
    for i in range(len(cuisine)):
        if cuisine[i] is None or cuisine[i].split()=="":
            cuisine[i] = ""

    priceNum = request.args.get('price')
    if priceNum is None or priceNum.split()=="":
        priceNum = ""
    priceNum = int(priceNum)
    price = 'inexpensive'
    if priceNum >= 10 and priceNum < 25:
        price = 'moderate'
    if priceNum >= 25:
        price = 'pricey'


    add_restaurant(restaurantName = restaurantName,
        restaurantAddress = restaurantAddress,
        restaurantHours = restaurantHours,
        restaurantMenu = restaurantMenu,
        restaurantMedia = restaurantMedia,
        restaurantTags = restaurantTags,
        cuisine = cuisine,
        type = type,
        price = price)
    html = render_template('joinrestaurant.html')
    response = make_response(html)
    return response

#---------------------------------------------------------

@app.route('/login', methods = ['GET'])
def login():
    html = render_template('login.html')
    response =  make_response(html)
    return response
