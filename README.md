<p align="center">
  <img src="assets/Nexora’s_Stock_Prediction_Tool.png" alt="Nexora Stock Prediction Tool" width="700">
</p>

# Nexora --- AI Stock Decision Support & Prediction Tool

> Analyze market information. Understand risk. Make informed decisions.

## Overview

Nexora is an AI-assisted stock decision-support and prediction platform
designed to transform relevant market information into structured,
understandable analytical results.

The initial scope focuses on the **Indian equity market ---
NSE/BSE-listed stocks** and supports prediction horizons of **1 trading
day** and **1 trading week**.

Nexora combines market-data retrieval, validation, processing,
prediction, risk assessment, and decision-support logic into one product
workflow.

> **Important:** Nexora provides decision support and predictions. It
> does not guarantee returns and is not a substitute for professional
> financial advice.

## Problem

Individual investors and other users can find it difficult to combine
fragmented market information, analytical signals, predictive outputs,
and risk considerations into one understandable view.

Nexora addresses this by providing a structured workflow that turns
relevant market information into a prediction, risk-aware
recommendation, and explanation.

## Aim

The aim of Nexora is to build a maintainable AI-assisted platform that
helps users analyze supported stocks and understand prediction-driven
decision-support outcomes while clearly communicating uncertainty and
risk.

## Objectives

-   Provide a structured stock-analysis workflow.
-   Retrieve and validate relevant market data.
-   Process data consistently for prediction.
-   Generate predictions for supported horizons.
-   Assess relevant risk and confidence.
-   Generate transparent decision-support outcomes.
-   Explain why a recommendation was generated.
-   Handle insufficient, stale, or unreliable data safely.
-   Provide a maintainable foundation for additional ML models and
    capabilities.
-   Apply software-engineering practices including Git, CI, testing,
    documentation, and incremental Agile development.

## Features

### Core Analysis

-   Stock search and selection.
-   1-day and 1-week analysis/prediction horizons.
-   Market-data retrieval and validation.
-   Data processing and feature preparation.
-   Machine-learning prediction.
-   Risk assessment.
-   Confidence information where supported.
-   Decision-support outcomes:
    -   **BUY**
    -   **SELL**
    -   **WATCH**
    -   **HOLD**
    -   **NO SIGNAL**
-   Recommendation explanation.
-   Result visualization.
-   Loading, error, no-data, and stale-data handling.

### User Features

-   Lightweight analysis preferences.
-   Optional risk preference where supported.
-   Watchlist.
-   Prediction history.

## High-Level Architecture

``` text
                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Frontend       │
                    │ React + TypeScript  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Backend / API    │
                    │       FastAPI       │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      Market Data        Data Processing    Decision / Risk
       Provider             & Validation        Layer
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   ML Prediction     │
                    │      Layer          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Prediction + Risk +  │
                    │ Recommendation +     │
                    │ Explanation          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Frontend Result UI  │
                    └─────────────────────┘
```

The architecture is intentionally modular so that additional models,
data providers, storage, and deployment capabilities can be introduced
as the project evolves.

## Repository Structure

``` text
nexora_stock_prediction/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── assets/
│   ├── diagrams/
│   ├── Nexora’s_Stock_Prediction_Tool.png
│   ├── 0.1_Definitions.md
│   ├── 0.2_Agile_Setup.md
│   ├── 0.3_Git_Initialization.md
│   ├── 0.4_CI_CD_Foundation.md
│   ├── 1.1_Business_Requirements.md
│   ├── 1.2_Functional_Requirements.md
│   ├── 1.3_Non_Functional_Requirements.md
│   ├── 1.4_User_Stories.md
│   ├── 2.2_Technology_Stack.md
│   └── Nexora_Stock_Prediction_Master_Checklist.md
│
├── frontend/
│   └── README.md
│
├── backend/
│   ├── app/
│   ├── tests/
│   ├── requirements.txt
│   └── README.md
│
├── ml/
│   └── README.md
│
├── docs/
├── tests/
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

The structure may evolve as implementation progresses. Changes should
remain deliberate and documented.

## Setup Overview

### Prerequisites

-   Git
-   GitHub access
-   Node.js and npm for the frontend
-   Python for backend and ML development
-   A suitable development environment such as VS Code

### Clone

``` bash
git clone https://github.com/annnuspeaks/Stock_Prediction.git
cd Stock_Prediction
```

### Frontend

``` bash
cd frontend
npm install
npm run dev
```

Production build:

``` bash
npm run build
```

Lint:

``` bash
npm run lint
```

### Backend

``` bat
cd backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The backend application is run from the `backend` directory with:

``` bash
uvicorn app.main:app --reload
```

### ML Environment

The ML workspace uses a separate Python environment:

``` text
ml/.venv
```

The Jupyter kernel is configured as:

``` text
Nexora ML
```

ML/data-processing and model dependencies will be added as the
corresponding ML phases are implemented.

### Configuration

Environment-specific configuration should use environment variables. The
repository provides:

