#!/usr/bin/env python
"""This is reviews.py"""
# -----------------------------------------------------------------------
# reviews.py
# -----------------------------------------------------------------------

from datetime import date
import sys
from os import name
from sys import argv, stderr
from socket import socket, SOL_SOCKET, SO_REUSEADDR

from pickle import dump
from pickle import load

from contextlib import closing
# from sqlite3 import DataError, DatabaseError
# from sqlite3 import connect
from psycopg2 import connect, DatabaseError
import psycopg2
import argparse
# loading


from restaurant import restaurant


# -----------------------------------------------------------------------
# Old Database -> for the original reg
#DATABASE_URL = 'file:reg.sqlite?mode=ro'

# New database for restaurants
DATABASE_URL = 'file:trentoneats.sql?mode=ro'
# -----------------------------------------------------------------------

def review_search(input):
    """search through restaurants"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #              database="trentoneats") as connection:
        # dequ5ope4nuoit
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                # stmt_str = "SELECT restaurant_id, name, open_closed, address, stars "
                # stmt_str += "FROM restaurants "
                # stmt_str += "WHERE LOWER (name) LIKE LOWER ('%" + \
                #     input + "%') "

                # Review Search 
                stmt_str = "SELECT date, text, review_id, email "
                stmt_str += "FROM reviews "
                stmt_str += "WHERE restaurant_id = '" + input + "';"
                # stmt_str = "SELECT r.id, date, text, restaurant_id "
                # stmt_str += "FROM reviews r JOIN restaurants u ON r.restaurant_id = u.restaurant_id "
                # stmt_str += "WHERE restaurant_id = " + input


                cursor.execute(stmt_str)

                row = cursor.fetchone()

                # course list
                reviews = []

                # rowstringlist this rowstring will contain all of the necessary values

                rowstring = ["", "", "", ""]

                # This iwll parse through the rows and get all of the necsary values
                while row is not None:
                    rowstring = ["", "", "", ""]
                    rowstring[0] = str(row[0])
                    rowstring[1] = str(row[1])
                    rowstring[2] = str(row[2])
                    rowstring[3] = str(row[3])
                    reviews.append(rowstring)
                    row = cursor.fetchone()
                
                return reviews

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")



def add_review(restaurant_id, date, text, rating, email):

    stmt_str = """
    INSERT INTO reviews (restaurant_id, date,
    text, overall, email) 
    VALUES  ( '"""
    stmt_str += str(restaurant_id) + "', '" + str(date) + "', '" + text + "', '" + rating + "', '" + email +"');"

    try:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                database="dequ5ope4nuoit") as connection:

            with connection.cursor() as cursor:
                print(stmt_str)
                cursor.execute(stmt_str)


    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex, file=stderr)
        exit(1)

def get_restaurant_info(res_id):
    """find all information on one restaurant"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #              database="trentoneats") as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                stmt_str = "SELECT name, address, hours, open_closed, menu, "
                stmt_str += "media, tags, review_count, stars, image FROM restaurants "
                stmt_str += "WHERE restaurant_id = '" + res_id + "'; "

                cursor.execute(stmt_str)
                print(stmt_str)
                row = cursor.fetchone()

                # hashmap to hold object info
                info_obj = {}


                # This will parse through the row and occupy the hashmap
                if row is not None:
                    info_obj['name'] = str(row[0])
                    info_obj['address'] = str(row[1])
                    info_obj['hours'] = str(row[2])
                    info_obj['open_closed'] = str(row[3])
                    info_obj['menu'] = str(row[4])
                    info_obj['media'] = str(row[5])
                    info_obj['tags'] = str(row[6])
                    info_obj['review_count'] = str(row[7])
                    info_obj['stars'] = str(row[8])
                    info_obj['image'] = str(row[9])

                return info_obj

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")