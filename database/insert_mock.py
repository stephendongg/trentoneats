#!/usr/bin/python
# -------------------------------------------------------------------------------
# create_table.py
# Group: Trenton Eats Local
# Author: Piers Ozuah


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
    #     'playabowlos.com/media', 'Acai, Fruit' , 15, 4.2)
    #     )
    #     """
    # )

    # The following code was adapted from POSTGRESQL TUTORIAL

    try:
        # with connect(
        #         host='localhost', port=5432, user='rmd', password='trentoneats333',
        #         database='trentoneats') as connection:
        with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
                     database="dequ5ope4nuoit") as connection:
            with connection.cursor() as cursor:
                # # create table one by one
                # for command in commands:
                cursor.execute("""
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars, image)
        VALUES ('Playa Bowls', '24 Trenton Avenue, Trenton, NJ',
        '9am-5pm everyday', TRUE, 'None',
        'playabowlos.com/media', 'Acai, Fruit' , 15, 4.2, 'test')
        """
        )

                # close communication with the PostgreSQL database server
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    insert_mock()
