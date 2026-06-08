from fastapi import FastAPI
from app.routes.data_routes import router as data_router
from app.routes.meter_routes import router as meter_router
from app.routes.analytics_routes import router as analytics_router
from app.routes.prediction_routes import router as prediction_router
from app.routes.view_routes import router as view_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Smart City",
    version="1.0.0"
)

app.include_router(data_router)
app.include_router(meter_router)
app.include_router(analytics_router)
app.include_router(prediction_router)
app.include_router(view_router)

@app.get('/')
def home_page():
    return {"message": "Smart city API is running"}


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)