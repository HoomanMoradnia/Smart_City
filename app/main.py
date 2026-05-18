from fastapi import FastAPI
from app.routes.data_routes import router as data_router

app = FastAPI(
    title="Smart City Smart Grid API",
    version="1.0.0"
)

app.include_router(data_router)

@app.get('/')
def home_page():
    return {"message": "Smart city API is running"}