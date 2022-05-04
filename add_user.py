#!/usr/bin/env python

# -----------------------------------------------------------------------
# add_user.py
# Author: Piers Ozuah
# -----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2

# -----------------------------------------------------------------------

# Current issue: figuring out how to know what to put in for open


def add_customer(unique_id, name):
    id = str(unique_id)
    name = str(name)
    stmt_str = """
    INSERT INTO customers (customer_id, name, review_count , avg_rating,
    account_type, reported_count)
    SELECT """
    stmt_str += id + ', ' + "'" + name + "'" + ', 0, 0, 0, 0'
    stmt_str += """ WHERE NOT EXISTS (
    SELECT 1 FROM customers WHERE customer_id= """ + "(CAST('" + id + "' AS VARCHAR(255))))"

    try:
        # with connect(
        #         host='localhost', port=5432, user='rmd', password='trentoneats333',
        #         database='trentoneats') as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with connection.cursor() as cursor:
                print(stmt_str)
                cursor.execute(stmt_str)

    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex, file=stderr)
        exit(1)


def add_user(unique_id):
    id = str(unique_id)
    stmt_str = """
    INSERT INTO usertype (user_id, customer_id, admin, restaurant, customer)
    SELECT """
    stmt_str += id + ', ' + id + ', FALSE, FALSE, TRUE'
    stmt_str += """ WHERE NOT EXISTS (
    SELECT 1 FROM usertype WHERE user_id= """ + "(CAST('" + id + "' AS VARCHAR(255))))"

    try:
        # with connect(
        #         host='localhost', port=5432, user='rmd', password='trentoneats333',
        #         database='trentoneats') as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with connection.cursor() as cursor:
                print(stmt_str)
                cursor.execute(stmt_str)

    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex, file=stderr)
        exit(1)

# -----------------------------------------------------------------------


def old_user(unique_id):
    id = str(unique_id)
    stmt_str = """
    SELECT CASE WHEN EXISTS (SELECT * FROM usertype WHERE user_id =
    """
    stmt_str += "(CAST('" + id + "' AS VARCHAR(255)))) THEN TRUE ELSE FALSE END"
    try:
        # with connect(
        #         host='localhost', port=5432, user='rmd', password='trentoneats333',
        #         database='trentoneats') as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with connection.cursor() as cursor:
                print(stmt_str)
                cursor.execute(stmt_str)

    except (Exception, psycopg2.DatabaseError) as ex:
        print(ex, file=stderr)
        exit(1)
