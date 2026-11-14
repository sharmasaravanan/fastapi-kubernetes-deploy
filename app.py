import os
from fastapi import FastAPI

app = FastAPI(title="Power Operations Health Monitor")
SERVICE_NAME = os.getenv("SERVICE_NAME", "power-health-api")
APP_ENV = os.getenv("APP_ENV", "training")

READINGS = [
    {"equipment_id": "SUB-101", "voltage_kv": 220.1, "status": "normal"},
    {"equipment_id": "SUB-102", "voltage_kv": 218.7, "status": "normal"},
    {"equipment_id": "SUB-103", "voltage_kv": 205.2, "status": "investigate"},
]

@app.get("/")
def root():
    return {"service": SERVICE_NAME, "environment": APP_ENV}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/readings")
def readings():
    return {"count": len(READINGS), "items": READINGS}
