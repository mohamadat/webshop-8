from fastapi import APIRouter
from models import Product
from services import load_products, save_products

router = APIRouter()

products = load_products()

@router.get("/products")
def get_products():
    return products

@router.post("/products")
def add_product(product: Product):
    products.append(product)
    save_products(products)
    return {"maseg": "product added seccessfully"}
