#!/usr/bin/python3

from peewee import *

db = MySQLDatabase(host="127.0.0.1",port=3306,user="lp",passwd="lppasswd",database="lp")

class Photo(Model):
    login       =   CharField()
    url         =   CharField()
    filename    =   CharField()
    path        =   CharField()
    class Meta:
        database = db

class Form(Model):
    login       = CharField()
    url         = CharField()
    age         = IntegerField(default=0)
    height      = IntegerField(default=0)
    weight      = IntegerField(default=0)
    state       = CharField()
    auto        = CharField()
    income      = CharField()
    scope       = CharField()
    education   = CharField()
    children    = CharField()
    smoke       = CharField()
    alcohol     = CharField()
    foreign     = CharField()
    housing     = CharField()
    education_e = CharField()
    music_e     = CharField()
    movies_e    = CharField()
    books_e     = CharField()
    hobby_e     = CharField()
    like_e      = CharField()
    search_from = IntegerField(default=0)
    search_to   = IntegerField(default=0)
    search_for  = CharField()
    search_who  = CharField()
    search_who2 = CharField()
    about_me    = CharField()
    body        = CharField()
    premium     = BooleanField()
    class Meta:
        database = db


db.connect()
try:
    db.create_tables([Photo])
except:
    pass
try:
    db.create_tables([Form])
except:
    pass
