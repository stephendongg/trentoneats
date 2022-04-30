# -----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team
# -----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from add_requests import add_requests
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template, abort
from requestshelper import delete_request, delete_request_add_res
# sfrom database import search
from search import get_request_info, restaurant_search, get_restaurant_info, request_search, restaurants_count
from add_restaurant import add_restaurant

from reviews import add_review, review_search, update_ratings

from admin import admin_search
from users import user_exists, user_add, add_favorite_restaurant, is_favorite_restaurant, get_favorites, delete_favorite_restaurant

import random
import datetime

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

    # Note! Figure out how to make it refresh.. Look int oCss.
    #randomrestaurant = random.randint(0, restaurants_count() - 1)
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''
    unique_id = session.get('google_id')
    admin = is_admin()
    html = render_template(
        'searchform.html', error_msg=error_msg, id=unique_id, admin=admin, randomrestaurant=random.randint(0, restaurants_count() - 1))
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/searchresults', methods=['GET'])
def search_results():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    restaurant = request.args.get('restaurant')
    if (restaurant is None) or (restaurant.split() == ""):
        restaurant = ""

    price = request.args.get('price')
    if (price is None) or (price.split() == ""):
        price = ""

    type = request.args.get('type')
    if (type is None) or (type.split() == ""):
        type = ""

    cuisine = request.args.get('cuisine')
    if (cuisine is None) or (cuisine == []):
        cuisine = "%%"


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
    admin = is_admin()
    html = render_template('searchresults.html', restaurantinfo=restaurantinfo,
                           id=unique_id, admin=admin)
    response = make_response(html)

    return response


# ---------------------------------------------------------


@app.route('/about', methods=['GET'])
def about():
    unique_id = session.get('google_id')
    admin = is_admin()
    html = render_template('about.html', id=unique_id, admin=admin)
    response = make_response(html)
    return response

# ---------------------------------------------------------


def is_admin():
    if ((session.get("email") is None) or (not admin_search(session["email"]))):
        return False
    else:
        return True


def authorized(function):
    def wrapper2(*args, **kwargs):
        unique_id = session.get('google_id')
        if ((session.get("email") is None) or (not admin_search(session["email"]))):
            html = render_template('unauthorized_login.html', id=unique_id)
            response = make_response(html)
            return response
        else:
            return function()
    return wrapper2


def authorize_res_add(function):
    def wrapper4(*args, **kwargs):
        unique_id = session.get('google_id')
        if ((session.get("email") is None)):
            html = render_template('unauthorized_login.html', id=unique_id)
            response = make_response(html)
            return response
        else:
            return function()
    return wrapper4

# Logged in Requirement


def loggedin(function):
    def wrapper3(*args, **kwargs):
        unique_id = session.get('google_id')
        if (session.get("email") is None):
            html = render_template('unauthorized_login.html', id=unique_id)
            response = make_response(html)
            return response
        else:
            return function()
    return wrapper3
# ---------------------------------------------------------

# FAVORITE RESTAURANTS


@app.route('/myfavorite', methods=['GET'])
@loggedin
def myrestaurant():
    unique_id = session.get('google_id')
    admin = is_admin()
    restaurantinfo = get_favorites(session["email"])
    # for restaurant in favorites

    #resid = favorites[1]
    #print("this is resid" + resid)
    #restaurantinfo = restaurant_search(resid)
    #html = render_template('myrestaurant.html', id=unique_id)
    html = render_template('myfavorite.html', restaurantinfo=restaurantinfo,
                           admin=admin)
    response = make_response(html)
    return response
 # ---------------------------------------------------------

# default


@app.route('/joinrestaurant', methods=['GET'])
@authorize_res_add
def joinrestaurant():
    admin = is_admin()
    unique_id = session.get('google_id')
    html = render_template('joinrestaurant.html', id=unique_id, admin=admin)
    response = make_response(html)
    return response

# ---------------------------------------------------------

# when submitted


