from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..dependencies import get_db, get_current_company

router = APIRouter(prefix="/trips")

@router.post("/")
def create_trip(
    trip: schemas.TripCreate,
    token: str,
    db: Session = Depends(get_db)
):
    company_id = get_current_company(token)

    new_trip = models.Trip(
        start_location=trip.start_location,
        end_location=trip.end_location,
        company_id=company_id
    )
    db.add(new_trip)
    db.commit()
    return {"msg": "Trip created"}