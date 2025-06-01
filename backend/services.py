import json
from models import Product, Order


DB_FILE = "db.json"

def load_products():
    with open(DB_FILE, "r") as f:
        products = json.load(f)
    return [Product(**product) for product in products]


def save_products(products):
    with open(DB_FILE, "w") as f:
        json.dump([product.dict() for product in products] ,f, indent=4)


ORDERS_FILE = "orders.json"

def load_orders():
    with open(ORDERS_FILE, "r") as f:
        orders = json.load(f)
    return [Order(**order) for order in orders]


def save_orders(orders):
    with open(ORDERS_FILE, "w") as f:
        json.dump([order.dict() for order in orders] ,f, indent=4)        