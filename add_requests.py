#!/usr/bin/env python

# -----------------------------------------------------------------------
# add_restaurant.py
# Author: Justice Chukwuma & Piers Ozuah
# -----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2

# -----------------------------------------------------------------------

# Current issue: figuring out how to know what to put in for open


def add_requests(restaurantName, restaurantAddress, restaurantHours,
                 restaurantMenu, restaurantMedia, restaurantTags, cuisine, type, price, restaurantImage):
    stmt_str = """
    INSERT INTO requests (name, address, hours,
    open_closed, menu, media, tags, review_count, stars, cuisine, type, price, image)
    VALUES ( '"""
    stmt_str += restaurantName + "','" + restaurantAddress + "','"
    stmt_str += restaurantHours + "', 'TRUE', '" + restaurantMenu + "', '"
    stmt_str += restaurantMedia + "', '" + restaurantTags + "', '0', '0', '"
    stmt_str += ", '".join(cuisine) + "', '" + ", '".join(type)
    stmt_str += "', '" + price + "', '" + restaurantImage + "');"

    try:
        # with connect(
        #         host='localhost', port=5432, user='rmd', password='trentoneats333',
        #         database='trentoneats') as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:
            with connection.cursor() as cursor:
                print(stmt_str)
                cursor.execute(stmt_str,
                 [restaurantName, restaurantAddress, restaurantHours,
                 restaurantMenu, restaurantMedia, restaurantTags,
                 restaurantIamge, cuisine, type, price])

    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex, file=stderr)
        exit(1)

# -----------------------------------------------------------------------


if __name__ == '__main__':
    add_requests()
