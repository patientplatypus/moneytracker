from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import sqlite3
import psycopg2

import os
from os.path import join, dirname
from dotenv import load_dotenv

from models.shared import db
from models.profits import Profit
#from models.race_unit import RaceUnit

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s/%s' % (os.environ.get('DB_DRIVER'), os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'), os.environ.get('DB_NAME'))

db.app = app
db.init_app(app)
# Create tables if they don't already exist
db.create_all()


# def checkTableExists(dbcon, tablename):
#     dbcur = dbcon.cursor()
#     dbcur.execute("""
#         SELECT COUNT(*)
#         FROM information_schema.tables
#         WHERE table_name = '{0}'
#         """.format(tablename.replace('\'', '\'\'')))
#     if dbcur.fetchone()[0] == 1:
#         dbcur.close()
#         return True
#
#     dbcur.close()
#     return False
#

conn = psycopg2.connect(database = "onetwothree", user = "patientplatypus", password = "Fvnjty0b")
cur = conn.cursor()
q = """CREATE TABLE IF NOT EXISTS onetwothree (
         id int,
         name  VARCHAR(255),
         description  VARCHAR(255))"""
cur.execute(q)
conn.commit()
conn.close()




@app.route('/')
def index():
    return 'At Index of Python Backend'
#
# @app.route('/loss', methods=['GET','POST','DELETE','PUT'])
# def races():
#     return 'loss'

# @app.route('/profit', methods=['POST'])
# def profits():
#     profit = {
#     'id':request.json['id'],
#     'title':request.json['title'],
#     'description':request.json['description']
#     }
#     profits.append(profit)

#
@app.route('/profit', methods=['POST','GET','DELETE'])
def profits():
    if request.method=='POST':
        print 'inside the post if statement'
        conn = psycopg2.connect(database = "onetwothree", user = "patientplatypus", password = "Fvnjty0b")
        cur = conn.cursor()
        sql = 'INSERT INTO "onetwothree" (ID,NAME,DESCRIPTION) VALUES (%s, %s, %s)'
        params = (request.json['id'], request.json['name'], request.json['description'])
        cur.execute(sql, params)
        conn.commit()
        print "Records created successfully";
        conn.close()
        return('successfully added to database')
    if request.method=='GET':
        conn = psycopg2.connect(database = "onetwothree", user = "patientplatypus", password = "Fvnjty0b")
        cur = conn.cursor()
        sql = 'SELECT * FROM onetwothree'
        cur.execute(sql)
        conn.commit()
        data = cur.fetchall()
        conn.close()
        return jsonify(data)
    if request.method=='DELETE':
        conn = psycopg2.connect(database = "onetwothree", user = "patientplatypus", password = "Fvnjty0b")
        cur = conn.cursor()
        sql = "DELETE FROM onetwothree WHERE id = %s"
        params = (request.json['id'])
        cur.execute(sql,params)
        conn.commit()
        conn.close()
        return('successfully deleted from database')
#
# @app.route('/food', methods=['GET','POST','DELETE','PUT'])
# def races_units(race_name):
#     return 'food'
#
# @app.route('/rent', methods=['GET','POST','DELETE','PUT'])
# def races_units(race_name):
#     return 'rent'
#
# @app.route('/utilities', methods=['GET','POST','DELETE','PUT'])
# def races_units(race_name):
#     return 'utilities'
#
# @app.route('/salary', methods=['GET','POST','DELETE','PUT'])
# def races_units(race_name):
#     return 'salary'
#
# @app.route('/interest', methods=['GET','POST','DELETE','PUT'])
# def races_units(race_name):
#     return 'interest'



# If this file is being run directly, then start Flask
if __name__ == '__main__':
    app.run(debug=True)
