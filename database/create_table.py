#!/usr/bin/python
# -------------------------------------------------------------------------------
# create_table.py
# Group: Trenton Eats Local
# Author: Piers Ozuah


from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS restaurants (
            restaurant_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            hours VARCHAR(255) NOT NULL,
            open_closed BOOLEAN,
            menu VARCHAR(255),
            media VARCHAR(255),
            tags VARCHAR(255),
            review_count INTEGER,
            stars FLOAT NOT NULL,
            cuisine VARCHAR(255),
            type VARCHAR(255),
            price VARCHAR(255),
            image VARCHAR(225)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS customers (
                customer_id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                review_count INTEGER NOT NULL,
                avg_rating FLOAT NOT NULL,
                account_type VARCHAR(255) NOT NULL,
                reported_count INT
                )
        """,
        """
        CREATE TABLE IF NOT EXISTS reviews (
                review_id SERIAL PRIMARY KEY,
                restaurant_id SERIAL,
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
                restaurant_id SERIAL PRIMARY KEY,
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
        # """
        # CREATE TABLE IF NOT EXISTS usertype (
        #     user_id SERIAL PRIMARY KEY,
        #     customer_id SERIAL,
        #     FOREIGN KEY (customer_id)
        #     REFERENCES customers (customer_id),
        #     restaurant_id SERIAL,
        #     FOREIGN KEY (restaurant_id)
        #     REFERENCES restaurants (restaurant_id),
        #     admin BOOLEAN,
        #     restaurant BOOLEAN,
        #     customer BOOLEAN

        # )
        # """
        """
        CREATE TABLE IF NOT EXISTS administrators (
            email VARCHAR(255) NOT NULL PRIMARY KEY
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS users (
            email VARCHAR(255) NOT NULL PRIMARY KEY,
            googleid INTEGER,
            name VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS requests (
            request_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            address VARCHAR(255) NOT NULL,
            hours VARCHAR(255) NOT NULL,
            open_closed BOOLEAN,
            menu VARCHAR(255),
            media VARCHAR(255),
            tags VARCHAR(255),
            review_count INTEGER,
            stars FLOAT NOT NULL,
            cuisine VARCHAR(255),
            type VARCHAR(255),
            price VARCHAR(255),
            image VARCHAR(225)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS favoriterestaurants (
            favoriterestaurantid SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            FOREIGN KEY (email)
            REFERENCES users (email),
            restaurant_id SERIAL NOT NULL,
            FOREIGN KEY (restaurant_id)
            REFERENCES restaurants (restaurant_id)
            
        )
        """)
    # restaurant_id SERIAL

# The following code was adapted from POSTGRESQL TUTORIAL

    try:
        # with connect(
        #         host='localhost', port=5432, user='rmd', password='trentoneats333',
        #         database='trentoneats') as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:

            with connection.cursor() as cursor:
                # create table one by one
                for command in commands:
                    cursor.execute(command)
                # close communication with the PostgreSQL database server
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    create_tables()
