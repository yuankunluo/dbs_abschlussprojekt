# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:24:44 2014

@author: yuankunluo
"""

import sqlite3

def openConnect():
    """Get the cousor object for a sqlite3 db
    
    :returns: a cousor object or None if connection 
    """
    try:
        conn = sqlite3.connect("db/london2012.db")
        # use row factory
        conn.row_factory = sqlite3.Row
        return conn
    except:
        print("Database connect failure.")
        return None

def closeConnct(coon):
    """Close the db connection
    
    :param conn: A sqlite3 connection object
    :type conn: A sqlite3.Connection Instance
    :return: None
    """
    coon.close()
    
    