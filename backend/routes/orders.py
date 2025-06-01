from fastapi import APIRouter
from models import Order,Product
from services import load_orders, save_orders

router = APIRouter()

orders = load_orders()
# for order in orders:
    # for order_item in order.order_items:
        # order_item.product = Product(**order_item.product)

@router.get("/orders")
def get_orders():
    return orders

@router.post("/orders")
def add_order(order: Order):
    orders.append(orders)
    save_orders(orders)
    return {"maseg": "your order added seccessfully"} 






