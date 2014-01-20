# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:24:44 2014

@author: yuankunluo
"""

import sqlite3

def execute(query, withLink = False):
    """Get the cousor object for a sqlite3 db
    
    :param query: A sql stament
    :type query: String
    :param withLink: Return a tuple with links
    :tyoe withLink: Boolean
    :returns: a cousor object or None if connection 
    """
#    try:
    conn = sqlite3.connect("db/london2012.db")
    # use row factory
    conn.row_factory = sqlite3.Row
    cousor = conn.cursor()
    result = cousor.execute(query).fetchall()
    conn.close()
    return tupleToList(result, withLink)
#    except:
#        print("Database connect failure.")
#        return None

#==============================================================================
# helper function
#==============================================================================
def tupleToList(sqlTuple, withLink= False):
    """Convert a sql executed result into a list of tuple,
    the first element is the key, the other element is the tuple.
    
    :param sqlTuple: A fetch result
    :type sqlTupee: A list of sqlite3.Row
    :param withLink: if return with link
    :type withLink: Boolean
    :returns: A list of tuple like [(v1,v2,v3..)]
    """
    if not withLink:
        result = []
        ks = tuple(sqlTuple[0].keys())
        result.append(ks)
        for r in sqlTuple:
            tem = []
            for k in ks:
                tem.append(r[k])
            result.append(tuple(tem))
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
            result.append(tuple(tem))
        return result