#!/usr/bin/env python3

from faker import Faker
from app import db
from models import Trainer, Monster, TrainerMonster, ShopItem, TrainerItem, Battle

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Seeding the database...")

        # Seed trainers
        trainers = []
        for _ in range(5):
            trainer = Trainer(username=fake.user_name())
            trainers.append(trainer)

        db.session.add_all(trainers)
        db.session.commit()

        # Seed monsters
        monsters = []
        for _ in range(10):
            monster = Monster(name=fake.first_name(), type=fake.word(), level=fake.random_int(min=1, max=100))
            monsters.append(monster)

        db.session.add_all(monsters)
        db.session.commit()

        # Seed trainer-monsters relationship
        for trainer in trainers:
            for _ in range(fake.random_int(min=1, max=5)):
                trainer_monster = TrainerMonster(trainer_id=trainer.trainer_id,
                                                 monster_id=fake.random_element(elements=monsters).monster_id,
                                                 capture_date=fake.date_between(start_date='-1y', end_date='today'),
                                                 level_when_caught=fake.random_int(min=1, max=100))
                db.session.add(trainer_monster)

        db.session.commit()

        # Seed shop items
        items = [
            {'name': 'Potion', 'description': 'Restores HP', 'price': 50},
            {'name': 'Ether', 'description': 'Restores MP', 'price': 100},
            {'name': 'Revive', 'description': 'Revives a fainted Pokémon', 'price': 200}
        ]

        shop_items = []
        for item_data in items:
            item = ShopItem(name=item_data['name'], description=item_data['description'], price=item_data['price'])
            shop_items.append(item)

        db.session.add_all(shop_items)
        db.session.commit()

        # Seed trainer-items relationship
        for trainer in trainers:
            for _ in range(fake.random_int(min=1, max=5)):
                trainer_item = TrainerItem(trainer_id=trainer.trainer_id,
                                           item_id=fake.random_element(elements=shop_items).item_id,
                                           quantity=fake.random_int(min=1, max=10))
                db.session.add(trainer_item)

        db.session.commit()

        # Seed battles
        for _ in range(20):
            battle = Battle(trainer_id=fake.random_element(elements=trainers).trainer_id,
                            monster_id=fake.random_element(elements=monsters).monster_id,
                            result=fake.random_element(elements=['Win', 'Loss']),
                            timestamp=fake.date_time_between(start_date='-1y', end_date='today'))
            db.session.add(battle)

        db.session.commit()

        print('Database seeding completed.')