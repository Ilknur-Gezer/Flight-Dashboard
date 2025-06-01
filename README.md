# Flight Operations Dashboard ✈️

This is a FastAPI-based dashboard to retrieve and display live flight information using the AviationStack API.

## Features
- Query flights by flight number
- Display flight status, departure/arrival times, delays
- Web interface using Jinja2 and Bootstrap

## Run locally
```bash
uvicorn app.main:app --reload --port 8000
