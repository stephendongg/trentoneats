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
        INSERT INTO restaurants ( name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        '1911 Smokehouse BBQ',
        '11 W Front St, Trenton, NJ 08608',
        'Monday 11:00 AM - 3:30 PM, Tuesday 11:00 AM - 3:30 PM, Wednesday 11:00 AM - 10:30 PM, Thursday 11:00 AM - 10:30 PM, Friday 11:00 AM - 10:30 PM, Saturday 1:00 PM - 10:30PM, Sunday 1:00 PM - 10:30 PM',
        FALSE,
        'http://places.singleplatform.com/1911-smoke-house-barbeque/menu?ref=google',
        'https://1911bbq.com',
        'BBQ',
        12,
        5.0,
        'BBQ, Grill, American',
        'Fast Food',
        'Moderate $$', 'https://hiddentrenton.com/wp-content/uploads/2015/10/smoked-salmon-on-salad.jpg' );
        """,

        """
        INSERT INTO restaurants ( name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Bamboo Grill Jamaican Restaurant',
        '1005 Chambers St, Trenton, NJ 08611',
        'Monday 10:00 AM - 7:00 PM, Tuesday 10:00 AM - 7:00 PM, Wednesday 10:00 AM - 7:00 PM, Thursday 10:00 AM - 7:00 PM, Friday 10:00 AM - 8:00 PM, Saturday 10:00 AM - 8:00 PM, Sunday Closed',
        TRUE,
        'None',
        'None',
        'Jamaican, Grill',
        1,
        3.2,
        'BBQ, Grill, Jamaican',
        'Fast Food',
        'Moderate $$',
        'https://cdn.usarestaurants.info/assets/uploads/5d0e3573a5822a6c84c9c4c5645632e0_-united-states-new-jersey-mercer-county-trenton-bamboo-grill-jamaican-restaurant-mini-mart-542551htm.jpg');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Ila Mae''s Restaurant',
        '313 Market St, Trenton, NJ 08611',
        'Monday Closed, Tuesday 9:00 AM - 8:00 PM, Wednesday 9:00 AM - 8:00 PM, Thursday 9:00 AM - 8:00 PM, Friday 9:00 AM - 8:00 PM, Saturday 9:00 AM - 8:00 PM, Sunday Closed', FALSE,
        'http://places.singleplatform.com/ila-maes-restaurant/menu?ref=google',
        'None',
        'Soul',
        10,
        4.3,
        'Soul',
        'Casual',
        'Moderate $$',
        'https://b.zmtcdn.com/data/reviews_photos/ae0/5e409171385c4b3f360eb7fe0ad87ae0_1449862294.jpg?fit=around|771.75:416.25&amp;crop=771.75:416.25;*,*');
        """,

        """
        INSERT INTO restaurants ( name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Blue Danube Restaurant',
        '538 Adeline St, Trenton, NJ 08611',
        'Monday Closed, Tuesday 11:30 AM - 7:30 PM, Wednesday 11:30 AM - 7:30 PM, Thursday 11:30 AM - 7:30 PM, Friday 11:30 AM - 8:00 PM, Saturday 3:00 - 8:00 PM, Sunday 3:00 PM - 7:30 PM',
        TRUE,
        'http://www.bluedanuberestaurant.net/menu.php',
        'http://www.bluedanuberestaurant.net/about.php',
        'Eastern European' ,
        273,
        4.6,
        'Eastern European',
        'Casual',
        'Moderate $$',
        'https://vrconcierge.com/wp-content/uploads/2021/07/blue-danube-restaurant-trenton-nj-exterior-1.jpg' );
        """,

        """
        INSERT INTO restaurants ( name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'The Big Easy of Trenton Restaurant',
        '111 S Warren St, Trenton, NJ 08608',
        'Monday 12:00 PM - 7:00 PM, Tuesday 12:00 PM - 7:00 PM, Wednesday 12:00 PM - 7:00 PM, Thursday 12:00 PM - 7:00 PM, Friday 12:00 PM - 7:00 PM, Saturday 9:00 AM - 5:00 PM, Sunday Closed', FALSE,
        'None',
        'None',
        'Dine-in' ,
        260,
        4.5,
        'Dine-in, Soul',
        'Casual',
        'Moderate $$',
        'https://hiddentrenton.com/wp-content/uploads/2018/05/the-buffet.jpg');
        """,

        """
        INSERT INTO restaurants ( name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Don Julio''s Bar and Grill',
        '900 Liberty St, Trenton, NJ 08611',
        'Monday 11:00 AM - 2:00 AM, Tuesday 11:00 AM - 2:00 AM, Wednesday 11:00 AM - 2:00 AM, Thursday 11:00 AM - 2:00 AM, Friday 11:00 AM - 2:00 AM, Saturday 11:00 AM - 2:00 AM, Sunday 12:00 PM - 2:00 AM',
        TRUE,
        'None',
        'None',
        'Bar & Grill' ,
        190,
        4.3,
        'Bar & Grill',
        'Casual',
        'Moderate $$',
        'https://resizer.otstatic.com/v2/photos/wide-huge/1/41970639.png'
        );
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'The Hummingbird Restaurant',
        '29 S Warren St, Trenton, NJ 08608',
        'Monday 10:00 AM - 7:00 PM, Tuesday 10:00 AM - 7:00 PM, Wednesday 10:00 AM - 7:00 PM, Thursday 10:00 AM - 7:00 PM, Friday 10:00 AM - 6:00 PM, Saturday 10:00 AM - 6:00 PM, Sunday Closed',
        FALSE,
        'None',
        'None',
        'Jamaican' ,
        282,
        4.2,
        'Jamaican',
        'Casual',
        'Moderate $$',
        'https://hiddentrenton.com/wp-content/uploads/2010/03/hummingbird1.jpg');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Sabor Latino',
        '293 Ashmore Ave, Trenton, NJ 08611',
        'Monday 10:00 AM - 12:00 AM, Tuesday 10:00 AM - 12:00 AM, Wednesday Closed, Thursday 10:00 AM - 12:00 AM, Friday 10:00 AM - 2:00 AM, Saturday 10:00 AM - 2:00 AM, Sunday 10:00 AM - 12:00 AM',
        TRUE,
        'None',
        'None',
        'Dominican' ,
        80,
        4.1,
        'Dominican, Mexican',
        'Casual',
        'Moderate $$',
        'https://www.trentondaily.com/wp-content/uploads/2019/07/sabor.png');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Trentini''s',
        '635 S Clinton Ave, Trenton, NJ 08611',
        'Monday 10:00 AM - 10:00 PM, Tuesday 10:00 AM - 10:00 PM, Wednesday 10:00 AM - 10:00 PM, Thursday 10:00 AM - 10:00 PM, Friday 10:00 AM - 10:00 PM, Saturday 10:00 AM - 10:00 PM, Sunday 10:00 AM - 10:00 PM',
        FALSE,
        'https://trentinismenu.com/menu.html',
        'https://trentinismenu.com/index.html',
        'Italian' ,
        420,
        4.1,
        'Italian, Mediterranean, Spanish',
        'Casual',
        'Inexpensive $',
        'https://trentinismenu.com/assets/img/logo.png');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Mama D Soul Food 2',
        '312 S Broad St, Trenton, NJ 08609',
        'Monday Closed, Tuesday Closed, Wednesday 12:00 PM - 7:00 PM, Thursday 12:00 PM - 7:00 PM, Friday 12:00 PM - 7:00 PM, Saturday 9:00 AM - 7:00 PM, Sunday 1:00 PM - 7:00 PM',
         TRUE,
        'None',
        'None',
        'Soul' ,
        112,
        3.9,
        'Soul',
        'Fast Food',
        'Inexpensive $',
        'https://blackenlightenmentapp.com/wp-content/uploads/2018/09/mamad-e1576679700857.jpg');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Cooper''s Riverview',
        '50 Riverview Plaza, Trenton, NJ 08611',
        'Monday Closed, Tuesday 12:00 PM - 2:00 AM, Wednesday 12:00 PM - 2:00 AM, Thursday 12:00 PM - 2:00 AM, Friday 12:00 PM - 2:00 AM, Saturday 12:00 PM - 2:00 AM, Sunday 11:30 AM - 11:00 PM',
        FALSE,
        'coopersnj.com',
        'None',
        'English' ,
        455,
        4.0,
        'English',
        'Fine Dining',
        'Pricey $$$',
        'https://www.nj.com/resizer/6CK6XH7YNlcxanJteQtof44WHtc=/800x0/smart/arc-anglerfish-arc2-prod-advancelocal.s3.amazonaws.com/public/6RLSBPHNOJCB7KK2NOXOGRFYXE.jpg');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Mi Ranchito Pizza and Tacos',
        '911 Chambers St, Trenton, NJ 08611',
        'Monday 10:00 AM - 10:00 PM, Tuesday 10:00 AM - 10:00 PM, Wednesday Closed, Thursday 10:00 AM - 10:00 PM, Friday 10:00 AM - 10:00 PM, Saturday 10:00 AM - 10:00 PM, Sunday 10:00 AM - 10:00 PM',
        TRUE,
        'None',
        'None',
        'Tacos' ,
        61,
        4.7,
        'Mexican, Tacos',
        'Casual',
        'Inexpensive $',
        'https://cdn.usarestaurants.info/assets/uploads/7a258e9a8dabd09a7e415256cd08757d_-united-states-new-jersey-mercer-county-trenton-mi-ranchito-pizza-and-tacos-609-498-0174htm.jpg');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'El Potrillo',
        '541 Roebling Ave, Trenton, NJ 08611',
        'Monday 10:00 AM - 10:00 PM, Tuesday Closed, Wednesday 10:00 AM - 10:00 PM, Thursday 10:00 AM - 10:00 PM, Friday 10:00 AM - 10:00 PM, Saturday 10:00 AM - 10:00 PM, Sunday 10:00 AM - 10:00 PM',
        FALSE,
        'http://places.singleplatform.com/el-potrillo-mexican-restaurant-7/menu?ref=google',
        'None',
        'Mexican' ,
        213,
        3.9,
        'Mexican',
        'Casual',
        'Moderate $$',
        'https://hiddentrenton.com/wp-content/uploads/2015/03/El_Potrillo.jpg');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Chencha y Chole',
        '865 S Broad St, Trenton, NJ 08611',
        'Monday 11:00 AM - 10:00 PM, Tuesday 11:00 AM - 10:00 PM, Wednesday 11:00 AM - 10:00 PM, Thursday 11:00 AM - 10:00 PM, Friday 11:00 AM - 10:00 PM, Saturday 11:00 AM - 10:00 PM, Sunday 11:00 AM - 10:00 PM',
         TRUE,
        'None',
        'None',
        'Mexican' ,
        319,
        4.2,
        'Mexican',
        'Casual',
        'Inexpensive $',
        'https://media-cdn.grubhub.com/image/upload/d_search:browse-images:default.jpg/w_1200,h_800,f_auto,fl_lossy,q_80,c_fit/xgqbyondwd2syksoznsj');
        """,

        """
        INSERT INTO restaurants (name, address, hours,
        open_closed, menu, media, tags, review_count, stars,
        cuisine, type, price, image)
        VALUES (
        'Casablanca Restaurant',
        '140 Washington St, Trenton, NJ 08611',
        'Monday 11:00 AM - 2:00 AM, Tuesday 11:00 AM - 2:00 AM, Wednesday 11:00 AM - 2:00 AM, Thursday 11:00 AM - 2:00 AM, Friday 11:00 AM - 2:00 AM, Saturday 11:00 AM - 2:00 AM, Sunday 11:00 AM - 2:00 AM',
        FALSE,
        'None',
        'None',
        'Spanish' ,
        372,
        4.1,
        'Spanish',
        'Casual',
        'Moderate $$',
        'https://hiddentrenton.com/wp-content/uploads/2017/12/Exterior.jpg');
        """,
        """
        INSERT INTO administrators (email)
        VALUES (
        'sd20@princeton.edu');
        """,
        """
        INSERT INTO administrators (email)
        VALUES (
        'pjozuah@princeton.edu');
        """,
        """
        INSERT INTO administrators (email)
        VALUES (
        'soumyag@princeton.edu');
        """,
        """
        INSERT INTO administrators (email)
        VALUES (
        'chukwuma@princeton.edu');
        """,
        """
        INSERT INTO administrators (email)
        VALUES (
        'anatk@princeton.edu');
        """,
        """
        INSERT INTO administrators (email)
        VALUES (
        'kao3@princeton.edu');
        """]
    try:
        with connect(
                host='localhost', port=5432, user='rmd', password='trentoneats333',
                database='trentoneats') as connection:
            # with connect(host='ec2-3-229-161-70.compute-1.amazonaws.com', port=5432, user='jazlvqafdamomp', password='6bc2f9e25e0ab4a2e167d5aed92096137eaacd1667e2863a6659e019dbb7e81a',
            #              database="dequ5ope4nuoit") as connection:

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
