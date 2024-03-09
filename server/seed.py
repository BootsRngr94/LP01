#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Trainer, Monster, TrainerMonster, ShopItem, TrainerItem, Battle

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Spring cleaning the database!")
        #Delete all db records
        db.session.query(Trainer).delete()
        db.session.query(Monster).delete()
        db.session.query(TrainerMonster).delete()
        db.session.query(ShopItem).delete()
        db.session.query(TrainerItem).delete()
        db.session.query(Battle).delete()

        print("Starting up the database...")

        print('Gathering Trainer info...')

        print('Creating trainers...')
        
