#!/usr/bin/env python
"""This is reg.py"""
#-----------------------------------------------------------------------
# reg.py
# Author: Stephen Dong, Naomi Farkas
#-----------------------------------------------------------------------
from sys import argv, stderr
from contextlib import closing
from sqlite3 import DatabaseError, connect
from psycopg2 import connect
import argparse
import sys
import textwrap
#-----------------------------------------------------------------------

#DATABASE_URL = 'file:reg.sqlite?mode=ro'
#DATABASE_URL = 'file:teldatabase.sql?mode=ro'

def __display__():
    try:
        with connect(host='localhost', port=5432, user='rmd', password='xxx',
        database="trentoneats") as connection:

            with connection.cursor() as cursor:
                stmt_str = "SELECT restaurant_id, name "
                stmt_str += "FROM restaurants"
                cursor.execute(stmt_str)

                row = cursor.fetchone()
                print(row)

                while row is not None:
                    print(row)
                    row = cursor.fetchone()

    except DatabaseError as error:
        print(sys.argv[0] + ": " + str(error), file=stderr)
        sys.exit(1)




def main():
    """The main function"""
    __display__()


    #if len(argv) == 3:
     #   _search__(argv[1], argv[2])



#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
