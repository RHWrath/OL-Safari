from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from loguru import logger
from pathlib import Path

from API.database import get_db, init_db
from API.models import Destination, DestinationSchema
from API.seed import seed

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="OLIPSafari",
    description="Travel destinations API for OLIP",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()
    seed()


@app.get("/", response_class=FileResponse)
def serve_frontend():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/destinations")
def get_locations(db: Session = Depends(get_db)):
    """Get locations endpoint"""
    destinations = db.query(Destination).all()
    return {"destinations": [DestinationSchema.from_orm(d) for d in destinations]}