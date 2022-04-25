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

# def __professor__():
#     stmt_str = "SELECT profname "
#     stmt_str += "FROM profs, coursesprofs, classes "
#     stmt_str += "WHERE profs.profid = coursesprofs.profid "
#     stmt_str += "AND classes.courseid = coursesprofs.courseid "
#     stmt_str += "AND classes.classid = ? "
#     stmt_str += "ORDER BY profname"
#     return stmt_str

# def __dept_and_num__():
#     # Dept + number
#     stmt_str = "SELECT dept, coursenum "
#     stmt_str += "FROM crosslistings, classes "
#     stmt_str += "WHERE crosslistings.courseid = classes.courseid "
#     stmt_str += "AND classes.classid = ? "
#     stmt_str += "ORDER BY dept, coursenum"
#     return stmt_str

# def __main_selection__():
#     # Selections
#     stmt_str = "SELECT classid, courses.courseid, days, "
#     stmt_str += "starttime, endtime, "
#     stmt_str += "bldg, roomnum, dept, coursenum, area, title, "
#     stmt_str += "descrip, prereqs "

#     # From
#     stmt_str += "FROM classes, courses, crosslistings "

#     # Where Statements
#     stmt_str += "WHERE courses.courseid = crosslistings.courseid "
#     stmt_str += "AND courses.courseid = classes.courseid "
#     stmt_str += "AND classes.courseid = crosslistings.courseid "

#     #FINAL AND -> ClassID
#     stmt_str += "AND classid = ? "
#     return stmt_str

# def courseid(row):
#     """return course id"""
#     return str(row[1])

# def __search__(class_id):
#     class_id = str(class_id)
#     try:
#         with connect(DATABASE_URL, isolation_level=None,
#             uri=True) as connection:

#             with closing(connection.cursor()) as cursor:
#                 stmt_str = __main_selection__()
#                 cursor.execute(stmt_str, [class_id])
#                 row = cursor.fetchone()

#                 #CourseId
#                 printstr = str(row[1]) + '\n'

#                 #Days, Start Time, End Time, Building, Room
#                 printstr += str(row[2]) + '\n'
#                 printstr += str(row[3]) + '\n'
#                 printstr += str(row[4]) + '\n'
#                 printstr += str(row[5]) + '\n'
#                 printstr += str(row[6]) + '\n'

#                 #temp statement for your department and number
#                 temp_statement = __dept_and_num__()
#                 cursor.execute(temp_statement, [class_id])
#                 row = cursor.fetchone()

#                 while row is not None:
#                     printstr += str(row[0]) + ' ' + str(row[1])
#                     row = cursor.fetchone()
#                     printstr += '@'

#                 cursor.execute(stmt_str, [class_id])
#                 row = cursor.fetchone()

#                 printstr += '\n'

#                 #Area
#                 printstr += str(row[9]) + '\n'

#                 #Title
#                 printstr += str(row[10]) + '\n'

#                 #Description
#                 printstr += str(row[11]) + '\n'

#                 #Prerequisites
#                 printstr += str(row[12]) + '\n'

#                 # temp statement for professor
#                 temp_statement = __professor__()

#                 cursor.execute(temp_statement, [class_id])
#                 row = cursor.fetchone()

#                 while row is not None:
#                     printstr += str(row[0])
#                     row = cursor.fetchone()
#                     printstr += '@'

#                 cursor.execute(stmt_str, [class_id])
#                 row = cursor.fetchone()

#                 printstr = printstr.replace(',', ', ')
#                 printstr = printstr.replace('.', '. ')
#                 return printstr

#     except DatabaseError as error:
#         print(sys.argv[0] + ": " + str(error), file=stderr)
#         error_msg = "A server error occurred. "
#         error_msg += "Please contact the system administrator."
#         return error_msg


#     except TypeError:
#         # Currently hard coded in... can we fix?
#         print(sys.argv[0] + ": no class with classid ",
#                             class_id, " exists", file=stderr)
#         error_msg = sys.argv[0] + ": no class with classid "
#         error_msg += class_id + " exists"
#         return error_msg
#         #sys.exit(1)

