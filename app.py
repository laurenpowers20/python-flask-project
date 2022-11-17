from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('pasta', user='laurenpowers',
                        password='12345', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Pasta(BaseModel):
    name = CharField()
    description = CharField()

db.connect()
db.drop_tables([Pasta])
db.create_tables([Pasta])

Pasta(name='Farfalle', description='bow tie shaped').save()
Pasta(name='Fusilli', description='cork screw shaped').save()

app = Flask(__name__)

@app.route('/pasta/', methods=['GET', 'POST'])
@app.route('/pasta/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Pasta.get(Pasta.id == id)))
    else:
        pasta_list = []
        for pasta in Pasta.select():
            pasta_list.append(model_to_dict(pasta))
        return jsonify(pasta_list)
    

app.run(debug=True, port=5000)
