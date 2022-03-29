# -----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team
# -----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template
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

    # Temp  ------- initial restaurant value
    restaurant = ""
    restaurantinfo = restaurant_search(
        restaurant)  # Exception handling omitted

    html = render_template('searchform.html',
                           #ampm = get_ampm(),
                           # current_time = get_current_time(),
                           restaurantinfo=restaurantinfo,
                           error_msg=error_msg)
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/searchresults', methods=['GET'])
def search_results():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    restaurant = request.args.get('restaurant')

    restaurantinfo = restaurant_search(restaurant)

    html = render_template('searchform.html',
                           restaurantinfo=restaurantinfo
                           )
    response = make_response(html)

    return response

# Under Construction WebPages! These will be the ones that we will modify!
# ---------------------------------------------------------


@app.route('/about', methods=['GET'])
def about():
    html = render_template('about.html')
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/joinrestaurant', methods=['GET'])
def joinrestaurant():
    html = render_template('joinrestaurant.html')
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/addrestaurant', methods=['GET'])
def addrestaurant():
    restaurantName = request.args.get('restaurantName')
    restaurantAddress = request.args.get('restaurantAddress')
    restaurantHours = request.args.get('restaurantHours')
    restaurantMenu = request.args.get('restaurantMenu')
    restaurantMedia = request.args.get('restaurantMedia')
    restaurantTags = request.args.get('restaurantTags')
    add_restaurant(restaurantName=restaurantName,
                   restaurantAddress=restaurantAddress,
                   restaurantHours=restaurantHours,
                   restaurantMenu=restaurantMenu,
                   restaurantMedia=restaurantMedia,
                   restaurantTags=restaurantTags)
    html = render_template('joinrestaurant.html')
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/resdetails', methods=['GET'])
def resdetails():
    name = request.args.get('name')
    id = request.args.get('id')
    info = get_restaurant_info(id)
    html = render_template('resdetails.html', info=info)
    response = make_response(html)
    return response

# ---------------------------------------------------------


# @app.route('/login', methods = ['GET'])
# def login():
#     html = render_template('login.html')
#     response =  make_response(html)
#     return response


GOOGLE_CLIENT_ID = "308675237756-nem83n7953b22dujose0okjmhfi9q6mf.apps.googleusercontent.com"

client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "client_secret.json")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
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
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)
    # html = render_template('login.html')
    # response = make_response(html)
    # return response


@app.route('/callback', methods=['GET'])
def callback():
    flow.fetch_token(authorization_response=request.url)

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
    return redirect("/protected_area")


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect("/")


@app.route('/protected_area', methods=['GET'])
@login_is_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"
