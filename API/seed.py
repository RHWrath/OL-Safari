"""
Run once after the DB is provisioned to seed the initial destinations.
    python seed.py
"""
from API.database import SessionLocal, init_db
from API.models import Destination

DESTINATIONS = [
    {"name": "Johannesburg", "lat": -26.2041, "lng": 28.0473, "description": "City of Gold, South Africa"},
    {"name": "London", "lat": 51.5074, "lng": -0.1278, "description": "Historic capital of England"},
    {"name": "Marsa Alam", "lat": 25.0674, "lng": 34.8876, "description": "Red Sea diving paradise, Egypt"},
    {"name": "Las Vegas", "lat": 36.1699, "lng": -115.1398, "description": "Entertainment capital of the world"},
    {"name": "Miami", "lat": 25.7617, "lng": -80.1918, "description": "Sun, beaches and nightlife"},
    {"name": "Tenerife", "lat": 28.2916, "lng": -16.6291, "description": "Largest of the Canary Islands"},
    {"name": "Paris", "lat": 48.8566, "lng": 2.3522, "description": "City of Light, France"},
    {"name": "Lisbon", "lat": 38.7223, "lng": -9.1393, "description": "Coastal capital of Portugal"},
]


def seed():
    init_db()
    db = SessionLocal()
    try:
        existing = db.query(Destination).count()
        if existing > 0:
            print(f"[!] Already {existing} destinations in DB, skipping seed")
            return

        for d in DESTINATIONS:
            db.add(Destination(**d))
        db.commit()
        print(f"[+] Seeded {len(DESTINATIONS)} destinations")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
