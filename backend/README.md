<p align="center">
  <img src="../assets/Nexora’s_Stock_Prediction_Tool.png" alt="Nexora Stock Prediction Tool" width="700">
</p>

# Nexora Backend

The backend provides the application and API layer for **Nexora — AI Stock Decision Support & Prediction Tool**.

It is responsible for exposing backend services, validating API data, coordinating application logic, and providing the foundation for future market-data, ML prediction, risk-assessment, and decision-engine integrations.

## Purpose

The backend will serve as the central application layer between the Nexora frontend and the project's data-processing, ML, risk, and decision-support components.

The current repository contains the initial FastAPI foundation. Market-data providers, prediction models, decision logic, and production API endpoints will be integrated incrementally.

## Technology Stack

- **Language:** Python
- **API framework:** FastAPI
- **Validation:** Pydantic
- **API documentation:** OpenAPI + Swagger UI + ReDoc
- **Logging:** Python `logging`
- **Configuration:** Environment variables + `.env` + `python-dotenv`
- **Testing:** pytest

## Current Foundation

The backend currently contains the application foundation, API package structure, schemas/models/services package structure, and automated tests.

Current structure:

```text
backend/
├── .venv/                 # local virtual environment; ignored by Git
├── app/
│   ├── __init__.py
│   ├── api/
│   │   └── __init__.py
│   ├── core/
│   │   └── __init__.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```

## Setup

From the repository root:

```bat
cd backend
python -m venv .venv
.venv\Scriptsctivate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For an existing environment:

```bat
cd backend
.venv\Scriptsctivate
pip install -r requirements.txt
```

## Environment Variables

Backend configuration uses environment variables and the repository-level `.env.example` template.

A local `.env` file may be used for development-specific configuration.

Example:

```env
APP_ENV=development
```

As external market-data providers and other integrations are added, their credentials and configuration values should be documented through `.env.example`.

**Never commit real secrets, API keys, tokens, or credentials to Git.**

## Run Commands

The default backend development command is:

```bash
uvicorn app.main:app --reload
```

Run it from the `backend` directory:

```bat
cd backend
.venv\Scriptsctivate
uvicorn app.main:app --reload
```

The backend development server is normally available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive documentation is available through Swagger UI at:

```text
http://127.0.0.1:8000/docs
```

ReDoc is available at:

```text
http://127.0.0.1:8000/redoc
```

## API Overview

The backend uses FastAPI to expose HTTP APIs.

The intended high-level application flow is:

```text
Frontend
   ↓
FastAPI Backend
   ↓
Market Data / Data Processing
   ↓
ML Prediction
   ↓
Risk Assessment
   ↓
Decision Engine
   ↓
Prediction / Decision Result
   ↓
Frontend
```

The current backend is still at the foundation stage, so the final application API surface is not yet implemented.

## Endpoint List

The current foundation does not yet define the final stock-prediction API endpoints.

As endpoints are implemented, they will be documented using this structure:

| Method | Endpoint | Purpose | Status |
|---|---|---|---|
| GET | `/` | Backend health/basic application response | Foundation |
| Application-specific endpoints | TBD | Market data, prediction, risk and decision workflows | Planned |

> Endpoint names above are not being treated as implemented prediction endpoints unless they exist in the application code.

FastAPI automatically exposes implemented endpoints through the OpenAPI schema and Swagger UI.

## Request / Response Examples

The current foundation does not yet contain finalized business-domain request/response schemas.

Once application endpoints are implemented, examples will follow this structure:

### Example request

```json
{
  "symbol": "RELIANCE",
  "horizon": "1d"
}
```

### Example response

```json
{
  "symbol": "RELIANCE",
  "prediction": "TBD",
  "confidence": null,
  "decision": "TBD"
}
```

> The example above is illustrative only. It is not an implemented Nexora prediction contract.

Actual request and response examples will be updated when the corresponding Pydantic schemas and API endpoints are implemented.

## Error Handling

Backend error handling will use FastAPI's HTTP exception and validation mechanisms.

The API should provide:

- Appropriate HTTP status codes.
- Clear validation errors for invalid input.
- Consistent error response structures.
- Safe error messages that do not expose secrets or internal implementation details.
- Proper handling of external provider failures when market-data integrations are added.
- Logging of useful diagnostic information without logging sensitive credentials.

Detailed domain-specific error handling will be documented as the API surface grows.

## Logging

The project has selected Python's built-in `logging` module for backend logging.

Logging should be used for:

- Application lifecycle events.
- API/service failures.
- External provider failures.
- Validation or processing failures.
- Important diagnostic information during development.

Sensitive information such as API keys, access tokens, passwords, and other secrets must never be written to logs.

The logging configuration will be expanded as the backend moves beyond its foundation stage.

## Testing

Backend automated tests use **pytest**.

Run tests from the `backend` directory:

```bat
set PYTHONPATH=.
pytest
```

Compile the application before or alongside testing:

```bash
python -m compileall app
```

The same backend compilation and pytest checks are executed by the GitHub Actions CI workflow.

Current backend tests cover the foundation stage. Additional tests will be added for API endpoints, validation, services, market-data integration, ML integration, and decision logic as those components are implemented.

## Model Integration

The backend is intended to integrate with the separate Nexora ML layer.

The planned relationship is:

```text
Backend/API
    ↓
Data validation
    ↓
Data processing
    ↓
ML model / prediction pipeline
    ↓
Prediction output
    ↓
Risk / decision layer
    ↓
API response
```

The current backend foundation does **not** yet contain a completed production ML model integration.

Model-specific libraries, model artifacts, inference pipelines, and model-versioning decisions remain part of the later ML implementation work.

## Security

Security requirements for the backend include:

- Never commit secrets or credentials.
- Keep `.env` files out of Git.
- Use `.env.example` only for documenting required configuration.
- Validate incoming API data with Pydantic.
- Avoid exposing internal exceptions or sensitive implementation details in API responses.
- Do not log API keys, tokens, passwords, or other secrets.
- Validate and constrain external input before processing.
- Apply appropriate authentication/authorization when protected functionality is introduced.
- Protect external provider credentials through environment configuration.
- Review CORS configuration before deployment.
- Use HTTPS in deployed environments.
- Keep dependencies maintained and review security advisories.

Production security controls will be finalized when deployment and external API integrations are introduced.

## API Documentation

FastAPI provides OpenAPI-based API documentation through:

- Swagger UI: `/docs`
- ReDoc: `/redoc`
- OpenAPI schema: `/openapi.json`

Detailed endpoint and service documentation will expand as the API surface is implemented.

## Development Quality Checks

Before committing backend changes, run:

```bat
cd backend
.venv\Scriptsctivate
python -m compileall app
set PYTHONPATH=.
pytest
```

These checks are also part of the project's GitHub Actions CI pipeline.

## Documentation Status

**Component:** Backend  
**Project:** Nexora — AI Stock Decision Support & Prediction Tool  
**Status:** Foundation initialized; documentation prepared for the current implementation stage.

The root `README.md` and Master Checklist remain the project-level sources of truth for overall project status and scope.
