from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    image_url : str
   
class User(BaseModel):
    name : str
    email : str
    adress : str

class order_item(BaseModel):
    product_id : int
    quantity : int
    

class Order(BaseModel):
    user : User
    order_items : list[order_item]
    total_price : float = None
    