``` text
.env.example
```

Actual secrets must never be committed to Git.

## Frontend Documentation

The frontend contains the user-facing Nexora application.

See:

`frontend/README.md`

The dedicated frontend documentation will cover setup, development,
build, project structure, routes, components, API communication, UI
conventions, and testing.

## Backend Documentation

The backend provides the application/API layer and coordinates
validation, processing, prediction, risk, and decision-support services.

See:

`backend/README.md`

The dedicated backend documentation will cover setup, configuration, API
endpoints, services, validation, error handling, ML integration,
testing, and deployment.

## ML / Data Documentation

The ML/data layer is responsible for data preparation, exploration,
feature engineering, model development, evaluation, and prediction
artifacts.

See:

`ml/README.md`

Detailed ML documentation will be expanded as the model-development
phases are implemented.

## Git Workflow

The `main` branch represents the stable project state.

Preferred workflow:

``` text
main
  ↓
Feature / Work
  ↓
Development
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
CI Checks
  ↓
Review
  ↓
Merge
```

Use meaningful commits and keep changes focused. The Master Checklist
remains the project source of truth:

``` text
assets/Nexora_Stock_Prediction_Master_Checklist.md
```

## CI/CD Overview

### Continuous Integration

Nexora uses **GitHub Actions**.

The CI workflow runs on:

-   Pushes to `main`
-   Pull requests targeting `main`

Current pipeline:

``` text
Code Change
    ↓
Push / Pull Request
    ↓
GitHub Actions
    ↓
Verify Project Structure
    ↓
Install Frontend Dependencies
    ↓
Frontend Checks
  ├── ESLint
  └── Production Build
    ↓
Install Backend Dependencies
    ↓
Backend Checks
  └── Python Compilation
    ↓
Automated Tests
  └── Pytest
    ↓
PASS / FAIL
```

The pipeline has also been intentionally tested with a controlled
failure to verify that CI correctly detects failures. The failure was
removed and the pipeline was successfully rerun.

### Continuous Delivery / Deployment

CD is **not implemented yet** and is intentionally deferred until the
application has a stable deployable build and the deployment target,
environments, configuration, deployment process, and rollback process
have been defined.

Current state:

```text
CI → Implemented
CD → Deferred
```

## Testing Overview

Testing is performed incrementally throughout development.

Current automated checks include:

-   Frontend ESLint.
-   Frontend production build.
-   Backend Python compilation.
-   Backend automated tests with pytest.

These checks currently run through the GitHub Actions CI pipeline.

Planned/expanding testing areas include:

-   Unit testing.
-   API testing.
-   Integration testing.
-   Frontend testing.
-   Backend testing.
-   ML/pipeline validation.
-   End-to-end testing.
-   Regression testing.
-   Performance testing.
-   Security checks.

Tests should be integrated into CI wherever practical.

## Development Methodology

Nexora follows an Agile SDLC with lightweight, practical iterations:

``` text
Planning
   ↓
Development
   ↓
Testing
   ↓
Documentation
   ↓
Review / Demo
   ↓
Retrospective
   ↓
Backlog Refinement
```

The Master Checklist is the master backlog and source of truth for
project progress.

## Limitations

Nexora's outputs depend on factors including:

-   Market-data availability and quality.
-   Data freshness.
-   Historical data coverage.
-   Prediction-model performance.
-   Feature quality.
-   Model assumptions.
-   Market conditions.
-   Prediction horizon.
-   Uncertainty in future market behavior.

A model that performs well on historical data does not guarantee
equivalent performance in future markets.

The system may intentionally return **NO SIGNAL** when evidence does not
meet defined data-quality, confidence, or risk requirements.

## Disclaimer

Nexora is a **software-based stock decision-support and prediction
tool**.

Its outputs are estimates generated from available data, analytical
methods, and prediction models. They are **not guarantees of future
stock performance, returns, or accuracy**.

Nexora is not a substitute for professional financial advice. Users
remain responsible for their own investment decisions.

The initial project does not provide automatic trading. Any future
real-world financial deployment or automated trading capability would
require separate review of applicable legal, regulatory, compliance,
security, and risk requirements.

## Current Project Status

| Area | Status |
|---|---|
| Project Repository | 🟢 Initialized |
| Git | 🟢 Initialized |
| GitHub | 🟢 Connected |
| Master Checklist | 🟢 Added |
| Initial CI | 🟢 Implemented |
| Phase 1 Requirements | 🟢 Completed |
| Root Documentation (1.5) | 🟢 Completed |
| Frontend Foundation | 🟢 Initialized |
| Backend Foundation | 🟢 Initialized |
| ML Python Environment | 🟢 Initialized |
| Architecture (2.1) | 🟡 In Progress |
| ML/Data Libraries | ⬜ To Be Decided |
| Deployment/CD | ⬜ Deferred |

## License

This project is licensed under the **MIT License**.

See `LICENSE` for details.

------------------------------------------------------------------------

**Nexora --- AI Stock Decision Support & Prediction Tool**
