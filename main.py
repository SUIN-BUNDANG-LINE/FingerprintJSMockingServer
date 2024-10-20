from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/finger-print")
async def get_finger_print():
    await asyncio.sleep(0.175)
    return {}
