#!/usr/bin/python
# -------------------------------------------------------------------------------
# create_table.py
# Group: Trenton Eats Local
# Author(s): Piers Ozuah, Justice Chukwuma


from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2


def insert_mock():
    # """ insert play bowls"""
    # commands = (
    #     """
    #     INSERT INTO restaurants (restaurant_id, name, address, hours,
    #     open_closed, menu, media, tags, review_count, stars )
    #     VALUES ('1', 'Playa Bowls', '24 Trenton Avenue, Trenton, NJ',
    #     '9am-5pm everyday', TRUE, 'Playa Bowlsabowls.com/trenton',
    #     'playabowlos.com/media', ['Acai, Fruit'] , 15, 4.2)
    #     )
    #     """
    # )

    # The following code was adapted from POSTGRESQL TUTORIAL
    mockrestaurants = []
    #------------------------------------------------------------------
    base = "INSERT INTO restaurants (restaurant_id, name, address, hours,"
    base += "open_closed, menu, media, tags, review_count, stars )"
    #------------------------------------------------------------------
    res1 = base
    res1 += "VALUES ('1', 'Playa Bowls', '24 Trenton Avenue, Trenton, NJ',"
    res1 += "'9am-5pm MTuWThFSaSu', TRUE, 'PlayaBowlsabowls.com/trenton',"
    res1 += "'playabowlos.com/media', 'Acai' , 15, 4.2)"
    #------------------------------------------------------------------
    res2 = base
    res2 += "VALUES ('2', 'Papa's Pizza', '13 Morrison Boulevard, Trenton, NJ',"
    res2 += "'7am-9pm MTuWThFSa', TRUE, 'None',"
    res2 += "'instagram.com/papapizzatrenton',"
    res2 += "'Pizza' , 20, 3.9)"
    #------------------------------------------------------------------
    res3 = base
    res3 += "VALUES ('3', 'Tico's', '2169 Stuyvesant Street, Trenton, NJ',"
    res3 += "'12pm-6pm MTuWThF', FALSE, 'ticos.com/trenton',"
    res3 += "['facebook.com/trentonticos', 'instagram.com/trentonticos'],"
    res3 += "'Acai, 7, 2.3)"
    #------------------------------------------------------------------
    res4 = base
    res4 += "VALUES ('4', 'Ramen Stop', '7 Boyden Lane, Trenton, NJ',"
    res4 += "'9am-10pm MTuThFSa', FALSE, 'ramenstopnj.com/trenton',"
    res4 += "'None', 'Ramen', 11, 4.7)"

    mockrestaurants=[res1, res2, res3, res4]

    try:
        with connect(
                host='localhost', port=5432, user='rmd', password='trentoneats333',
                database='trentoneats') as connection:

            with connection.cursor() as cursor:
                # # fill in table one by one
                for command in mockrestaurants:
                    cursor.execute(command)
                # close communication with the PostgreSQL database server
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        exit(1)


if __name__ == '__main__':
    insert_mock()
