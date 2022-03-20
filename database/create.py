#!/usr/bin/env python

#-----------------------------------------------------------------------
# create.py
# Author: Justice CHukwuma
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect

#-----------------------------------------------------------------------

def main():
    create_restaurant_string = "CREATE TABLE [IF NOT EXISTS] restaurants (" +
        "restaurant_id VARCHAR(20) PRIMARY KEY," +
        "name VARCHAR(255) NOT NULL," +
        "address VARCHAR(255) NOT NULL," +
        "hours VARCHAR(255) NOT NULL," +
        "open_closed BOOLEAN," +
        "menu VARCHAR(255)," +
        "media VARCHAR(255)," +
        "tags VARCHAR(255)," +
        "review_count INTEGER," +
        "stars FLOAT NOT NULL)"


    create_customer_string = "CREATE TABLE [IF NOT EXISTS] customers (" +
            "customer_id VARCHAR(20) PRIMARY KEY," +
            "name VARCHAR(255)," +
            "review_count INTEGER NOT NULL," +
            "avg_rating FLOAT NOT NULL," +
            "account_type VARCHAR(255) NOT NULL," +
            "reported_count INT)"

    create_review_string = "CREATE TABLE [IF NOT EXISTS] reviews (" +
            "review_id INTEGER PRIMARY KEY," +
            "FOREIGN KEY (customer_id)" +
            "REFERENCES customers (customer_id)," +
            "FOREIGN KEY (restaurant_id)" +
            "REFERENCES restaurants (restaurant_id)," +
            "date TIMESTAMP NOT NULL," +
            "text TEXT NOT NULL," +
            "price INTEGER," +
            "taste INTEGER," +
            "authenticity INTEGER," +
            "coolness INTEGER," +
            "overall INTEGER)"

    create_categories_string = "CREATE TABLE [IF NOT EXISTS] categories (" +
            "category VARCHAR(20) PRIMARY KEY," +
            "FOREIGN KEY (restaurant_id)" +
            "REFERENCES restaurants (restaurant_id))" 


    if len(argv) != 1:
        print('Usage: python create.py', file=stderr)
        exit(1)

    try:
        with connect(
            host='localhost', port=5432, user='rmd', password='trentoneats333',
            database='trentoneats') as connection:

            with connection.cursor() as cursor:

                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS restaurants")
                cursor.execute(create_restaurant_string)


                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS customers")
                cursor.execute(create_customer_string)

                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS reviews")
                cursor.execute(create_review_string)

                #-------------------------------------------------------

                cursor.execute("DROP TABLE IF EXISTS categories")
                cursor.execute(create_categories_string)

                #-------------------------------------------------------

    except Exception as ex:
        print(ex, file=stderr)
        exit(1)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
