#!/usr/bin/env python

#-----------------------------------------------------------------------
# add_restaurant.py
# Author: Justice Chukwuma
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2

#-----------------------------------------------------------------------

# Current issue: figuring out how to know what to put in for id and open

def add_restaurant(restaurantName, restaurantAddress, restaurantHours,
restaurantMenu, restaurantMedia, restaurantTags, cuisine, type, price):
    stmt_str = """
    INSERT INTO restaurants (name, address, hours,
    open_closed, menu, media, tags, review_count, stars, cuisine, type, price)
    VALUES ( '"""
    stmt_str += restaurantName + "','" + restaurantAddress + "','"
    stmt_str += restaurantHours + "', 'TRUE', '" + restaurantMenu + "', '"
    stmt_str += restaurantMedia + "', '" + restaurantTags + "', '0', '0', "
    stmt_str += "'" + ", ".join(cuisine) + "', '" + ", ".join(type)
    stmt_str += "', '" + price + "');"

    try:
        with connect(
            host='localhost', port=5432, user='rmd', password='trentoneats333',
            database='trentoneats') as connection:

            with connection.cursor() as cursor:
                print(stmt_str)
                cursor.execute(stmt_str)


    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    add_restaurant()
