# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 04:39:22 2014

@author: yuankunluo
"""
import sqlite3

def get_conn():
    """Return the connection object
    """
    conn = sqlite3.connect("db/london2012.db")
    conn.row_factory = sqlite3.Row
    return conn
def get_cousor(conn):
    """Return the cousor object
    """
    # use row factory   
    cousor = conn.cursor()
    return cousor