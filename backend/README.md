<p align="center">
  <img src="../assets/Nexora’s_Stock_Prediction_Tool.png" alt="Nexora Stock Prediction Tool" width="700">
</p>

# Nexora Backend

The backend provides the application/API layer for **Nexora --- AI Stock
Decision Support & Prediction Tool**.

## Technology Stack

- **Language:** Python
- **API framework:** FastAPI
- **Validation:** Pydantic
- **API documentation:** OpenAPI + Swagger UI + ReDoc
- **Logging:** Python `logging`
- **Configuration:** Environment variables + `.env` + `python-dotenv`

## Current Foundation

The backend currently contains the application foundation, API package
structure, schemas/models/services package structure, and automated tests.

Current structure:

```text
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
```

## Setup

From the repository root:

```bat
cd backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the Backend

The backend is run from the `backend` directory with:

```bash
uvicorn app.main:app --reload
```

## Checks

Compile the application:

```bash
python -m compileall app
```

Run automated tests:

```bash
set PYTHONPATH=.
pytest
```

The same backend compilation and pytest checks are executed by the
GitHub Actions CI workflow.

## Configuration

Environment-specific configuration uses environment variables and the
repository `.env.example` template.

Actual secrets must never be committed to Git.

## API Documentation

FastAPI provides the project's OpenAPI-based API documentation through
Swagger UI and ReDoc.

Detailed endpoint and service documentation will be expanded as the API
surface is implemented.

## Documentation Scope

As backend implementation progresses, this document will be expanded to
cover:

- API endpoints
- Request/response schemas
- Services
- Validation
- Error handling
- ML integration
- Testing
- Deployment

The root `README.md` and Master Checklist remain the project-level sources
of truth for overall project status and scope.

## Document Status

**Component:** Backend  
**Project:** Nexora --- AI Stock Decision Support & Prediction Tool  
**Status:** Foundation initialized
