#!/usr/bin/env python
"""This is search.py"""
# -----------------------------------------------------------------------
# search.py
# -----------------------------------------------------------------------

# Originally assignment 2's regserver.py -> adapted to search.py to import __search__ cand course_search
# course_search -> searchbar = restaurant_search
# __search__ -> gets the details -> might be renamed to details

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
import argparse
# loading


from restaurant import restaurant


# -----------------------------------------------------------------------
# Old Database -> for the original reg
#DATABASE_URL = 'file:reg.sqlite?mode=ro'

# New database for restaurants
DATABASE_URL = 'file:trentoneats.sql?mode=ro'
# -----------------------------------------------------------------------


def restaurant_search(input):
    """search through restaurants"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #              database="trentoneats") as connection:
        # dequ5ope4nuoit
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                stmt_str = "SELECT restaurant_id, name, open_closed, address, "
                stmt_str += "stars, cuisine, type, price, tags "
                stmt_str += "FROM restaurants "
                stmt_str += "WHERE LOWER(name) ILIKE %s"

                # print(stmt_str)
                input = '%' + input.lower() + '%'
                # print(input)
                cursor.execute(stmt_str, [input])
                #cursor.execute(stmt_str, ["'bbq'"])
                row = cursor.fetchone()

                # course list
                restaurants = []

                # rowstringlist this rowstring will contain all of the necessary values

                rowstring = ["", "", "", "", "", "", "", "", ""]

                # This iwll parse through the rows and get all of the necsary values
                while row:
                    rowstring[0] = row[0]
                    rowstring[1] = row[1]
                    rowstring[2] = row[2]
                    rowstring[3] = row[3]
                    rowstring[4] = row[4]
                    rowstring[5] = row[5]
                    rowstring[6] = row[6]
                    rowstring[7] = row[7]
                    rowstring[8] = row[8]
                    res = restaurant(rowstring)
                    restaurants.append(res)
                    row = cursor.fetchone()

                return restaurants

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")


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
                stmt_str += "media, tags, review_count, stars, image, "
                stmt_str += "price, cuisine, type FROM restaurants "
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
                    info_obj['price'] = str(row[10])
                    info_obj['cuisine'] = str(row[11])
                    info_obj['type'] = str(row[12])

                return info_obj

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")


def request_search(input):
    """search through restaurants"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #              database="trentoneats") as connection:
        # dequ5ope4nuoit
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                stmt_str = "SELECT request_id, name, open_closed, address, "
                stmt_str += "stars, cuisine, type, price, tags "
                stmt_str += "FROM requests "
                stmt_str += "WHERE LOWER(name) ILIKE %s"

                # print(stmt_str)
                input = '%' + input.lower() + '%'
                # print(input)
                cursor.execute(stmt_str, [input])
                #cursor.execute(stmt_str, ["'bbq'"])
                row = cursor.fetchone()

                # course list
                restaurants = []

                # rowstringlist this rowstring will contain all of the necessary values

                rowstring = ["", "", "", "", "", "", "", "", ""]

                # This iwll parse through the rows and get all of the necsary values
                while row:
                    rowstring[0] = row[0]
                    rowstring[1] = row[1]
                    rowstring[2] = row[2]
                    rowstring[3] = row[3]
                    rowstring[4] = row[4]
                    rowstring[5] = row[5]
                    rowstring[6] = row[6]
                    rowstring[7] = row[7]
                    rowstring[8] = row[8]
                    res = restaurant(rowstring)
                    restaurants.append(res)
                    row = cursor.fetchone()

                return restaurants

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")


def get_request_info(res_id):
    """find all information on one restaurant"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #              database="trentoneats") as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                stmt_str = "SELECT name, address, hours, open_closed, menu, "
                stmt_str += "media, tags, review_count, stars, image, "
                stmt_str += "price, cuisine, type FROM requests "
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
                    info_obj['price'] = str(row[10])
                    info_obj['cuisine'] = str(row[11])
                    info_obj['type'] = str(row[12])

                return info_obj

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")
