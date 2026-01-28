# AI Worker Productivity Dashboard (Full-Stack MLOps Project)

## 📌 Overview
The **AI Worker Productivity Dashboard** is a full-stack MLOps-oriented application designed to ingest event-level factory data and compute meaningful productivity metrics at **worker**, **workstation**, and **factory** levels.

The project demonstrates **end-to-end system design**, covering:
- Backend API development
- Metrics computation
- Frontend dashboard visualization
- Containerization using Docker
- Service orchestration using Docker Compose

This project was built as part of a **Full-Stack MLOps Engineer Technical Assessment**.

---

## 🏗️ System Architecture

```
Frontend (React)
   │
   │  REST API calls
   ▼
Backend (FastAPI)
   │
   │  ORM (SQLAlchemy)
   ▼
SQLite Database
```

- **Frontend** displays real-time productivity insights
- **Backend** ingests events and computes metrics
- **Docker Compose** runs the entire stack with a single command

---

## 🧰 Tech Stack

### Backend
- Python 3
- FastAPI
- SQLAlchemy
- SQLite

### Frontend
- React
- JavaScript
- HTML / CSS

### MLOps / DevOps
- Docker
- Docker Compose

---

## 📂 Project Structure

```
mlops-productivity-dashboard/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── metrics.py
│   ├── db.py
│   ├── dependencies.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 How to Run the Project (Docker)

### Prerequisites
- Docker Desktop installed and running
- WSL 2 enabled (Windows)

### Steps

```bash
docker compose up --build
```

### Access the Application

- **Frontend Dashboard:** http://localhost:3000
- **Backend API Docs:** http://localhost:8000/docs

---

## 📥 API Endpoints

### Event Ingestion
```
POST /events
```

### Metrics
```
GET /metrics/workers
GET /metrics/workstations
GET /metrics/factory
```

---

## 🗄️ Database Schema

**events table**
| Field | Description |
|-----|------------|
| timestamp | Event time |
| entity_type | worker/workstation |
| entity_id | W1, S1, etc |
| event_type | working/idle |
| duration_minutes | Activity duration |
| units_produced | Output |
| confidence | Data reliability |

---

## 📐 Metric Definitions

- **Utilization (%)** = working / total time × 100
- **Units/hour** = units / (minutes / 60)
- **Throughput/hour** = station units / (occupied / 60)

---

## ⚖️ Assumptions & Tradeoffs

- SQLite chosen for simplicity
- Raw events stored for recomputation
- No auth (out of scope)
- Metrics computed dynamically

---

## 📊 Dashboard Features

### Factory Summary
- Total productive minutes
- Total units produced
- Average utilization
- Average production rate

### Worker Metrics
- Working time
- Idle time
- Utilization percentage
- Units produced
- Units per hour

### Workstation Metrics
- Occupied time
- Units produced
- Throughput per hour

---

## 🐳 Dockerization

- Backend and frontend are containerized separately
- Services orchestrated using `docker-compose.yml`
- Entire application runs using a single command

---

## 🌍 Deployment

> The application can be deployed on cloud platforms such as:
- Backend: Railway / Render
- Frontend: Vercel

## 🌍 Deployment Links

Frontend: https://mlops-productivity-dashboard.vercel.app/  
Backend: https://mlops-backend-kcco.onrender.com/docs  

---

---
---

## 🧠 MLOps & System Design Considerations

### 1️⃣ Handling Intermittent Connectivity
In real-world factory environments, edge devices (such as CCTV systems or IoT sensors) may experience intermittent network connectivity.

**Approach:**
- Events are generated and buffered at the edge.
- Once connectivity is restored, buffered events are sent in batches to the backend.
- The backend processes events in an idempotent manner to avoid duplication issues.
- Temporary network failures do not affect metric correctness because metrics are derived from persisted events.

---

### 2️⃣ Handling Duplicate Events
Duplicate events can occur due to retries, network instability, or edge-side buffering.

**Approach:**
- Each event is associated with a unique combination of:
  - entity_id
  - event_type
  - timestamp
- Before inserting a new event, the backend checks whether an identical event already exists.
- Duplicate events are ignored to prevent metric inflation.
- This ensures idempotent event ingestion.

---

### 3️⃣ Handling Out-of-Order Events
Events may arrive out of chronological order due to network delays or batching.

**Approach:**
- All events are stored with their original timestamps.
- Metrics are computed using timestamp-based ordering instead of arrival order.
- SQL queries aggregate durations based on event timestamps, ensuring correctness even if events arrive late.
- This design guarantees accurate metrics regardless of ingestion order.

---

### 4️⃣ Model Versioning, Drift Detection & Scaling Strategy

#### Model Versioning
- Each deployed ML model would be tagged with a version (e.g., v1.0, v1.1).
- Event records can store the model_version used to generate predictions.
- This allows historical comparison and rollback if needed.

#### Model Drift Detection
- Drift can be detected by monitoring changes in:
  - Utilization patterns
  - Production rate distributions
  - Confidence scores over time
- Statistical techniques such as distribution comparison or threshold alerts can be applied.

#### Retraining Triggers
- Retraining can be triggered when:
  - Drift crosses a predefined threshold
  - Performance metrics degrade
  - New labeled data becomes available
- Retraining pipelines can be automated using CI/CD or scheduled jobs.

#### Scaling to Multiple Factories
- Replace SQLite with PostgreSQL or a distributed database.
- Deploy backend services using container orchestration (Kubernetes).
- Use message queues (Kafka / RabbitMQ) for event ingestion.
- Each factory can be treated as a separate tenant with logical isolation.

---



## 👤 Author

**Vishal Singh Kushwaha**
singhkushwahavishal344@gmail.com
B.Tech CSE (AI & ML)  
Aspiring Full-Stack MLOps Engineer

---

## ✅ Assessment Notes

- End-to-end working system
- Dockerized full stack
- Clean API design
- Metrics-driven architecture
- Ready for production deployment
- Deployed

---

⭐ *This project demonstrates practical Full-Stack MLOps skills including system design, backend engineering, frontend integration, and DevOps best practices.*