@app.route('/addrestaurant', methods=['GET'])
def addrestaurant():
    restaurantName = request.args.get('restaurantName')
    if restaurantName is None or restaurantName.split() == "":
        restaurantName = ""
    restaurantAddress = request.args.get('restaurantAddress')
    if restaurantAddress is None or restaurantAddress.split() == "":
        restaurantAddress = ""
    # RESTAURANT HOURS START
    restaurantHours = ""

    # -> weekday lol
    weekdayHours = ""
    if request.args.get('mondayopen'):
        weekdayHours += "Monday " + \
            request.args.get('mondaystart') + " - " + \
            request.args.get('mondayend') + ", "
    else:
        weekdayHours += "Monday Closed, "
    if request.args.get('tuesdayopen'):
        weekdayHours += "Tuesday " + \
            request.args.get('tuesdaystart') + " - " + \
            request.args.get('tuesdayend') + ", "
    else:
        weekdayHours += "Tuesday Closed, "
    if request.args.get('wednesdayopen'):
        weekdayHours += "Wednesday " + \
            request.args.get('wednesdaystart') + " - " + \
            request.args.get('wednesdayend') + ", "
    else:
        weekdayHours += "Wednesday Closed, "
    if request.args.get('thursdayopen'):
        weekdayHours += "Thursday " + \
            request.args.get('thursdaystart') + " - " + \
            request.args.get('thursdayend') + ", "
    else:
        weekdayHours += "Thursday Closed, "
    if request.args.get('fridayopen'):
        weekdayHours += "Friday " + \
            request.args.get('fridaystart') + " - " + \
            request.args.get('fridayend') + ", "
    else:
        weekdayHours += "Friday Closed, "
    if request.args.get('saturdayopen'):
        weekdayHours += "Saturday " + \
            request.args.get('saturdaystart') + " - " + \
            request.args.get('saturdayend') + ", "
    else:
        weekdayHours += "Saturday Closed, "
    if request.args.get('sundayopen'):
        weekdayHours += "Sunday " + \
            request.args.get('sundaystart') + " - " + \
            request.args.get('sundayend')
    else:
        weekdayHours += "Sunday Closed"

    restaurantHours = weekdayHours

    # change?
    if restaurantHours is None or restaurantHours.split() == "":
        restaurantHours = ""
    restaurantMenu = request.args.get('restaurantMenu')
    if restaurantMenu is None or restaurantMenu.split() == "":
        restaurantMenu = ""
    restaurantMedia = request.args.get('restaurantMedia')
    if restaurantMedia is None or restaurantMedia.split() == "":
        restaurantMedia = ""
    restaurantTags = request.args.get('restaurantTags')
    restaurantImage = request.args.get('restaurantImage')

    if restaurantTags is None or restaurantTags.split() == "":
        restaurantTags = ""

    type = request.args.get('type')
    if type is None or type.split() == "":
        type = ""
    cuisine = request.args.getlist('cuisine')
    for i in range(len(cuisine)):
        if cuisine[i] is None or cuisine[i].split() == "":
            cuisine[i] = ""
    cuisine = ', '.join(cuisine)

    priceNum = request.args.get('price')
    if priceNum is None or priceNum.split() == "":
        priceNum = ""
    priceNum = int(priceNum)
    price = 'Inexpensive $'
    if priceNum > 10 and priceNum <= 30:
        price = 'Moderate $$'
    if priceNum > 30:
        price = 'Pricey $$$'

    # trying to add to requests table first

    add_requests(restaurantName=restaurantName,
                 restaurantAddress=restaurantAddress,
                 restaurantHours=restaurantHours,
                 restaurantMenu=restaurantMenu,
                 restaurantMedia=restaurantMedia,
                 restaurantTags=restaurantTags,
                 cuisine=cuisine,
                 type=type,
                 price=price,
                 restaurantImage=restaurantImage)

    # add_restaurant(restaurantName=restaurantName,
    #                restaurantAddress=restaurantAddress,
    #                restaurantHours=restaurantHours,
    #                restaurantMenu=restaurantMenu,
    #                restaurantMedia=restaurantMedia,
    #                restaurantTags=restaurantTags,
    #                cuisine=cuisine,
    #                type=type,
    #                price=price,
    #                restaurantImage=restaurantImage)
    unique_id = session.get('google_id')
    admin = is_admin()
    html = render_template('joinrestaurant.html', id=unique_id, admin=admin)
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/resdetails', methods=['GET', 'POST'])
def resdetails():
    name = request.args.get('name')
    id = request.args.get('id')
    admin = is_admin()
    session['resid'] = id
    info = get_restaurant_info(id)
    unique_id = session.get('google_id')

    reviews = review_search(id)

    # OK HERE IS FAVORITE INFO!

    favorite = -1
    # -1 - not logged in, 1 = favorite, 0 = not favorite
    if (not session.get("email") is None):
        if is_favorite_restaurant(session["email"], id):
            favorite = 1
        else:
            favorite = 0

    # LOGGGED IN INFO
    if (not session.get("email") is None):
        isLoggedin = True
    else:
        isLoggedin = False

    if request.method == 'POST':
        text = request.form['review-text']
        rating = request.form['rating']
        email = session["email"]
        print(rating)
        text = text.strip()
        error = None
        if not text:
            error = 'You didn\'t add any new reviews.'
        if error is None:
            add_review(id, datetime.datetime.now(), text, rating, email)
            update_ratings(id)
            reviews = review_search(id)

    html = render_template('resdetails.html', info=info,
                           reviews=reviews, id=unique_id, admin=admin, favorite=favorite, loggedin=isLoggedin)
    response = make_response(html)
    return response


