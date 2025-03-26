from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

db = SQLAlchemy()




class User(db.Model):
    """ Table for groups"""
    __tablename__ = 'groups'
    userId = db.Column(db.Integer,
                        primary_key = True,
                        autoincrement = True)
    firstName = db.Column(db.String(150),
                         index = False,
                         unique = False,
                         nullable = False)
    lastName = db.Column(db.DateTime,
                          index = False,
                          unique = False,
                          nullable = False)
    email  = db.Column(db.String(150),
                          index = False,
                          unique = True,
                          nullable = False)

    def __init__(self, userId, firstName, lastName, email):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

