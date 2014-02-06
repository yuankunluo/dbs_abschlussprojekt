# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:24:44 2014

@author: yuankunluo
"""

import sqlite3
import sqlstaments as sqls
import os


def fetch_tuple(query, condition = None, withLink = False):
    """Get the cousor object for a sqlite3 db
    
    :param query: A sql stament
    :type query: String
    :param condition: A condition for select query
    :param withLink: Return a tuple with links
    :tyoe withLink: Boolean
    :returns: a cousor object or None if connection 
    """
    conn = get_conn()
    # use row factory
    conn.row_factory = sqlite3.Row
    cousor = conn.cursor()
    if condition:
        result = cousor.execute(query,condition).fetchall()
        return tupleToList(result,withLink)
    else:
        result = cousor.execute(query).fetchall()
        conn.close()
        return tupleToList(result, withLink)

#==============================================================================
# get conn or get cousor
#==============================================================================
def get_conn(dbs="db/london2012.db"):
    """Return the connection object
    """
    conn = sqlite3.connect(dbs)
    conn.row_factory = sqlite3.Row
    return conn
def get_cousor(conn):
    """Return the cousor object
    """
    # use row factory   
    cousor = conn.cursor()
    return cousor
#==============================================================================
# select primary key of a table
#==============================================================================
def select_something(table, something, condition):
    """Test if a given tuple already in a given table
    
    :param sqlquery: A table name
    :type sqlquery: string
    :param something: a tuple of column
    :type something: a tuple
    :param condition: a dict
    :type conditon: a dist
    :returns: A primary key
    """
    conn = get_conn()
    cousor = get_cousor(conn)
    if len(something) >1:
        items = ",".join(something)
    else:
        items = "".join(something)
    sqlq = "select {items} from {table} where".format(items = items,
                                                table= table)
    keys = condition.keys()
    for i in range(len(keys)):
        k = keys[i]
        if i == 0:
            sqlq += " "+k + "=:" + k + " "
        if i in range(1, len(keys)):
            sqlq += " and "+k + "=:" + k + " "
#    print(condition)
#    print(sqlq)
    r = cousor.execute(sqlq, condition)
    r = r.fetchall()
    conn.close()
    # return item
    result = tupleToList(r)
    #print(result)
    return result
#==============================================================================
# insert
#==============================================================================
def insert_into_tables(table, condition, re_item):
    """Insert into 
    
    :param sqlquery: A table name
    :type sqlquery: string
    :param condition: a dict
    :type conditon: a dist
    :param re_item: A specfiy returned item after inserting
    :param re_item: A tuple
    :returns: A primary key
    """
    test = select_something(table, re_item, condition)
    if len(test) > 1:
        return test
    conn = get_conn()
    cousor = get_cousor(conn)
    insertsql = """insert into {t}({c}) values ({q})"""
    columns = []
    values = []
    for k,v in condition.items():
        columns.append(k)
        values.append(v)
    questions = "? "*len(values)
    questions = questions.strip(" ")
    questions = questions.split(" ")
    questions = ",".join(questions)
    insertsql = insertsql.format(t = table, c = ",".join(columns),
                                 q = questions)
    cousor.execute(insertsql,values)
    conn.commit()
    conn.close()
    result = select_something(table, re_item, condition)
    return result
    
    


#==============================================================================
# helper function
#==============================================================================
def tupleToList(sqlTuple, withLink= False):
    """Convert a sql executed result into a list of tuple,
    the first element is the key, the other element is the tuple.
    
    ..note::
    How to use, 
    select a, a_link from x,
    this result a list of tuple, first element of this list is a header.
    
    
    :param sqlTuple: A fetch result
    :type sqlTupee: A list of sqlite3.Row
    :param withLink: if return with link
    :type withLink: Boolean
    :returns: A list of tuple like [(v1,v2,v3..)]
    """
    # if no fetched
    if len(sqlTuple) == 0:
        return []
    # if not link attached
    if not withLink:
        result = []
        ks = sqlTuple[0].keys()
        result.append(ks)
        for r in sqlTuple:
            tem = []
            for k in ks:
                tem.append(r[k])
            result.append(tem)
        return result
    if withLink:
        result = []
        r = tupleToList(sqlTuple)
        linkindex = []
        for i in range(len(r[0])):
            if r[0][i].endswith("_link"):
                l = r[0][i].split("_")
                linkindex.append((i-1,l[0])) 
        index = [x[0] for x in linkindex]
        for row in r:
            tem = []
            i = 0
            j = 0
            while i < len(row):
                if i in index:
                    tem.append((row[i],linkindex[j][1],row[i+1]))
                    i += 2
                    j +=1
                else:
                    tem.append(row[i])
                    i += 1
            result.append(tem)
        return result