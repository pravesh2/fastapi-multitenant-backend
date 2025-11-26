#  FastAPI Multi-Tenant Backend  
### _JWT Auth • Row-Level Isolation • PostgreSQL • Production-Ready Architecture_

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-RLS-important)
![License](https://img.shields.io/badge/Status-Production_Ready-success)

A clean, professional **multi-tenant backend** built with **FastAPI**, featuring:

-  **JWT-based authentication**
-  **Company-level isolation** (each company sees only its own data)
-  **PostgreSQL models**
-  **Modular and extendable FastAPI architecture**


---

# 📁 Project Structure

fastapi-multitenant-backend/
│── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── auth.py
│ ├── dependencies.py
│ └── routers/
│ ├── users.py
│ └── trips.py
│── requirements.txt
│── README.md


---

#  Architecture Diagram


      ┌────────────────────┐
      │   Client Apps      │
      └───────┬────────────┘
              │  JWT Token
      ┌───────▼────────────┐
      │     FastAPI        │
      │  (main.py API)     │
      └───────┬────────────┘
 Auth Token   │    CRUD
      ┌───────▼────────────┐
      │   Routers          │
      │ users / trips      │
      └───────┬────────────┘
              │  DB Ops
      ┌───────▼────────────┐
      │ SQLAlchemy Models  │
      └───────┬────────────┘
      │ RLS Applied via Tenant Token
      ┌───────▼────────────┐
      │   PostgreSQL       │
      └────────────────────┘


---

# ⚙️ Installation

### 1.  Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt

3. Run API
uvicorn app.main:app --reload


API Docs:
👉 http://127.0.0.1:8000/docs
