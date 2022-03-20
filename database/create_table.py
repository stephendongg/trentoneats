#!/usr/bin/python
# -------------------------------------------------------------------------------
# create_table.py
# Group: Trenton Eats Local
# Author: Piers Ozuah

<<<<<<< HEAD

from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2
=======
from psycopg2 import connect, DatabaseError
from config import config
>>>>>>> searchbar_test


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS restaurants (
            restaurant_id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            hours VARCHAR(255) NOT NULL,
            open_closed BOOLEAN,
            menu VARCHAR(255),
            media VARCHAR(255),
            tags VARCHAR(255),
            review_count INTEGER,
            stars FLOAT NOT NULL
        )
        """,
<<<<<<< HEAD
        """ 
        CREATE TABLE IF NOT EXISTS customers (
=======
        """
        CREATE TABLE [IF NOT EXISTS] customers (
>>>>>>> searchbar_test
                customer_id VARCHAR(20) PRIMARY KEY,
                name VARCHAR(255),
                review_count INTEGER NOT NULL,
                avg_rating FLOAT NOT NULL,
                account_type VARCHAR(255) NOT NULL,
                reported_count INT
                )
        """,
        """
        CREATE TABLE IF NOT EXISTS reviews (
                review_id INTEGER PRIMARY KEY,
<<<<<<< HEAD
                customer_id VARCHAR(20),
                FOREIGN KEY (customer_id) 
=======
                FOREIGN KEY (customer_id)
>>>>>>> searchbar_test
                REFERENCES customers (customer_id),
                restaurant_id VARCHAR(20),
                FOREIGN KEY (restaurant_id)
                REFERENCES restaurants (restaurant_id),
                date TIMESTAMP NOT NULL,
                text TEXT NOT NULL,
                price INTEGER,
                taste INTEGER,
                authenticity INTEGER,
                coolness INTEGER,
                overall INTEGER
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS categories (
                restaurant_id VARCHAR(20) PRIMARY KEY,
                fast_food BOOLEAN,
                fine_dining BOOLEAN,
                casual_dining BOOLEAN,
                inexpensive BOOLEAN,
                moderate_price BOOLEAN,
                pricey BOOLEAN,
                priciest BOOLEAN,
                american BOOLEAN,
                french BOOLEAN,
                indian BOOLEAN,
                FOREIGN KEY (restaurant_id)
                REFERENCES restaurants (restaurant_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS usertype (
            user_id VARCHAR(20) PRIMARY KEY,
            customer_id VARCHAR(20),
            FOREIGN KEY (customer_id) 
            REFERENCES customers (customer_id),
            restaurant_id VARCHAR(20),
            FOREIGN KEY (restaurant_id)
            REFERENCES restaurants (restaurant_id),
            admin BOOLEAN,
            restaurant BOOLEAN,
            customer BOOLEAN

        )
        """)

# The following code was adapted from POSTGRESQL TUTORIAL

    try:
<<<<<<< HEAD
        with connect(
                host='localhost', port=5432, user='rmd', password='trentoneats333',
                database='teldatabase') as connection:

            with connection.cursor() as cursor:
                # create table one by one
                for command in commands:
                    cursor.execute(command)
                # close communication with the PostgreSQL database server
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

=======
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, DatabaseError) as error:
        print(error)

        #conn.close()

>>>>>>> searchbar_test

if __name__ == '__main__':
    create_tables()
