#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from tokenize import Floatnumber
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#Core QUestions:
# 1) Boolean + float types? Timestamp types 
# 2) relationships and references

Base = declarative_base()

class restaurants (Base):
    __tablename__ = 'restaurants'
    restaurant_id = Column(String(20), primary_key=True)
    address = Column(String(225))
    hours = Column(String(225))
    open_closed = Column(Boolean)
    menu = Column(String(225))
    media = Column(String(225))
    tags = Column(String(225))
    review_count = Column(Integer)
    stars = Column(Float)

class customers (Base): 
    __tablename__ = 'customers'
    customer_id = Column(String(20), primary_key=True)
    name = Column(String(225))
    review_count = Column(Integer)
    avg_rating = Column(Float)
    account_type = Column(String(225))
    reported_count = Column(Integer)

class reviews (Base): 
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    # customer_id VARCHAR(20), FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    # restaurant_id VARCHAR(20), FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id),
    # date TIMESTAMP NOT NULL,
    # text TEXT NOT NULL,
    price = Column(Integer) 
    taste = Column(Integer)
    authenticity = Column(Integer)
    coolness = Column(Integer)
    overall = Column(Integer)

class categories (Base): 
    __tablename__ = 'categories'
    restaurant_id = Column(String(20), primary_key=True)
    fast_food = Column(Boolean)
    casual_dining = Column(Boolean) 
    inexpensive = Column(Boolean)
    moderate_price = Column(Boolean)
    pricey = Column(Boolean)
    priciest = Column(Boolean)
    american = Column(Boolean)
    french = Column(Boolean)
    indian = Column(Boolean)
    # FOREIGN KEY (restaurant_id)
    #  REFERENCES restaurants (restaurant_id)

class reviews (Base): 
    __tablename__ = 'reviews'
    review_id = Column(Integer, primary_key=True)
    # customer_id VARCHAR(20), FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    # restaurant_id VARCHAR(20), FOREIGN KEY (restaurant_id) REFERENCES restaurants (restaurant_id),
    # date TIMESTAMP NOT NULL,
    # text TEXT NOT NULL,
    price = Column(Integer)
    taste = Column(Integer)
    authenticity = Column(Integer)
    coolness = Column(Integer)
    overall = Column(Integer) 

class usertype (Base): 
    __tablename__ = 'usertype'
    user_id = Column(String(20), primary_key=True)
    customer_id = Column(String(20))
    # FOREIGN KEY (customer_id) 
    # REFERENCES customers (customer_id),
    # restaurant_id VARCHAR(20),
    # FOREIGN KEY (restaurant_id)
    # REFERENCES restaurants (restaurant_id),
    admin = Column(Boolean)
    restaurant = Column(Boolean)
    customer = Column(Boolean) 
   