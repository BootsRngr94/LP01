#!/usr/bin/env python3

from faker import Faker
from app import app
from models import db, Trainer, Monster, TrainerMonster, ShopItem, TrainerItem, Battle

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        #Delete database
        print("Spring cleaning the database...")
        db.session.query(Trainer).delete()
        db.session.query(Monster).delete()
        db.session.query(TrainerMonster).delete()
        db.session.query(ShopItem).delete()
        db.session.query(TrainerItem).delete()
        db.session.query(Battle).delete()

        #Seeding database
        print("Database initializing")

        print('Logging trainers...')
        t1 = Trainer(username='Green')
        t2 = Trainer(username='Blue')
        t3 = Trainer(username='Red')
        db.session.add_all([t1, t2, t3])
        db.session.commit()

        print('Spawning monsters...')
        monsters = [
            #Three typings available- Corona(), Aurora(), Flash()
            Monster(name='Stikan', type='Aurora', level='1'),
            Monster(name='Eegu', type='Aurora', level='1'),
            Monster(name='Massero', type='Aurora', level='1'),
            Monster(name='Koman', type='Corona', level='1'),
            Monster(name='Vidir', type='Corona', level='1'),
            Monster(name='Mesa', type='Corona', level='1'),
            Monster(name='Zozin', type='Flash', level='1'),
            Monster(name='Naja', type='Flash', level='1'),
            Monster(name='Kubu', type='Flash', level='1'),
        ]
        db.session.add_all(monsters)
        db.session.commit()
        