# coding: utf-8

from . import db


Base = db.Model
metadata = Base.metadata


#class TableExample(Base):
#    __tablename__ = 'tablename'
#
#    first_field = db.Column(db.Integer, primary_key=True)
#    second_field = db.Column(db.String(2))
#    third_field = db.Column(db.String(11))


#class ViewExample(Base):
#    __tablename__ = 'viewname'
#    __table_args_ = (db.UniqueConstraint('first_field', 'second_field'))
#
#    first_field = db.Column(db.String(2), primary_key=True)
#    second_field = db.Column(db.String(11), primary_key=True)
#    third_field = db.Column(db.Integer)
