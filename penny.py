# -----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team
# -----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template, abort
# sfrom database import search
from search import restaurant_search, get_restaurant_info
from add_restaurant import add_restaurant

import os
import pathlib
import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

# -----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')
app.secret_key = "dsghabkjcn1iy2u6gdoyq"

# -----------------------------------------------------------------------


@app.route('/', methods=['GET'])
@app.route('/searchform', methods=['GET'])
def search_form():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''
    unique_id = session.get('google_id')
    html = render_template('searchform.html', error_msg=error_msg, id=unique_id)
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/searchresults', methods=['GET'])
def search_results():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    restaurant = request.args.get('restaurant')
    if (restaurant is None) or (restaurant.split()==""):
        restaurant=""

    price = request.args.get('price')
    if (price is None) or (price.split()==""):
        price=""

    type = request.args.get('type')
    if (type is None) or (type.split()==""):
        type = ""

    cuisine = request.args.get('cuisine')
    if (cuisine is None) or (cuisine ==[]):
        cuisine= "%%"

    try:
        restaurantinfo = restaurant_search(restaurant, cuisine, type, price)
    except Exception as e:
        print(e)
        html = render_template('servererror.html')
        response = make_response(html)
        return response
    if restaurantinfo == "stdservererr":
        print("Standard server error")
        response = make_response('<div><p>Standard Server Error</p></div>')
        return response
    unique_id = session.get('google_id')
    html = render_template('searchresults.html', restaurantinfo=restaurantinfo,
                            id=unique_id)
    response = make_response(html)
    return response

# Under Construction WebPages! These will be the ones that we will modify!
# ---------------------------------------------------------


@app.route('/about', methods=['GET'])
def about():
    unique_id = session.get('google_id')
    html = render_template('about.html', id=unique_id)
    response = make_response(html)
    return response

# ---------------------------------------------------------


def authorized(function):
    def wrapper2(*args, **kwargs):
        unique_id = session.get('google_id')
        if (session.get("email") is None) or not (session["email"] == "pjozuah@princeton.edu" or session["email"] == "sd20@princeton.edu"
                                                  or session["email"] == "soumyag@princeton.edu" or session["email"] == "chukwuma@princeton.edu"
                                                  or session["email"] == "kao3@princeton.edu" or session["email"] == "anatk@princeton.edu"):
            html = render_template('unauthorized_login.html', id=unique_id)
            response = make_response(html)
            return response
        else:
            return function()

    return wrapper2


@app.route('/joinrestaurant', methods=['GET'])
@authorized
def joinrestaurant():
    unique_id = session.get('google_id')
    html = render_template('joinrestaurant.html', id=unique_id)
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/addrestaurant', methods=['GET'])
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
    restaurantImage = request.args.get('restaurantImage')

    if restaurantTags is None or restaurantTags.split()=="":
        restaurantTags = ""

    type= request.args.get('type')
    if type is None or type.split()=="":
        type = ""
    cuisine = request.args.getlist('cuisine')
    for i in range(len(cuisine)):
        if cuisine[i] is None or cuisine[i].split()=="":
            cuisine[i] = ""
    cuisine = ', '.join(cuisine)

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
        price = price,
        restaurantImage = restaurantImage)
    unique_id = session.get('google_id')
    html = render_template('joinrestaurant.html', id=unique_id)
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/resdetails', methods=['GET'])
def resdetails():
    name = request.args.get('name')
    id = request.args.get('id')
    info = get_restaurant_info(id)
    unique_id = session.get('google_id')
    html = render_template('resdetails.html', info=info, id=unique_id)
    response = make_response(html)
    return response

# ---------------------------------------------------------


GOOGLE_CLIENT_ID = "308675237756-nem83n7953b22dujose0okjmhfi9q6mf.apps.googleusercontent.com"

client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "google-credentials.json")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    #redirect_uri="https://trentoneats.herokuapp.com/callback"
    redirect_uri="http://127.0.0.1:8080/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route('/login', methods=['GET'])
def login():

    # session.clear()
    # CHECK IF LOGGED IN IF LOGGED IN THEN LOG OUT
    authorization_url, state = flow.authorization_url()
    # print(authorization_url)
    session["state"] = state
    return redirect(authorization_url)
    # html = render_template('login.html')
    # response = make_response(html)
    # return response


@app.route('/callback', methods=['GET'])
def callback():
    # Debugging
    # print(session["state"])
    code = request.args.get('code')
    flow.fetch_token(code=code)
    # flow.fetch_token(authorization_response=request.url)
    # print(request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")

    unique_id = session.get('google_id')
    restaurant = ""
    cuisine = "%%"
    type = ""
    price = ""

    # price = request.args.get('price')
    # if (price is None) or (price.split()==""):
    #     price=""
    #
    # type = request.args.get('type')
    # if (type is None) or (type.split()==""):
    #     type = ""
    #
    # cuisine = request.args.get('cuisine')
    # if (cuisine is None) or (cuisine ==[]):
    #     cuisine=["%%"]
    restaurantinfo = restaurant_search(restaurant, cuisine, type, price)

    #restaurantinfo = restaurant_search(restaurant)
    # try:
    #     restaurantinfo = restaurant_search(restaurant, cuisine, type, price)
    # except:
    #     html = render_template('servererror.html')
    #     response = make_response(html)
    #     return response
    # if restaurantinfo == "stdservererr":
    #     print("Standard server error")
    #     response = make_response('<div><p>Standard Server Error</p></div>')
    #     return response
    html = render_template('searchform.html',
                           #ampm = get_ampm(),
                           # current_time = get_current_time(),
                           restaurantinfo=restaurantinfo,
                           id=unique_id)
    response = make_response(html)
    return response
    # return redirect("/")  # ,id=unique_id)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('name', None)
    session.clear()
    return redirect("/")


@app.route('/protected_area', methods=['GET'])
@login_is_required
def protected_area():
    return redirect("/")
    # return f"Thank you for logging in {session['name']}! \
    #  <br/> <a href='/logout'><button>Logout</button></a>"


def authenticate():
    if 'google_id' not in session:
        abort(redirect(url_for('login')))
    return session.get('name')
