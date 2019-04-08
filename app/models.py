from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db




class Company_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names_one= db.Column(db.String(120), index=True)
    names_two = db.Column(db.String(80), index=True)
    names_three = db.Column(db.String(80), index=True)
    branches = db.Column(db.String(80))
    def __repr__(self):
        return 'Company_list {}'.format(self.one_name)

