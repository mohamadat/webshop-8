from fastapi import FastAPI

from routes.products import router
from routes.orders import router as order_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],  # allow frontend access

    allow_methods=["*"],

    allow_headers=["*"],

)

app.include_router(router)

app.include_router(order_router)

@app.get("/hoi")

def hello():

    return {"message": "welcome to me API"}