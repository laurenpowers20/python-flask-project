from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

# db = PostgresqlDatabase('people', user='laurenpowers',
#                         password='12345', host='localhost', port=5432)


# class BaseModel(Model):
#     class Meta:
#         database = db


# class Pasta(BaseModel):
#     name = CharField()
#     description = CharField()


# db.connect()
# db.drop_tables([Pasta])
# db.create_tables([Pasta])

# Pasta(name='Farfalle', description='bow tie shaped').save()
# Pasta(name='Fusilli', description='cork screw shaped').save()

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"
  
@app.route('/get-json')
def get_json():
  return jsonify({
    "name": "Garfield",
    "hatesMondays": True,
    "friends": ["Sheldon", "Wade", "Orson", "Squeak"]
  })


app.run(debug=True, port=5000)
