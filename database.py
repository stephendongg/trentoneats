#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Books (Base):
    __tablename__ = 'books'
    isbn = Column(String, primary_key=True)
    title = Column(String)
    quantity = Column(Integer)

class Authors (Base):
    __tablename__ = 'authors'
    isbn = Column(String, primary_key=True)
    author = Column(String, primary_key=True)

class Orders (Base):
    __tablename__ = 'orders'
    isbn = Column(String, primary_key=True)
    custid = Column(String, primary_key=True)
    quantity = Column(Integer)

class Customers (Base):
    __tablename__ = 'customers'
    custid = Column(String, primary_key=True)
    custname = Column(String)
    street = Column(String)
    zipcode = Column(String)

class Zipcodes (Base):
    __tablename__ = 'zipcodes'
    zipcode = Column(String, primary_key=True)
    city = Column(String)
    state = Column(String)
