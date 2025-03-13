from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Admin API is working"}