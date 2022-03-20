#!/usr/bin/env python

#-----------------------------------------------------------------------
# create.py
# Author: Justice CHukwuma
#-----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect

#-----------------------------------------------------------------------

def main():
    create_restaurant_string = "CREATE TABLE IF NOT EXISTS restaurants (" 
    create_restaurant_string += "restaurant_id VARCHAR(20) PRIMARY KEY," 
    create_restaurant_string += "name VARCHAR(255) NOT NULL," 
    create_restaurant_string += "address VARCHAR(255) NOT NULL," 
    create_restaurant_string += "hours VARCHAR(255) NOT NULL," 
    create_restaurant_string += "open_closed BOOLEAN," 
    create_restaurant_string += "menu VARCHAR(255)," 
    create_restaurant_string += "media VARCHAR(255)," 
    create_restaurant_string += "tags VARCHAR(255)," 
    create_restaurant_string += "review_count INTEGER," 
    create_restaurant_string += "stars FLOAT NOT NULL)"


    create_customer_string = "CREATE TABLE IF NOT EXISTS customers (" 
    create_customer_string += "customer_id VARCHAR(20) PRIMARY KEY," 
    create_customer_string += "name VARCHAR(255)," 
    create_customer_string += "review_count INTEGER NOT NULL," 
    create_customer_string += "avg_rating FLOAT NOT NULL," 
    create_customer_string += "account_type VARCHAR(255) NOT NULL," 
    create_customer_string += "reported_count INT)"

    create_review_string = "CREATE TABLE IF NOT EXISTS reviews (" 
    create_review_string += "review_id INTEGER PRIMARY KEY," 
    create_review_string += "customer_id VARCHAR(20)," 
    create_review_string += "FOREIGN KEY (customer_id)" 
    create_review_string += "REFERENCES customers (customer_id)," 
    
    create_review_string += "restaurant_id VARCHAR(20)," 
    create_review_string += "FOREIGN KEY (restaurant_id)" 
    create_review_string += "REFERENCES restaurants (restaurant_id)," 
    create_review_string += "date TIMESTAMP NOT NULL," 
    create_review_string += "text TEXT NOT NULL," 
    create_review_string += "price INTEGER," 
    create_review_string += "taste INTEGER," 
    create_review_string += "authenticity INTEGER," 
    create_review_string += "coolness INTEGER," 
    create_review_string += "overall INTEGER)"

    create_categories_string = "CREATE TABLE IF NOT EXISTS categories (" 
    create_categories_string += "category VARCHAR(20) PRIMARY KEY," 
    create_categories_string += "restaurant_id VARCHAR(20)," 
    create_categories_string += "FOREIGN KEY (restaurant_id)" 
    create_categories_string += "REFERENCES restaurants (restaurant_id))" 


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
