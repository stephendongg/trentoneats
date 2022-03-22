#!/usr/bin/env python
"""This is search.py"""
#-----------------------------------------------------------------------
# search.py
#-----------------------------------------------------------------------

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
#loading


from restaurant import restaurant 


#-----------------------------------------------------------------------
#Old Database -> for the original reg
#DATABASE_URL = 'file:reg.sqlite?mode=ro'

# New database for restaurants 
DATABASE_URL = 'file:teldatabase.sql?mode=ro'
#-----------------------------------------------------------------------

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


def restaurant_search(input):
    """search through courses"""
    try:
        with connect(host='localhost', port=5432, user='rmd', password='xxx',
        database="trentoneats") as connection:


            with closing(connection.cursor()) as cursor:
                # This needs to be adjusted 
                stmt_str = "SELECT restaurant_id, name "
                stmt_str += "FROM restaurants "
                stmt_str += "WHERE name LIKE '%" + input + "%' "
                #stmt_str += 'WHERE name LIKE ? ESCAPE "\\"'

                # stmt_str = "SELECT classid, dept, "
                # stmt_str += "coursenum, area, title "
                # stmt_str += "FROM classes, courses, "
                # stmt_str += "crosslistings "
                # stmt_str += "WHERE courses.courseid = "
                # stmt_str += "crosslistings.courseid "
                # stmt_str += "AND courses.courseid = "
                # stmt_str += "classes.courseid "
                # stmt_str += "AND classes.courseid = "
                # stmt_str += "crosslistings.courseid "

# here will be where restaurant is diffenret 
                #stmt_str += 'WHERE name LIKE ' + input

                # stmt_str += "ORDER BY dept,"
                # stmt_str += "coursenum, classid"

                cursor.execute(stmt_str)

                row = cursor.fetchone()

                # course list
                restaurants = []

                #rowstringlist this rowstring will contain all of the necessary values

                rowstring = ["", ""]

                # This iwll parse through the rows and get all of the necsary values 
                while row is not None:
                    rowstring[0] = str(row[0])
                    rowstring[1] = str(row[1])
                    restaurants.append(restaurant(rowstring))
                    row = cursor.fetchone()

                return restaurants

    # Normally exit status 0.
    # If database-related error, terminate with exit status 1.
    # If erroneous command-line arguments terminate with exit status 2

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        return ("stdservererr")



