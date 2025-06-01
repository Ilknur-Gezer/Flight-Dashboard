import requests
import os
from datetime import datetime, timedelta, timezone
from dateutil import parser
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
BASE_URL = "http://api.aviationstack.com/v1/flights"

def get_flight_by_number(flight_number: str):
    params = {
        "access_key": API_KEY,
        "flight_iata": flight_number
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        flights = data.get("data", [])
        if flights:
            flight = flights[0]
            return {
                "callsign": flight["flight"].get("iata"),
                "airline": flight["airline"].get("name"),
                "departure": flight["departure"].get("airport"),
                "arrival": flight["arrival"].get("airport"),
                "status": flight.get("flight_status"),
                "delay": flight["departure"].get("delay"),
                "departure_time": flight["departure"].get("scheduled"),
                "arrival_time": flight["arrival"].get("scheduled")
            }
    return None

