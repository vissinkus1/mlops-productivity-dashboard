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

(Deployment links provided during submission)

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

---

⭐ *This project demonstrates practical Full-Stack MLOps skills including system design, backend engineering, frontend integration, and DevOps best practices.*

