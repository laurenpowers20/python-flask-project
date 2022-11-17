from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('people', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db
    
class Pasta(BaseModel):
  name = CharField()
  description = CharField()
  
