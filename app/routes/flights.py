# flights.py
from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse
from app.services.aviationstack import get_flight_by_number
from unidecode import unidecode
from app.utils.templates import templates



router = APIRouter()

def normalize(text):
    return unidecode(text.lower()) if text else ""
'''
@router.get("/flights/live")
def live_flights(
    limit: int = 5,
    date: str = None,
    status: str = None,
    departure: str = None,
    arrival: str = None,
    filter_by_time: bool = True
):
    flights = get_live_flights(
        limit=limit,
        date=date,
        status=status,
        departure=departure,
        arrival=arrival,
        filter_by_time=filter_by_time
    )

    return {"flights": flights}


@router.get("/flights/summary")
def flight_summary(limit: int = 100):
    flights = get_live_flights(limit=limit)
    summary = {"total_flights": len(flights), "statuses": {}}

    for flight in flights:
        status = flight.get("status", "unknown")
        summary["statuses"][status] = summary["statuses"].get(status, 0) + 1

    return summary


@router.get("/flights/inbound_outbound")
def inbound_outbound(airport: str = Query(...), limit: int = 50):
    flights = get_live_flights(limit=limit)
    inbound = []
    outbound = []
    target = normalize(airport)

    for flight in flights:
        dep = normalize(flight.get("departure"))
        arr = normalize(flight.get("arrival"))

        if target in arr:
            inbound.append(flight)
        if target in dep:
            outbound.append(flight)

    return {
        "airport": airport,
        "inbound": inbound,
        "outbound": outbound
    }
'''

@router.get("/flights/by_number", response_class=HTMLResponse)
def flight_by_number(request: Request, flight_number: str = None):
    from app.services.aviationstack import get_flight_by_number

    result = None
    if flight_number:
        result = get_flight_by_number(flight_number)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "result": result
    })