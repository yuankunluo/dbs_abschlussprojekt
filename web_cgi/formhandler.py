# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:35:43 2014

@author: yuankunluo
"""

import dbconnector as db
from bottle import redirect,response,request
import re
from bottle import template
import datetime
import os
#==============================================================================
# add solo event
#==============================================================================
def do_add_solo_event(req):
    """"Do sql insert based on the html form
    
    :prame req: The request object
    :tyeoe req: bottle.request
    :returns: none
    """
    check_login(True)
    if not check_reporter():
        return template("error",error= "You have no right to do this")
    uid = int(req.get_cookie("uid"))
    form = req.forms
    form = request_to_dict(form)
    ts = {"p":"Preliminaries","s":"Semifinal","f":"Finals"}
    # collect event infomation
    event = form.pop("event")
    event["user"] = uid
    e_type = event.pop("type")
    event["type"] =  "Solo "+ ts[e_type]
    test = db.select_something("events",("id","name"),{"name":event["name"], "type":event["type"]},onlyone=True)
    if test != None:
        oe_id = test[0]
        oe_name = test[1]
        return error_duplicate(oe_name, "events", oe_id)
    ath_keys = [ath for ath in form.keys() if ath.startswith("ath")]
    p_infos = {}
    ath_rowids = []
    for ak in ath_keys:
        a_info = form[ak]
        a_condition = {"firstname":a_info["firstname"],
        "lastname":a_info["lastname"],
        "gender":a_info["gender"],
        "country":a_info["country"],
        "birthday":a_info["date"],}
        ath_rowid = db.insert_into_tables("athletes",a_condition, ("id",))
        ath_rowid = ath_rowid[0]
        ath_rowids.append(ath_rowid)
        t_name = a_info["country"] + "-"+ event["name"] + "-" + event["type"]
        p_condition = {"athlete":ath_rowid,"rank":a_info["rank"],"team":t_name,
                       "result":a_info["result"],"medal":a_info["medal"]}
        p_infos[ath_rowid] = p_condition
    ath_rowids_rm = remove_duplicates(ath_rowids)
    # test if duplicated athe in one event
    if len(ath_rowids) != len(ath_rowids_rm):
        e = "You have inputed duplicated althetes in one event!"
        return template("error",error = e)
    e_id =  db.insert_into_tables("events",event,("id",))[0]
    for k,v in p_infos.items():
        v["event"] = e_id
        db.insert_into_tables("participants",v,("rowid",))
    redirect("/events/"+str(e_id))
#==============================================================================
# add team event
#==============================================================================
def do_add_team_event(req):
    """Process the form for adding team event
    
    :param req: a html post request
    :type req: a bottle.request
    :returns: none
    """
    check_login(True)
    if not check_reporter():
        return template("error",error= "You have no right to do this")
    uid = int(req.get_cookie("uid"))
    # clean form request
    form = request_to_dict(req.forms)
    event = form.pop("event")
    event["user"] = uid
    ts = {"p":"Preliminaries","s":"Semifinal","f":"Finals"}
    # test if this event in db
    e_type = event.pop("type")
    event["type"] = "Team "+ ts[e_type]
    e_test = db.select_something("events",("id","name",),
                                 {"name":event["name"]}, onlyone=True)
    if e_test != None :
        e_name = e_test[1]
        e_id = e_test[0]
        return error_duplicate(e_name, "events",e_id)
    # add athletes
    teams = extract_from_interdict(form)
    # store ath_rowids 
    a_ids = []
    p_cons = []
    for team,aths in teams.items():
        country = aths.pop("country")
        t_name = country + "-" + event["name"] + "-" +event["type"]
        medal = aths.pop("medal")
        result = aths.pop("result")
        rank = aths.pop("rank")
        for k,ath in aths.items():
            # the year,month, day was not proceed by manage_tuple()            year = ath.pop("year")
            day = ath.pop("day")
            month = ath.pop("month")
            year = ath.pop("year")
            birthday = "-".join([year,month,day])
            ath["birthday"] = birthday
            ath["country"] = country
            # insert into athletes
            a_id = db.insert_into_tables("athletes",ath,("id",))[0]
            a_ids.append(a_id)
            p_con = {"athlete":a_id,"team":t_name,"result":result,
                     "rank":rank,"medal":medal}
            p_cons.append(p_con)
    # check if there are duplikates in one team
    a_ids = remove_duplicates(a_ids)
    if len(p_cons) != len(a_ids):
        e = "You have inputed duplicated althetes in one event!"
        return template("error",error = e)
    # add event
    e_id = db.insert_into_tables("events", event,("id",))[0]
    for p in p_cons:
        p["event"] = e_id
        db.insert_into_tables("participants",p,())
    redirect("/events/"+str(e_id))

#==============================================================================
# add news
#==============================================================================
def do_add_news(req):
    """Insert news into dbs.
    
    :param req: A request object
    :type req: bottle.baserequest
    :param uid: A user id in cookies
    :type req: string
    :returns: none
    """
    check_login(True)
    # clean form request
    form = request_to_dict(req.forms)
    news = form.pop("news")
    # test if duplikated
    test = db.select_something("news",("name","id",),{"name":news["name"],
                               "event":news["event"]
                               }, onlyone=True)
    if test != None :
        nid = test[1]
        nname = test[0]
        return error_duplicate(nname, "news", nid)
    news["datetime"] = get_now()
    n_id = db.insert_into_tables("news",news, ("id",))[0]
    redirect("/news/"+str(n_id))

def do_add_comment(nid):
    check_login(True)
    uid = int(request.get_cookie("uid"))
    co = request.forms["comment"]
    comment =  {"news":nid, "content":co, 
                 "user":uid, "datetime":get_now()}
    db.insert_into_tables("comments",comment)
    redirect("/news/"+str(nid))

#==============================================================================
# do upload pic
#==============================================================================
def do_upload_pic(req):
    """Insert news into dbs.
    
    :param req: A request object
    :type req: bottle.baserequest
    :param uid: A user id in cookies
    :type req: string
    :returns: pic id in dbs
    """
    check_login(True)
    uid = int(req.get_cookie("uid"))
    upload = req.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed. Pleas use .jpg, .png or .jepg'
    form = req.forms
    des = form.get("picture_des")
    # save pic in static/images/
    pn = save_pic(upload,ext,uid)
    # insert this pic into dbs
    pid = db.insert_into_tables("pictures",{"link":pn,"des":des},("id",))[0]
    return pid
    
def do_add_pic(t,iid, req):
    """Add pic to a given table.
    
    :parma t: The table name.
    :type t: string
    :param iid: the id of one item in table
    :param iid: integer
    :param req: the request
    :type req: bottle.baserequest
    """
    # first insert thi pic into dbs
    check_login(True)
    pid = do_upload_pic(req)
    uid = int(req.get_cookie("uid"))
    if t == "newspics":
        db.insert_into_tables(t,{"news":iid,"pic":pid,"user":uid},("id",))
        redirect("/news/"+str(iid))
    if t == "athletes":
        db.update_table(t,{"pic":pid},{"id":iid},("id",))
        redirect("/athletes/" + str(iid))
    if t == "athletespics":
        db.update_table(t,{"pic":pid},{"id":iid},("id",))
        redirect("/athletes/" + str(iid))
    if t == "users":
        db.update_table(t,{"pic":pid},{"id":iid},("id",))
        redirect("/users/" +  str(iid))
    
#==============================================================================
# sigup and login
#==============================================================================
def do_singup(req):
    """Insert user into dbs.
    
    :param req: A request object
    :type req: bottle.baserequest
    :returns: none
    """
    form = request_to_dict(req.forms)
    user = form.pop("user")
    u_name = user["name"]
    name_test = re.findall(r"\w",u_name)
    name_test = "".join(name_test)
    if name_test != u_name:
        return template("error",error="Username was not allowed. Username can contain only letter and number.")
    date = user.pop("date")
    user["birthday"] = date
    ps1 = user.pop("password1")
    ps2 = user.pop("password2")
    user["registertime"] = get_now()
    if ps1 != ps2:
        return template("error",error="Passowrd must be the same!")
    user["password"]  = ps1
    # test if this user existed in db
    u_test = db.select_something("users",("id",),
                                 {"name":user["name"]},onlyone=True)
    if u_test != None:
        return template("error",error=user["name"] + " was existed. Please use a new one!")
    else:
        u_id = db.insert_into_tables("users",user,("id",))[0]
        response.set_cookie("uid",str(u_id))
        redirect("/admin")

def do_login(req):
    """Process login 
    
    :param req: A request object
    :type req: bottle.baserequest
    :returns: none
    """
    form = request_to_dict(req.forms)
    user = form.pop("user")
    # test username
    o_user = db.select_something("users",("id",),{"name":user["name"]},onlyone=True)
    if o_user == None:
        return template("error",error="User name does not exist in db.")
    user = db.select_something("users",("id",),user,False,onlyone=True)
    if user == None:
        return template("error",error="Username or Password doesnot match! Try again.")
    else:
        response.set_cookie("uid", str(user[0]))
        redirect("/admin")

#==============================================================================
# user update and delete
#==============================================================================
def do_user_update(req, uid):
    """Update user 
    
    """
    c_uid = int(req.get_cookie("uid"))
    form = request_to_dict(req.forms)
    user = form.pop("user")
    uid = int(user.pop("id"))
    if c_uid != uid:
        redirect("/login")
    if uid in [1,2]:
        return template("error", error = "test and admin account can not be updated! FUU")
    p1 = user.pop('password1')
    p2 = user.pop("password2")
    date = user.pop("date")
    user["birthday"] = date
    if p1 != p2:
        return template("error",error="Password must be the same!")
    if len(p1) < 3 or len(p2) < 3:
        return template("error",error="Password must have at least 3 characters!")
    user["password"] = p1
    db.update_table("users",user,{"id":uid},("id",))
    redirect("/users/"+str(uid))
    
def do_delete_user(req,uid):
    check_login(True)
    p2 = req.forms.get("p2")
    p1 = req.forms.get("p1")
    if p2 != p1:
        return template("error", error = "Two passwords must be the same.")
    c_uid = int(req.get_cookie("uid"))
    if c_uid != uid:
        return template("error", error = "your can not delete other's account")
    if uid == 1 or uid ==2:
        return template("error", error = "test and admin account can not be deleted! FUU")
    p = db.select_something("users",("password",),{"id":uid},onlyone=True)[0]
    if p != p2 or p1 != p1:
        return template("error", error = "Password and Username not match!")
    # delete from tables
    du = db.delete_table("users",{"id":uid})
    dn = db.delete_table("news",{"user":uid})
    dm = db.delete_table("comments",{"user":uid})
    de = db.delete_table("events",{"user":uid})
    dp = db.delete_table("newspics",{"user":uid})
    for r in [du,dn,dm,de,dp]:
        if r != True:
            error = """
            <p class="tipp">Boah! DBS Fuck! Error! Try later!! Later! ter! er! r!</p>
            """
            return template("error", error = error)
    else:
        redirect("/logout")
        
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# # # # # # dont look down
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
#==============================================================================
# help functions
#==============================================================================
def request_to_dict(reqForms):
    """Helper: transform a bottle.request.form into dict
    
    :param reqForms: a bottle.request.form
    :type reqForms: form object
    :returns: a dict of {"tuplehead":{"column":"value"}}
    """
    infos = []
    for k,v in reqForms.items():
        k = k.split("_")
        k.append(v)
        k = cleanRequest(k)
        k = [unicode(x,encoding="utf-8") for x in k]
        infos.append(tuple(k))
    infos = manage_tuples(infos)
    return infos
    
def manage_tuples(tuples):
    """Helper: make the request tuples into wellformated tuple,
    inorder to match tablls in dbs
    
    :param tuples: a list of tuples
    :type tuples: a list
    :returns: a list of tuples that match tables in dbs
    """
    tables = {}
    for t in tuples:
        s = t[2]
        if t[1] in ["month","year","day","hour","minute"] and len(s) ==1:
            s = "0" + s
        if t[0] not in tables.keys():
            tables[t[0]] = {}
            tables[t[0]][t[1]]=s
        else:
            tables[t[0]][t[1]]=s
    # make date
    for k in tables.keys():
        t = tables[k]
        if "year" in t.keys():
            year = t["year"]
            month = t["month"]
            day = t["day"]
            date = "-".join([year,month,day])
            t.pop("year")
            t.pop("month")
            t.pop("day")
            t["date"] = date
        if "minute" in t.keys():
            hour = t["hour"]
            minute = t["minute"]
            time = ":".join([hour,minute])
            t.pop("hour")
            t.pop("minute")
            t["time"] = time
    return tables

def cleanRequest(sqltupe):
    """Helper: clean sql
    
    :param sqltupe: A quests data extracted
    :type sqltupe: A list
    :returns: A list
    """
    result = []
    for i in sqltupe:
        i = i.lower()
        i  = re.sub(r"select.*from|insert into|update .* wherer|delete .* from","",i)
        i = i.strip(" ")
        result.append(i)
    return result
    
def remove_duplicates(l):
    """Remove duplicate element in a list
    
    :param l: A list object
    :type l: List
    :returns: a list without duplicate
    """
    return list(set(l))

def extract_from_interdict(interdict, delimeter="/"):
    """Extract ath for every team. It can handel inter delimeter "/".
    The add team event form results a dict like:
    {"t1":{"a1/firstname":"love", "a2/gender":"f"}}.
    This helper make the inter infomations into a inter dict:
    Result:
    {"t1":{"r":"100", "medal":"g","a1":{"firstname":"love"},"a2":{"gender":"f"}}}
    
    :param teams: A dict of teams like {teams:{athx/xx:xxx, athx/xx:xxx}
    :type teams: A dict
    :returns: A dict 
    """
    result = {}
    for k,v in interdict.items():
        result[k] = {}
        for ik, iv in v.items():
            # split ik,iv into one list [k, k2, v]
            ks = ik.split(delimeter)
            ks.append(iv)
            temp = ks
            if len(temp) == 2:
                result[k][temp[0]] = temp[1]
                continue
            if temp[0] in result[k].keys() and len(temp)>2:
                result[k][temp[0]][temp[1]] =  temp[2]
            else:
                result[k][temp[0]] = {}
                result[k][temp[0]][temp[1]] = temp[2]
    return result

def error_duplicate(itemname, link, itemid, edit=False):
    """Return a error page for duplicate event 
    
    :param itemname: a name for given item
    :type itemname: a string
    :param link: a link goal to the duplicate 
    :type link: string
    :param itemid: the id for link
    :type itemid: integer
    :returns: String
    """
    e = """
    <p><a href="/{link}/{itemid}">{itemname}</a> was already reported!</p>
    """
    if edit:
        e += """<p>You can <a href ="/edit/{link}/{itemid}">edit it</a></p>"""
    e = e.format(itemid = itemid, itemname = itemname, link = link)
    return template("error", error = e)


def check_login(auto=False):
    """use cookie to check if login
    
    """
    if auto:
        uid = request.get_cookie("uid")
        if uid in ["",None]:
            redirect("/login")
    else:       
        uid = request.get_cookie("uid")
        if uid not in ["",None]:
            return True
        else:
            return False

def check_reporter():
    """Check if user is reporter.
    If is user, return true, else redirect to error page
    
    :returns: True or False
    """
    uid = request.get_cookie("uid")
    if uid == None:
        redirect("/login")
    reporter = db.select_something("users",("reporter",),{"id":uid},onlyone=True)[0]
    if reporter != 1:
        return False
    else:
        return True


    
def get_now(onlydate=False, onlytime=False, forfile = False):
    """Return the datetime for now
    
    :param onlydate: If only return date
    :type onlydate: Boolean, default False
    :param onlytime: If only return time
    :type onlytime: Boolean default False
    :returns: A time string    
    """
    if onlydate:
        return datetime.datetime.now().strftime("%Y-%m-%d")
    if onlytime:
        return datetime.datetime.now().strftime("%H:%M:%S")
    if forfile:
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    else:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_pic(pic, ext, uid, dest = "static/images/"):
    """Store the uplpaded pic into static/images folder
    with the ext and user id
    
    :param dest: where pic was stored
    :type dest: a string
    :param pic: the pic object
    :type pic: bottle.request.FileUpload.Filefeld
    :param ext: the file name extention
    :type ext: 
    """
    stamp = get_now(forfile=True)
    fn = str(uid)+"_"+stamp + ext
    with open(dest+fn, 'wb') as fp:
        fp.write(pic.file.read())
    return fn