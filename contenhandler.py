# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:29 2014

@author: yuankunluo
"""
import dbconnector as db

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
    news = cousor.excute("select * from news")
    
    
    
