from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from config import db
from sqlalchemy.ext.hybrid import hybrid_property


# Models go here!
#Main models are Trainer, Monsters, TrainerMonsters, TrainersItems, Battles, ShopItems

class Trainer(db.Model):
    __tablename__ = 'trainers'
    trainer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    # Define relationships
    trainer_monsters = db.relationship('TrainerMonster', backref='trainer', lazy='dynamic')
    trainer_items = db.relationship('TrainerItem', backref='trainer', lazy='dynamic')
    battles = db.relationship('Battle', backref='trainer', lazy='dynamic')
    # Validations
    @validates('username')
    def validate_username(self, key, username):
        if isinstance(username, str):
            return username
        else:
            raise ValueError('Username must be a string!')
    @validates('password_hash')
    def validate_password(self, key, password_hash):
        if isinstance(password_hash, str):
            return password_hash
        else:
            raise ValueError('Password must be a string!')

class Monster(db.Model):
    __tablename__ = 'monsters'
    monster_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    level = db.Column(db.Integer)
    # Define relationships
    trainer_monsters = db.relationship('TrainerMonster', backref='monster', lazy='dynamic')
    battles = db.relationship('Battle', backref='monster', lazy='dynamic')

class TrainerMonster(db.Model):
    __tablename__ = 'trainer_monsters'
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.trainer_id'), primary_key=True)
    monster_id = db.Column(db.Integer, db.ForeignKey('monsters.monster_id'), primary_key=True)
    capture_date = db.Column(db.Date)
    level_when_caught = db.Column(db.Integer)

class ShopItem(db.Model):
    __tablename__ = 'shop_items'
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

class TrainerItem(db.Model):
    __tablename__ = 'trainer_items'
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.trainer_id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('shop_items.item_id'), primary_key=True)
    quantity = db.Column(db.Integer)

class Battle(db.Model):
    __tablename__ = 'battles'
    battle_id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.trainer_id'))
    monster_id = db.Column(db.Integer, db.ForeignKey('monsters.monster_id'))
    result = db.Column(db.String)
    timestamp = db.Column(db.DateTime)