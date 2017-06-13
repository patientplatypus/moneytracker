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

# profit or loss
# list name
# amount
# description

conn = psycopg2.connect(database = "profitnloss3", user = "patientplatypus", password = "Fvnjty0b")
cur = conn.cursor()
q = """CREATE TABLE IF NOT EXISTS ledger (
         id Bigint,
         profitorloss varchar(255),
         listname varchar(255),
         itemname  VARCHAR(255),
         itemdescription  VARCHAR(255))"""
cur.execute(q)
conn.commit()
conn.close()

# if request.args.has_key('campaign_id_crid'):


@app.route('/', methods=['GET', 'DELETE', 'POST'])
def profits():
    if request.method=='GET':
        if 'listname' in request.json:
            print 'inside listname == True!!!'
            conn = psycopg2.connect(database = "profitnloss3", user = "patientplatypus", password = "Fvnjty0b")
            cur = conn.cursor()
            sql = 'SELECT * FROM ledger WHERE listname = %s'
            params = (request.json['listname'])
            cur.execute(sql, params)
            conn.commit()
            data = cur.fetchall()
            conn.close()
            return jsonify(data)
        else:
            print 'inside listname == False!!!'
            conn = psycopg2.connect(database = "profitnloss3", user = "patientplatypus", password = "Fvnjty0b")
            cur = conn.cursor()
            sql = 'SELECT * FROM ledger'
            cur.execute(sql)
            conn.commit()
            data = cur.fetchall()
            conn.close()
            return jsonify(data)
    if request.method=='DELETE':
        conn = psycopg2.connect(database = "profitnloss3", user = "patientplatypus", password = "Fvnjty0b")
        cur = conn.cursor()
        sql = "DELETE FROM ledger WHERE id = %s"
        params = (request.json['id'])
        cur.execute(sql,params)
        conn.commit()
        conn.close()
        return('successfully deleted from database')
    if request.method=='POST':
        print 'inside the post if statement'
        conn = psycopg2.connect(database = "profitnloss3", user = "patientplatypus", password = "Fvnjty0b")
        cur = conn.cursor()
        sql = 'INSERT INTO "ledger" (ID, PROFITORLOSS, LISTNAME, ITEMNAME, ITEMDESCRIPTION) VALUES (%s,  %s, %s, %s, %s)'
        params = (request.json['id'],  request.json['profitorloss'], request.json['listname'], request.json['itemname'], request.json['itemdescription'])
        cur.execute(sql, params)
        conn.commit()
        print "Records created successfully";
        conn.close()
        return('successfully added to database')

# @app.route('/add', methods=['POST'])
# def profits():
#     if request.method=='POST':
#         print 'inside the post if statement'
#         conn = psycopg2.connect(database = "profitnloss", user = "patientplatypus", password = "Fvnjty0b")
#         cur = conn.cursor()
#         sql = 'INSERT INTO "ledgertable" (ID, PROFITORLOSS, LISTNAME, ITEMNAME, ITEMDESCRIPTION) VALUES (%s,  %s, %s, %s, %s)'
#         params = (request.json['id'],  request.json['profitorloss'], request.json['listname'], request.json['itemname'], request.json['itemdescription'])
#         cur.execute(sql, params)
#         conn.commit()
#         print "Records created successfully";
#         conn.close()
#         return('successfully added to database')

# @app.route('/loss', methods=['POST'])
# def profits():
#     if request.method=='POST':
#         print 'inside the post if statement'
#         conn = psycopg2.connect(database = "profitnloss", user = "patientplatypus", password = "Fvnjty0b")
#         cur = conn.cursor()
#         sql = 'INSERT INTO "ledgertable" (ID, PROFITORLOSS, LISTNAME, ITEMNAME, ITEMDESCRIPTION) VALUES (%s, "loss", %s, %s, %s)'
#         params = (request.json['id'], request.json['listname'], request.json['itemname'], request.json['itemdescription'])
#         cur.execute(sql, params)
#         conn.commit()
#         print "Records created successfully";
#         conn.close()
#         return('successfully added to database')

# If this file is being run directly, then start Flask
if __name__ == '__main__':
    app.run(debug=True)
