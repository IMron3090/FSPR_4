import re


USERS = [
    {
        "name": "Bahti",
        "password": "234$fjfdsd",
        "email": "bahti@gmail.com",
        "purchases": [],
        "card": {"code": "3647583465734283", "balance": 1000},
    },
    {
        "name": "Bale",
        "password": "bale345345@",
        "email": "bale@gmail.com",
        "purchases": [],
        "card": {"code": "4567485767574876", "balance": 200},
    },
]
PRODUCTS = [
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "color": "black",
    },
    {
        "product_name": "bag",
        "count": 20,
        "price": 200,
        "color": "gray",
    },
]


class Store:
    purchases = []

    def init(self, name, email, password, card_code, card_balance):
        self.name = name
        self.password = password
        self.email = email
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        for user in USERS:
            if email == user["email"] and user["password"] == password:
                return "Пользователь с этим адресом электронной почты или паролем уже существует."

        if not (name and email and password and card_balance and card_code):
            return "Были заданы пустые значения."