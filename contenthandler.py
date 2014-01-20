# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:29 2014

@author: yuankunluo
"""
import dbconnector as db
import sql

def getHomepage():
    """Get the content for homepage.
    
    – Anzeigen der letzten drei stattgefundenen Wettk ̈ampfe.
    – Anzeigen aller Wettkampfberichte einer Disziplin.
    – Anzeigen von Wettk ̈ampfen, 
    bei denen von bestimmten Nationen Medaillen erzielt wurden.
    
    :returns: rederned String
    """
    conn = db.openConnect()
    cousor = conn.cursor()
    lastEvents = cousor.execute(sql.lastthreeevents).fetchall()
    lastEvents = tupleToList(lastEvents)
    db.closeConnct(conn)
    return lastEvents

#==============================================================================
# helper function
#==============================================================================
def tupleToList(sqlTuple):
    """Convert a sql executed result into a list of tuple,
    the first element is the key, the other element is the tuple.
    
    :param sqlTuple: A fetch result
    :type sqlTupee: A list of sqlite3.Row
    :returns: A list of tuple like [(v1,v2,v3..)]
    """
    result = []
    ks = tuple(sqlTuple[0].keys())
    result.append(ks)
    for r in sqlTuple:
        tem = []
        for k in ks:
            tem.append(r[k])
        result.append(tuple(tem))
    return result
        
    
    
    
    
    
