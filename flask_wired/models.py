# -*- coding: utf-8 -*-
from datetime import datetime
from flask_wired.extensions import db

__all__ = ['UserProfile']


class UserProfile(db.Model):
    __tablename__ = "user_profile"

    id = db.Column('id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String)
    last_name = db.Column('last_name', db.String)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    modified_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
