#!/usr/bin/env python
"""This is users.py.py"""
# -----------------------------------------------------------------------
# requests.py
# Piers Ozuah
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
import restaurant
import argparse
# loading


from restaurant import restaurant


# -----------------------------------------------------------------------
# Old Database -> for the original reg
#DATABASE_URL = 'file:reg.sqlite?mode=ro'

# New database for restaurants
DATABASE_URL = 'file:trentoneats.sql?mode=ro'
# -----------------------------------------------------------------------


def delete_request(request_id):
    """delete a restaurant from the requests table"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #              database="trentoneats") as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                stmt_str = "DELETE FROM requests "
                stmt_str += "WHERE request_id =" + request_id + ";"

                print(stmt_str)
                cursor.execute(stmt_str, [request_id])

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")


def delete_request_add_res(request_id):
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
                stmt_str += "WHERE request_id = '" + request_id + "'; "

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

    #             stmt_str2 = """
    # INSERT INTO restaurants (name, address, hours,
    # open_closed, menu, media, tags, review_count, stars, cuisine, type, price, image)
    # VALUES ( '"""
    #             stmt_str2 += info_obj['name'] + \
    #                 "','" + info_obj['address'] + "','"
    #             stmt_str2 += info_obj['hours'] + "'" + \
    #                 "," + info_obj['open_closed'] + \
    #                 "," + info_obj['menu'] + ", "
    #             stmt_str2 += info_obj['media'] + ", " + \
    #                 info_obj['tags'] + ", '0', '0', "
    #             stmt_str2 += "".join(info_obj['cuisine']) + ", "
    #             stmt_str2 += "" + \
    #                 ", ".join(info_obj['type']) + \
    #                 "', '" + "," + info_obj['price']
    #             stmt_str2 += "', " + info_obj['image'] + ");"

                stmt_str2 = """
    INSERT INTO restaurants (name, address, hours,
    open_closed, menu, media, tags, review_count, stars, image, cuisine, type, price)
    VALUES ( '"""
                stmt_str2 += info_obj['name'] + \
                    "','" + info_obj['address'] + "','"
                stmt_str2 += info_obj['hours'] + \
                    "', 'TRUE', '" + info_obj['menu'] + "', '"
                stmt_str2 += info_obj['media'] + "', '" + \
                    info_obj['tags'] + "', '0', '0', '"
                stmt_str2 += info_obj['image'] + "', "
                stmt_str2 += "'" + \
                    ", " + info_obj['cuisine'] + \
                    "', '" + ", " + info_obj['type']
                stmt_str2 += "', '" + info_obj['price'] + "');"

                print(stmt_str2)
                cursor.execute(stmt_str2)

                stmt_str3 = "DELETE FROM requests "
                stmt_str3 += "WHERE request_id =" + request_id + ";"

                print(stmt_str3)
                cursor.execute(stmt_str3)

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")
