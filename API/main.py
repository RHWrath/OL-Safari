from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
import asyncio
from loguru import logger
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(
    title="UIM Service Manager",
    description="Unified Intent Mediator - Service Catalogue with Query Interface",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", response_class=FileResponse)
def serve_frontend():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy"
    }

@app.get("/destinations")
def Get_locations():
    """Get locations endpoint"""
    return {
        "destinations": [
            {"name": "Johannesburg", "lat": -26.2041, "lng": 28.0473, "description": "City of Gold, South Africa"},
            {"name": "London", "lat": 51.5074, "lng": -0.1278, "description": "Historic capital of England"},
            {"name": "Marsa Alam", "lat": 25.0674, "lng": 34.8876, "description": "Red Sea diving paradise, Egypt"},
            {"name": "Las Vegas", "lat": 36.1699, "lng": -115.1398, "description": "Entertainment capital of the world"},
            {"name": "Miami", "lat": 25.7617, "lng": -80.1918, "description": "Sun, beaches and nightlife"},
            {"name": "Tenerife", "lat": 28.2916, "lng": -16.6291, "description": "Largest of the Canary Islands"},
            {"name": "Paris", "lat": 48.8566, "lng": 2.3522, "description": "City of Light, France"},
            {"name": "Lisbon", "lat": 38.7223, "lng": -9.1393, "description": "Coastal capital of Portugal"}
        ]
    }