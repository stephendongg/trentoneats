"""this is restaurant.py"""
#-----------------------------------------------------------------------
# restaurant.py
#-----------------------------------------------------------------------
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
# Rowstring[0] -> restaurantid
# rowstring[1] -> name
class restaurant:
    """class Restaurant"""

    # Note: Rowstring is a list of inputs that needs to go into a restaurant
    def __init__(self, rowstring):
        # --- The following will be modified to work for restaurants
        self._restaurantid = rowstring[0]
        self._name = rowstring[1]
        self._openclose = rowstring[2]
        self._address = rowstring[3]
        self._stars = rowstring[4]
        self._cuisine = rowstring[5]
        self._type = rowstring[6]
        self._price = rowstring[7]
        self._tag = rowstring[8]
        self._hours = rowstring[9]


    # def __str__(self):
    # # --- The following will be modified to work for restaurants
    #     string_form = str(self._name) + ' '
    #     # string_form += str(self._dept) + ' '
    #     # string_form += str(self._course_num) + ' '
    #     # string_form += str(self._area) + ' '
    #     # string_form += str(self._title)
    #     return string_form

    # def by_id(cls, id):
    #     """search through restaurants"""
    #     try:
    #         #with connect(host='localhost', port=5432, user='rmd', password='xxx',
    #         #              database="trentoneats") as connection:
    #         # dequ5ope4nuoit
    #         with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
    #                     database="dequ5ope4nuoit") as connection:

    #             with closing(connection.cursor()) as cursor:
    #                 # This needs to be adjusted
    #                 stmt_str = "SELECT restaurant_id, name, open_closed, address, "
    #                 stmt_str += "stars, cuisine, type, price, tags "
    #                 stmt_str += "FROM restaurants "
    #                 stmt_str += "WHERE restaurant_id = '" + id + "';"

    #                 #print(input)
    #                 cursor.execute(stmt_str, [id])
    #                 row = cursor.fetchone()

    #                 # course list
    #                 restaurants = []

    #                 # rowstringlist this rowstring will contain all of the necessary values

    #                 rowstring = ["", "", "", "", "", "", "", "", ""]

    #                 # This iwll parse through the rows and get all of the necsary values
    #                 rowstring[0] = row[0]
    #                 rowstring[1] = row[1]
    #                 rowstring[2] = row[2]
    #                 rowstring[3] = row[3]
    #                 rowstring[4] = row[4]
    #                 rowstring[5] = row[5]
    #                 rowstring[6] = row[6]
    #                 rowstring[7] = row[7]
    #                 rowstring[8] = row[8]
    #                 return cls(rowstring)
    #     except DatabaseError as error:
    #         print(sys.argv[0] + ": " + str(error), file=stderr)
    #         return ("stdservererr")

    # Make sure to have name
    def get_name(self):
        """restaurant name"""
        return self._name

    def get_restaurantid(self):
        """restaurant ID"""
        return self._restaurantid

    def get_openclose(self):
        """restaurant open or closed"""
        return self._openclose

    def get_address(self):
        """restaurant address"""
        return self._address

    def get_stars(self):
        """restaurant stars"""
        return self._stars


    def get_cuisine(self):
        """restaurant cuisine"""
        return self._cuisine

    def get_type(self):
        """restaurant type"""
        return self._type

    def get_price(self):
        """restaurant price"""
        return self._price

    def get_hours(self):
        """restaurant hours"""
        return self._hours
