"""

"""
import math
import os

from pathlib import Path, WindowsPath

#import pandas as pd
from itertools import *

#import utils.shop as shp
import db_connection as dbs

print(__name__)#  main

a = "fdsfds"



import datetime
POSTS = [
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 8),
    },
    {
        'tags': 'django, hiking',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 9),
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 12),
    },
    {
        'tags': 'django,music',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 11),
    },
    {
        'tags': 'jazz',
        'title' : 'Random title',
        'body': 'dasdsadasdsa',
        'published': datetime.date(2023, 5, 10),
    },
]
def buy(poost):
    for post in POSTS:
        if post == poost:
            return print(f"{POSTS['title']}")