@app.route('/added', methods=['GET', 'POST'])
def test():
    #name = request.args.get('name')
    #id = request.args.get('id')
    name = request.args.get('name')
    id = session['resid']
    info = get_restaurant_info(id)
    # This line is new.
    unique_id = session.get('google_id')
    admin = is_admin()
    #html = render_template('resdetails.html', info=info, id=unique_id)

    reviews = review_search(id)
    # Info currently is:
    info = get_restaurant_info(id)
    # This line is new.
    #html = render_template('resdetails.html', info=info, id=unique_id)

    # -- ADD TO FAVORITE --
    if (not is_favorite_restaurant(session["email"], id)):
        add_favorite_restaurant(session["email"], id)
    else:
        delete_favorite_restaurant(session["email"], id)
        # HOW DO I MAKE THIS DISSAPEAR.

    # -1 - not logged in, 1 = favorite, 0 = not favorite
    if (not session.get("email") is None):
        if is_favorite_restaurant(session["email"], id):
            favorite = 1
        else:
            favorite = 0

    # LOGGGED IN INFO
    if (not session.get("email") is None):
        isLoggedin = True
    else:
        isLoggedin = False

    if request.method == 'POST':
        text = request.form['review-text']
        rating = request.form['rating']
        email = session["email"]
        print(rating)
        text = text.strip()
        error = None
        if not text:
            error = 'You didn\'t add any new reviews.'
        if error is None:
            # Gotta figure out if its customer taht we still want to link for placeolder
            # Currently, placeholder reviews are all -10
            # NEed Cusomter Ids sorted out.
            add_review(id, datetime.datetime.now(), text, rating, email)
            update_ratings(id)
            # return redirect(url_for('review.dashboard'))
            reviews = review_search(id)
        # flash(error)
        # return render_template('review/create.html')

    html = render_template('resdetails.html', info=info,
                           reviews=reviews, id=unique_id, admin=admin, favorite=favorite, loggedin=isLoggedin)
    response = make_response(html)
    return response

    # html = render_template('resdetails.html', info=info,
    #                                         reviews=reviews, id=unique_id)
    # response = make_response(html)
    # return response
    # id = session['resid']
    # return redirect('/resdetails', id=id)
    # # Info currently is:
    # info = get_restaurant_info(id)
    # # This line is new.
    # unique_id = session.get('google_id')
    # #html = render_template('resdetails.html', info=info, id=unique_id)
    # reviews = review_search(id)

    # html = render_template('resdetails.html', info=info,
    #                                         reviews=reviews, id=unique_id)
    # response = make_response(html)
    # return responsez
# ---------------------------------------------------------


GOOGLE_CLIENT_ID = "308675237756-nem83n7953b22dujose0okjmhfi9q6mf.apps.googleusercontent.com"

