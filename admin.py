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

def admin_search(email):
    """search through restaurants"""
    try:
    
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted
                stmt_str = "SELECT email "
                stmt_str += "FROM administrators "
                stmt_str += "WHERE email = '" + email + "'; "

                cursor.execute(stmt_str, [email])
                #cursor.execute(stmt_str, ["'bbq'"])
                row = cursor.fetchone()

                # course list
                admins = []

                # rowstringlist this rowstring will contain all of the necessary values

                rowstring = [""]

                # This iwll parse through the rows and get all of the necsary values
                while row is not None:
                    rowstring = [""]
                    rowstring[0] = row[0]
                    admins.append(rowstring)
                    row = cursor.fetchone()
                if (len(admins) > 0):
                    return True
                return False
                # if row is not None:
                #     return True
                # return False

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return False
        # return ("stdservererr")
