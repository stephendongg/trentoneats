#!/usr/bin/python
# -------------------------------------------------------------------------------
# create_table.py
# Group: Trenton Eats Local
# Author: Piers Ozuah

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE [IF NOT EXISTS] restaurants (
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
        """ 
        CREATE TABLE [IF NOT EXISTS] customers (
                customer_id VARCHAR(20) PRIMARY KEY,
                name VARCHAR(255),
                review_count INTEGER NOT NULL,
                avg_rating FLOAT NOT NULL,
                account_type VARCHAR(255) NOT NULL,
                reported_count INT
                )
        """,
        """
        CREATE TABLE [IF NOT EXISTS] reviews (
                review_id INTEGER PRIMARY KEY,
                FOREIGN KEY (customer_id) 
                REFERENCES customers (customer_id),
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
        CREATE TABLE [IF NOT EXISTS] categories (
                category VARCHAR(20) PRIMARY KEY,
                FOREIGN KEY (restaurant_id)
                REFERENCES restaurants (restaurant_id)
        )
        """)
    conn = None

# The following code was adapted from POSTGRESQL TUTORIAL

    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

        conn.close()


if __name__ == '__main__':
    create_tables()