client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "google-credentials.json")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="https://trentoneats.herokuapp.com/callback"
    # redirect_uri="http://127.0.0.1:8080/callback"
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
    return redirect(str(authorization_url) + "&prompt=consent")
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

    # if not session["state"] == request.args["state"]:
    #     abort(500)  # State does not match!

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

    session["email"] = id_info.get("email")
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")

    if (not user_exists(session["email"])):
        user_add(session["email"], session["name"])

    unique_id = session.get('google_id')
    restaurant = ""
    cuisine = "%%"
    type = ""
    price = ""
    admin = is_admin()

    restaurantinfo = restaurant_search(restaurant, cuisine, type, price)

    html = render_template('searchform.html',
                           #ampm = get_ampm(),
                           # current_time = get_current_time(),
                           #    restaurantinfo=restaurantinfo,
                           id=unique_id, admin=admin, randomrestaurant=random.randint(0, restaurants_count() - 1))
    response = make_response(html)
    return response
    # return redirect("/")  # ,id=unique_id)


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('name', None)
    session.pop('state', None)
    session.pop('email', None)
    session.pop('google_id', None)
    session.pop('resid', None)
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


# ------------------------------------------------------------------------
# Handle admin requests


@app.route('/requestresults', methods=['GET'])
def request_results():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    restaurant = request.args.get('restaurant')
    if (restaurant is None) or (restaurant.split() == ""):
        restaurant = ""

    try:
        restaurantinfo = request_search(restaurant)
    except:
        html = render_template('servererror.html')
        response = make_response(html)
        return response
    if restaurantinfo == "stdservererr":
        print("Standard server error")
        response = make_response('<div><p>Standard Server Error</p></div>')
        return response
    unique_id = session.get('google_id')
    admin = is_admin()
    html = render_template('requestresults.html', restaurantinfo=restaurantinfo,
                           id=unique_id, admin=admin)
    response = make_response(html)

    return response


@app.route('/requests', methods=['GET'])
def reqeusts_area():
    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''
    unique_id = session.get('google_id')
    admin = is_admin()
    html = render_template(
        'requestform.html', error_msg=error_msg, id=unique_id, admin=admin)
    response = make_response(html)
    return response


@app.route('/requestdetails', methods=['GET', 'POST'])
def request_details():
    name = request.args.get('name')
    id = request.args.get('id')
    admin = is_admin()
    session['resid'] = id
    # set approval = 0
    session['approval'] = 0
    # Info currently is:
    info = get_request_info(id)
    # This line is new.
    unique_id = session.get('google_id')
    #html = render_template('resdetails.html', info=info, id=unique_id)

    reviews = review_search(id)
    # info_obj['name'] = str(row[0])
    # info_obj['address'] = str(row[1])
    # info_obj['hours'] = str(row[2])
    # info_obj['open_closed'] = str(row[3])
    # info_obj['menu'] = str(row[4])
    # info_obj['media'] = str(row[5])
    # info_obj['tags'] = str(row[6])
    # info_obj['review_count'] = str(row[7])
    # info_obj['stars'] = str(row[8])
    # info_obj['image'] = str(row[9])

    # Separate Code here
    # Stmt
    # reviews = db.execute(
    # Just gotta fetch one of them. current_user_review = db.execute("SELECT * FROM reviews WHERE book_id=:book_id AND user_id=:user_id", {"book_id": book.id, "user_id": session["user_id"]}).fetchone()
    #book_extra = goodreads_lookup(isbn)

    if request.method == 'POST':
        if request.form['submit_button'] == 'Deny':
            print("DENY CLICKED")
            delete_request(id)
            html = render_template('requestform.html', info=info,
                                   reviews=reviews, id=unique_id, admin=admin)
            response = make_response(html)
            return response
        elif request.form['submit_button'] == 'Approve':
            delete_request_add_res(id)
            html = render_template('requestform.html', info=info,
                                   reviews=reviews, id=unique_id, admin=admin)
            response = make_response(html)
            return response

    html = render_template('requestdetails.html', info=info,
                           reviews=reviews, id=unique_id, admin=admin)
    response = make_response(html)
    return response
