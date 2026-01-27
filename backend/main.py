from metrics import compute_workstation_metrics
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


from db import engine, Base
from models import Event
from schemas import EventCreate
from dependencies import get_db
from models import Worker, Workstation
from sqlalchemy import delete 
from metrics import compute_worker_metrics
from datetime import timedelta



app = FastAPI(title="AI Worker Productivity API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend is running successfully"}


@app.post("/events")
def ingest_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(
        timestamp=event.timestamp,
        worker_id=event.worker_id,
        workstation_id=event.workstation_id,
        event_type=event.event_type,
        confidence=event.confidence,
        count=event.count
    )
    db.add(db_event)
    db.commit()
    return {"status": "event stored successfully"}
@app.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    # Clear existing data
    db.execute(delete(Event))
    db.execute(delete(Worker))
    db.execute(delete(Workstation))
    db.commit()

    # Create workers
    workers = [
        Worker(worker_id="W1", name="Amit"),
        Worker(worker_id="W2", name="Rahul"),
        Worker(worker_id="W3", name="Sneha"),
        Worker(worker_id="W4", name="Priya"),
        Worker(worker_id="W5", name="Rohit"),
        Worker(worker_id="W6", name="Neha"),
    ]

    # Create workstations
    stations = [
        Workstation(station_id="S1", name="Assembly"),
        Workstation(station_id="S2", name="Packaging"),
        Workstation(station_id="S3", name="Quality Check"),
        Workstation(station_id="S4", name="Welding"),
        Workstation(station_id="S5", name="Painting"),
        Workstation(station_id="S6", name="Dispatch"),
    ]

    db.add_all(workers + stations)
    db.commit()

    return {"status": "Factory data seeded successfully"}
@app.get("/metrics/workers")
def get_worker_metrics(db: Session = Depends(get_db)):
    events = db.query(Event).order_by(Event.timestamp).all()

    raw_metrics = compute_worker_metrics(events)

    response = []

    for worker_id, data in raw_metrics.items():
        total_time = data["working_time"] + data["idle_time"]

        utilization = (
            (data["working_time"] / total_time) * 100
            if total_time.total_seconds() > 0 else 0
        )

        units_per_hour = (
            data["units_produced"] / (data["working_time"].total_seconds() / 3600)
            if data["working_time"].total_seconds() > 0 else 0
        )

        response.append({
            "worker_id": worker_id,
            "working_minutes": round(data["working_time"].total_seconds() / 60, 2),
            "idle_minutes": round(data["idle_time"].total_seconds() / 60, 2),
            "utilization_percent": round(utilization, 2),
            "units_produced": data["units_produced"],
            "units_per_hour": round(units_per_hour, 2)
        })

    return response
@app.get("/metrics/workstations")
def get_workstation_metrics(db: Session = Depends(get_db)):
    events = db.query(Event).order_by(Event.timestamp).all()
    raw_metrics = compute_workstation_metrics(events)

    response = []

    for station_id, data in raw_metrics.items():
        occupied_hours = data["occupied_time"].total_seconds() / 3600

        throughput = (
            data["units_produced"] / occupied_hours
            if occupied_hours > 0 else 0
        )

        response.append({
            "workstation_id": station_id,
            "occupied_minutes": round(data["occupied_time"].total_seconds() / 60, 2),
            "units_produced": data["units_produced"],
            "throughput_per_hour": round(throughput, 2)
        })

    return response
@app.get("/metrics/factory")
def get_factory_metrics(db: Session = Depends(get_db)):
    events = db.query(Event).order_by(Event.timestamp).all()

    # Worker-level metrics reuse
    worker_metrics = compute_worker_metrics(events)

    total_working_time = 0
    total_units = 0
    utilization_sum = 0
    worker_count = 0

    for data in worker_metrics.values():
        working_seconds = data["working_time"].total_seconds()
        idle_seconds = data["idle_time"].total_seconds()
        total_time = working_seconds + idle_seconds

        if total_time > 0:
            utilization_sum += (working_seconds / total_time) * 100
            worker_count += 1

        total_working_time += working_seconds
        total_units += data["units_produced"]

    avg_utilization = (
        utilization_sum / worker_count if worker_count > 0 else 0
    )

    avg_production_rate = (
        total_units / (total_working_time / 3600)
        if total_working_time > 0 else 0
    )

    return {
        "total_productive_minutes": round(total_working_time / 60, 2),
        "total_units_produced": total_units,
        "average_utilization_percent": round(avg_utilization, 2),
        "average_production_rate_per_hour": round(avg_production_rate, 2)
    }


