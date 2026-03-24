import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "pycharm é legal"}


@app.get("/funcaotest")
async def funcaotest():
    return {"teste": True, "num_aletorio": random.randint(0, 1000)}