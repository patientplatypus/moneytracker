# models/race.py
from shared import db, dump_datetime
# from models.unit import Unit
import datetime
#
# race_units = db.Table('race_units',
#     db.Column('race_id', db.Integer, db.ForeignKey('races.id')),
#     db.Column('unit_id', db.Integer, db.ForeignKey('units.id'))
# )
#
# class Race(db.Model):
#     __tablename__ = 'races'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     description = db.Column(db.Text)
#     created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
#     updated_at = db.Column(db.DateTime)
#     # This is the connection for many to many relationship between race and units
#     units = db.relationship('Unit', secondary=race_units,
#         backref=db.backref('race', lazy='dynamic'))
#
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#
#     @property
#     def serialize(self):
#        """Return object data in easily serializable format"""
#        return {
#            'id'         : self.id,
#            'name'       : self.name,
#            'description': self.description,
#            'units'      : self.units,
#            'created_at' : dump_datetime(self.created_at)
#        }
#
#     def __repr__(self):
#         return '<Race %r>' % self.name



# q = """CREATE TABLE IF NOT EXISTS ledgertable (
#          id int,
#          profitorloss varchar(255),
#          listname varchar(255)
#          itemname  VARCHAR(255),
#          itemdescription  VARCHAR(255))"""
# cur.execute(q)


class Profit(db.Model):
    __tablename__ = 'ledger'
    id = db.Column(db.BigInteger, primary_key=True, nullable=True)
    profitorloss = db.Column(db.String(255), unique=False, nullable=True)
    listname = db.Column(db.String(255), unique=False, nullable=True)
    itemname = db.Column(db.String(255), unique=False, nullable=True)
    itemdescription = db.Column(db.String(255), unique=False, nullable=True)

    def __init__(self, profitorloss, listname, itemname, itemdescription):
        self.profitorloss = profitorloss
        self.listname = listname
        self.itemname = itemname
        self.itemdescription = itemdescription

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id'             : self.id,
            'profitorloss'   : self.profitorloss,
            'listname'       : self.listname,
            'itemname'       : self.itemname,
            'itemdescription': self.itemdescription
        }

    def __repr__(self):
        return '<ledger %r>' % self.name
