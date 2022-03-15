#-----------------------------------------------------------------------
# penny.oy
# Author: Trenton Eats Local Team 
#-----------------------------------------------------------------------

#from time import localtime, asctime, strftime
from urllib import response
from flask import Flask, request, make_response, redirect,url_for
from flask import render_template
#sfrom database import search

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')

#-----------------------------------------------------------------------

@app.route('/', methods = ['GET'])
@app.route('/searchform', methods=['GET'])
def search_form():

    error_msg = request.args.get('error_msg')
    if error_msg is None:
        error_msg = ''

    prev_author = request.cookies.get('prev_author')
    if prev_author is None:
        prev_author = '(None)'

    html = render_template('searchform.html',
        #ampm = get_ampm(),
        # current_time = get_current_time(),
        error_msg = error_msg,
        prev_author=prev_author)
    response = make_response(html)
    return response

#---------------------------------------------------------

@app.route('/searchresults', methods = ['GET'])
def search_results():

    author = request.args.get('author')
    if(author is None) or (author.strip() == ''):
        error_msg = 'Please type an author name.'
        return redirect(url_for('search_form', error_msg=error_msg))

    #book = search(author) #Exception handling omitted

    html = render_template('searchresults.html',
        ampm=get_ampm(),
        #current_time=get_current_time(),
        author=author,
        #books = books
        )
    response = make_response(html)
    response.set_cookie('prev_author', author)
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