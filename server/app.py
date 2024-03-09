#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, api
# Add your model imports
from models import db, Trainer, Monster, TrainerMonster, ShopItem, TrainerItem, Battle

# Views go here!

@app.route('/')
def index():
    return '<h1>Server up and running!</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

