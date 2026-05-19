from pydantic import BaseModel


class PredictionInput(BaseModel):
    hour: int
    temperature: float
    peak_hour: int
    holiday: int