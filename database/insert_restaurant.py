#!/usr/bin/env python

# -----------------------------------------------------------------------
# insert_restaurant.py
# Author: Piers Ozuah
# Debugger: Justice Chukwuma
# -----------------------------------------------------------------------

from sys import argv, stderr, exit
from psycopg2 import connect
import psycopg2


def insert_restaurant():
    """ Insert our test restaurants"""

    commands = [
        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars)
        VALUES ('2',
        '1911 Smokehouse BBQ',
        '11 W Front St, Trenton, NJ 08608',
        'Monday	11AM - 3:30PM,
        Tuesday	11AM - 3:30PM,
        Wednesday 11AM - 10:30PM,
        Thursday 11AM - 10:30PM,
        Friday 11AM - 10:30PM,
        Saturday 1 - 10:30PM,
        Sunday 1 - 10:30PM', FALSE,
        'http://places.singleplatform.com/1911-smoke-house-barbeque/menu?ref=google',
        'https://1911bbq.com',
        'BBQ',
        12,
        5.0);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('3',
        'Bamboo Grill Jamaican Restaurant',
        '1005 Chambers St, Trenton, NJ 08611',
        'Monday	10AM - 7PM,
        Tuesday	10AM - 7PM,
        Wednesday 10AM - 7PM,
        Thursday 10AM - 7PM,
        Friday 10AM - 8PM,
        Saturday 10AM - 8PM,
        Sunday Closed', TRUE,
        'None',
        'None',
        'Jamaican, Grill',
        1,
        3.2);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('4',
        $$'Ila Mae's Restaurant'$$,
        '313 Market St, Trenton, NJ 08611',
        'Monday	Closed,
        Tuesday	9AM - 8PM,
        Wednesday 9AM - 8PM,
        Thursday 9AM - 8PM,
        Friday 9AM - 8PM,
        Saturday 9AM - 8PM,
        Sunday Closed', FALSE,
        'http://places.singleplatform.com/ila-maes-restaurant/menu?ref=google',
        'None',
        'Soul',
        10,
        4.3);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('5',
        'Blue Danube Restaurant',
        '538 Adeline St, Trenton, NJ 08611',
        'Monday	Closed
        Tuesday	11:30AM - 2:15PM, 5 - 7:30PM,
        Wednesday 11:30AM - 2:15PM, 5 - 7:30PM,
        Thursday 11:30AM - 2:15PM, 5 - 7:30PM,
        Friday 11:30AM - 2:15PM, 5 - 8PM,
        Saturday 3 - 8PM,
        Sunday 3 - 7:30PM', TRUE,
        'http://www.bluedanuberestaurant.net/menu.php',
        'http://www.bluedanuberestaurant.net/about.php',
        'Eastern European' ,
        273,
        4.6);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('6',
        'The Big Easy of Trenton Restaurant',
        '111 S Warren St, Trenton, NJ 08608',
        'Monday	12 - 7PM,
        Tuesday	12 - 7PM,
        Wednesday 12 - 7PM,
        Thursday 12 - 7PM,
        Friday 12 - 7PM,
        Saturday 9AM - 5PM,
        Sunday Closed', FALSE,
        'None',
        'None',
        'Dine-in' ,
        260,
        4.5);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('7',
        $$'Don Julio's Bar and Grill'$$,
        '900 Liberty St, Trenton, NJ 08611',
        'Monday	11AM - 2AM,
        Tuesday	11AM - 2AM,
        Wednesday 11AM - 2AM,
        Thursday 11AM - 2AM,
        Friday 11AM - 2AM,
        Saturday 11AM - 2AM,
        Sunday 12PM - 2AM', TRUE,
        'None',
        'None',
        'Bar & Grill' ,
        190,
        4.3);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('8',
        'The Hummingbird Restaurant',
        '29 S Warren St, Trenton, NJ 08608',
        'Monday	10AM - 7PM,
        Tuesday	10AM - 7PM,
        Wednesday 10AM - 7PM,
        Thursday 10AM - 7PM,
        Friday 10AM - 6PM,
        Saturday 10AM - 6PM,
        Sunday Closed', FALSE,
        'None',
        'None',
        'Jamaican' ,
        282,
        4.2);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('9',
        'Sabor Latino',
        '293 Ashmore Ave, Trenton, NJ 08611',
        'Tuesday 10AM - 12AM,
        Wednesday Closed,
        Thursday 10AM - 12AM,
        Friday 10AM - 2AM,
        Saturday 10AM - 2AM,
        Sunday 10AM - 12AM,
        Monday 10AM - 12AM', TRUE,
        'None',
        'None',
        'Dominican' ,
        80,
        4.1);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('10',
        $$'Trentini's'$$,
        '635 S Clinton Ave, Trenton, NJ 08611',
        'Tuesday 10AM - 10PM,
        Wednesday 10AM - 10PM,
        Thursday 10AM - 10PM,
        Friday 10AM - 10PM,
        Saturday 10AM - 10PM,
        Sunday 10AM - 10PM,
        Monday 10AM - 10PM', FALSE,
        'https://trentinismenu.com/menu.html',
        'https://trentinismenu.com/index.html',
        'Italian' ,
        420,
        4.1);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('11',
        'Mama D Soul Food 2',
        '312 S Broad St, Trenton, NJ 08609',
        'Tuesday Closed,
        Wednesday 12 - 7PM,
        Thursday 12 - 7PM,
        Friday 12 - 7PM,
        Saturday 9AM - 7PM,
        Sunday 1 - 7PM,
        Monday Closed', TRUE,
        'None',
        'None',
        'Soul' ,
        112,
        3.9);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('12',
        $$'Cooper's Riverview'$$,
        '50 Riverview Plaza, Trenton, NJ 08611',
        'Tuesday 12PM - 2AM,
        Wednesday 12PM - 2AM,
        Thursday 12PM - 2AM,
        Friday 12PM - 2AM,
        Saturday 12PM - 2AM,
        Sunday 11:30AM - 11PM,
        Monday Closed', FALSE,
        'coopersnj.com',
        'None',
        'English' ,
        455,
        4.0);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('13',
        'Mi Ranchito Pizza and Tacos',
        '911 Chambers St, Trenton, NJ 08611',
        'Tuesday 10AM - 10PM,
        Wednesday Closed,
        Thursday 10AM - 10PM,
        Friday 10AM - 10PM,
        Saturday 10AM - 10PM,
        Sunday 10AM - 10PM,
        Monday 10AM - 10PM', TRUE,
        'None',
        'None',
        'Tacos' ,
        61,
        4.7);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('14',
        'El Potrillo',
        '541 Roebling Ave, Trenton, NJ 08611',
        'Tuesday Closed,
        Wednesday 10AM - 10PM,
        Thursday 10AM - 10PM,
        Friday 10AM - 10PM,
        Saturday 10AM - 10PM,
        Sunday 10AM - 10PM,
        Monday 10AM - 10PM', FALSE,
        'http://places.singleplatform.com/el-potrillo-mexican-restaurant-7/menu?ref=google',
        'None',
        'Mexican' ,
        213,
        3.9);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('15',
        'Chencha y Chole',
        '865 S Broad St, Trenton, NJ 08611',
        '11AM - 10PM everyday', TRUE,
        'None',
        'None',
        'Mexican' ,
        319,
        4.2);
        """,

        """
        INSERT INTO restaurants (restaurant_id, name, address, hours,
        open_closed, menu, media, tags, review_count, stars )
        VALUES ('16',
        'Casablanca Restaurant',
        '140 Washington St, Trenton, NJ 08611',
        'Monday	11AM - 2AM,
        Tuesday	11AM - 2AM,
        Wednesday 11AM - 2AM,
        Thursday 11AM - 2AM,
        Friday 11AM - 2AM,
        Saturday 11AM - 2AM,
        Sunday 11AM - 2AM', FALSE,
        'None',
        'None',
        'Spanish' ,
        372,
        4.1);
        """]


    try:
        with connect(
                host='localhost', port=5432, user='rmd', password='trentoneats333',
                database='trentoneats') as connection:

            with connection.cursor() as cursor:
                # # create table one by one
                for command in commands:
                    cursor.execute(command)

                # close communication with the PostgreSQL database server
                cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    insert_restaurant()