def adjust_inputs(restaurant):
    """format classes"""
    restaurant = restaurant.replace('%', r'\%')
    restaurant = restaurant.replace('_', r'\_')
    # This line probably not encessary lol
    if restaurant == "placeholder":
        restaurant = "%"

    # num = num.replace('%', r'\%')
    # num = num.replace('_', r'\_')
    # if num == "placeholder":
    #     num = "%"

    # area = area.replace('%', r'\%')
    # area = area.replace('_', r'\_')
    # if area == "placeholder":
    #     area = "%"

    # title = title.replace('%', r'\%')
    # title = title.replace('_', r'\_')
    # if title == "placeholder":
    #     title = "%"

    # inputs = [dept, num, area, title]
    # return inputs
    return restaurant

# def restaurant_search(input): #, tags, price, type, cuisine):
#     """search through restaurants"""
#     try:
#         print('Trying')
#          #with connect(host='localhost', port=5432, user='rmd', password='xxx',
#         #              database="trentoneats") as connection:
#         # dequ5ope4nuoit
#         with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
#                      database="dequ5ope4nuoit") as connection:
#
#             print("****")
#             with closing(connection.cursor()) as cursor:
#                 print('Tried')
#
#                 # This needs to be adjustedf
#                 stmt_str = "SELECT restaurant_id, name, open_closed, address, "
#                 stmt_str += "stars, cuisine, type, price, tags "
#                 stmt_str += "FROM restaurants "
#                 stmt_str += "WHERE LOWER(name) ILIKE %s;"
#
#
#                 input = '%' + input.lower() + '%'
#
#                 print(stmt_str)
#                 cursor.execute(stmt_str, [input])
#                 row = cursor.fetchone()
#
#                 # course list
#                 restaurants = []
#
#                 # rowstringlist this rowstring will contain all of the necessary values
#
#                 rowstring = ["", "", "", "", "", "", "", "", ""]
#
#                 # This iwll parse through the rows and get all of the necsary values
#                 while row:
#                     rowstring[0] = row[0]
#                     rowstring[1] = row[1]
#                     rowstring[2] = row[2]
#                     rowstring[3] = row[3]
#                     rowstring[4] = row[4]
#                     rowstring[5] = row[5]
#                     rowstring[6] = row[6]
#                     rowstring[7] = row[7]
#                     rowstring[8] = row[8]
#                     res = restaurant(rowstring)
#                     restaurants.append(res)
#                     row = cursor.fetchone()
#
#                 return restaurants
#
#     # Normally exit status 0.
#     # If database-related error, terminate with exit status 1.
#     # If erroneous command-line arguments terminate with exit status 2
#
#     except DatabaseError as error:
#         print(sys.argv[0] + ": " + str(error), file=stderr)
#         return ("stdservererr")

def restaurant_search(input, cuisine, type, price): #, tags, price, type, cuisine):
    """search through restaurants"""
    try:
        # with connect(host='localhost', port=5432, user='rmd', password='xxx',
        #               database="trentoneats") as connection:
        # dequ5ope4nuoit
         with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                    database="dequ5ope4nuoit") as connection:

            with closing(connection.cursor()) as cursor:

                # This needs to be adjusted
                nullPrice = False
                nullType = False
                stmt_str = "SELECT restaurant_id, name, open_closed, address, "
                stmt_str += "stars, cuisine, type, price, tags "
                stmt_str += "FROM restaurants "
                stmt_str += "WHERE LOWER(name) ILIKE %s "
                if price == "":
                    nullPrice = True
                else:
                    stmt_str += "AND LOWER(price) ILIKE %s "
                    price = '%' + price.lower() + '%'
                if type == "":
                    nullType = True
                else:
                    stmt_str += "AND LOWER(type) ILIKE %s"
                    type = '%' + type.lower() + '%'
                if cuisine != "%%":
                    c = cuisine.lower().split(",")
                    for i in c:
                        stmt_str += " AND LOWER(cuisine) ILIKE '%" + i + "%'"

                stmt_str += ";"

                input = '%' + input.lower() + '%'

                print(stmt_str)
                if not nullPrice and not nullType:
                    print('Hit 1')
                    cursor.execute(stmt_str, [input, price, type])
                    print(stmt_str % (input, price, type))
                elif not nullType:
                    print('Hit 2')
                    cursor.execute(stmt_str, [input, type])
                    print(stmt_str % (input, type))
                elif not nullPrice:
                    print('Hit 3')
                    cursor.execute(stmt_str, [input, price])
                    print(stmt_str % (input, price))
                else:
                    print('Hit 5')
                    print(stmt_str % input)
                    cursor.execute(stmt_str, [input])
                    #cursor.execute(stmt_str)

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
         #with connect(host='localhost', port=5432, user='rmd', password='xxx',
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
