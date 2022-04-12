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

from reviews import add_review, review_search
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

# ---------------------------------------------------------


@app.route('/about', methods=['GET'])
def about():
    html = render_template('about.html')
    response = make_response(html)
    return response

# ---------------------------------------------------------


def authorized(function):
    def wrapper2(*args, **kwargs):
        if (session.get("email") is None) or not (session["email"] == "pjozuah@princeton.edu" or session["email"] == "sd20@princeton.edu"
                                                  or session["email"] == "soumyag@princeton.edu" or session["email"] == "chukwuma@princeton.edu"
                                                  or session["email"] == "kao3@princeton.edu" or session["email"] == "anatk@princeton.edu"):
            html = render_template('unauthorized_login.html')
            response = make_response(html)
            return response
        else:
            return function()

    return wrapper2


@app.route('/joinrestaurant', methods=['GET'])
@authorized
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
    restaurantImage = request.args.get('restaurantImage')
    add_restaurant(restaurantName=restaurantName,
                   restaurantAddress=restaurantAddress,
                   restaurantHours=restaurantHours,
                   restaurantMenu=restaurantMenu,
                   restaurantMedia=restaurantMedia,
                   restaurantTags=restaurantTags,
                   restaurantImage=restaurantImage)
    html = render_template('joinrestaurant.html')
    response = make_response(html)
    return response

# ---------------------------------------------------------


@app.route('/resdetails', methods=['GET', 'POST'])
def resdetails():
    name = request.args.get('name')
    id = request.args.get('id')
    # Info currently is: 
    info = get_restaurant_info(id)
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

    #Separate Code here 
    #Stmt
    #reviews = db.execute(
    # Just gotta fetch one of them. current_user_review = db.execute("SELECT * FROM reviews WHERE book_id=:book_id AND user_id=:user_id", {"book_id": book.id, "user_id": session["user_id"]}).fetchone()
    #book_extra = goodreads_lookup(isbn)
    
    if request.method == 'POST':
        text = request.form['review-text']
        text = text.strip()
        error = None
        if not text:
            error = 'You didn\'t add any new reviews.'
        if error is None:
            # Gotta figure out if its customer taht we still want to link for placeolder
            # Currently, placeholder reviews are all -10
            #NEed Cusomter Ids sorted out.
            add_review(id, datetime.datetime.now(), text)
            #return redirect(url_for('review.dashboard'))
            reviews = review_search(id)
        #flash(error)
        #return render_template('review/create.html')

    

    html = render_template('resdetails.html', info=info,
                                            reviews=reviews)
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

    session.clear()
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
    return redirect("/protected_area")


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect("/")


@app.route('/protected_area', methods=['GET'])
@login_is_required
def protected_area():
    return redirect("/")
    # return f"Thank you for logging in {session['name']}! \
    #  <br/> <a href='/logout'><button>Logout</button></a>"

# @app.route('/create', methods=('GET', 'POST'))
# @login_is_required
# def create():
#   if request.method == 'POST':
#     text = request.form['review-text']
#     text = text.strip()
#     db = get_db()
#     error = None
#     if not text:
#         error = 'You didn\'t add any new reviews.'
#     if error is None:
#         db.execute(
#         'INSERT INTO review (author_id, content) VALUES (?, ?)',   
#         (g.user['id'], text)
#         )
#         db.commit()
#         return redirect(url_for('review.dashboard'))
#     flash(error)
#     return render_template('review/create.html')
