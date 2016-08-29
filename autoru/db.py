#!/usr/bin/python3

from peewee import *

db = MySQLDatabase(host="127.0.0.1",port=3306,user="autoru",passwd="autoru",database="autoru")

class Auto(Model):
    year    = IntegerField(default=0)
    price   = IntegerField(default=0)
    mileage = IntegerField(default=0)
    owner  = IntegerField(default=0)
    class Meta:
        database = db



db.connect()
try:
    db.create_tables([Auto])
except:
    pass
