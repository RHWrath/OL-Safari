from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import asyncio
from loguru import logger

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


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy"
    }

@app.get("/Destinations")
def Get_locations():
    """Get locations endpoint"""
    return {
        "locations": ["Jberg", "Cape town", "Florida", "Sydney"]
    }