<p align="center">
  <img src="../assets/Nexora’s_Stock_Prediction_Tool.png" alt="Nexora Stock Prediction Tool" width="700">
</p>

# Nexora Frontend

The frontend is the user-facing application for **Nexora — AI Stock Decision Support & Prediction Tool**.

It is responsible for presenting the Nexora interface, collecting user inputs, displaying analysis and prediction results, and communicating with the backend API as the application develops.

## Purpose

The frontend provides the web interface through which users will interact with Nexora's stock analysis and prediction capabilities.

The current repository contains the initial Vite + React + TypeScript foundation. Application-specific prediction workflows and backend integrations will be added incrementally.

## Technology Stack

- **Framework/library:** React + TypeScript
- **Build tool:** Vite
- **Routing:** React Router
- **State management:** React Context + hooks initially
- **Charting:** Recharts
- **UI/icons:** Lucide React + custom Nexora UI components
- **Styling:** CSS Modules + global CSS/design tokens

## Setup

From the repository root:

```bash
cd frontend
npm install
```

The project uses the Node.js/npm toolchain required by the Vite frontend.

## Environment Variables

Frontend environment-specific configuration should use Vite environment variables.

Vite exposes client-side variables through the `VITE_` prefix.

Example:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Do not commit real secrets or sensitive credentials. Use `.env.example` for documenting required configuration and keep local `.env` files ignored by Git.

> **Current status:** API-specific environment variables should only be added when the corresponding backend integration is implemented.

## Run Commands

Start the development server:

```bash
npm run dev
```

Run from:

```bash
cd frontend
```

The Vite development server provides the local frontend development environment.

## Build Commands

Create a production build:

```bash
npm run build
```

Preview the production build locally:

```bash
npm run preview
```

The production build is also validated by the GitHub Actions CI workflow.

## Test Commands

The current frontend foundation does not yet contain a dedicated frontend test suite.

Available quality checks are:

```bash
npm run lint
npm run build
```

These checks are also executed by the GitHub Actions CI workflow.

When frontend tests are introduced, their command and test framework will be documented here.

## Folder Structure

Current frontend structure:

```text
frontend/
├── .gitignore
├── README.md
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
├── public/
│   ├── favicon.svg
│   └── icons.svg
├── src/
│   ├── assets/
│   │   ├── hero.png
│   │   ├── react.svg
│   │   └── vite.svg
│   ├── App.css
│   ├── App.tsx
│   ├── index.css
│   └── main.tsx
├── tsconfig.app.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

Generated directories such as `node_modules/` and build output such as `dist/` are intentionally excluded from Git.

## Routes

The frontend has been initialized with React Router as the selected routing technology.

The current repository foundation does not yet define the final Nexora application route map. Routes will be documented here as application pages are implemented.

### Planned documentation format

| Route | Purpose | Status |
|---|---|---|
| `/` | Nexora entry/dashboard experience | To be finalized |
| Application-specific routes | Prediction, analysis, results, etc. | To be finalized |

> Route names above are documentation placeholders only and are not being treated as implemented routes until they exist in the application.

## Major Components

The current foundation includes:

- `src/main.tsx` — frontend application entry point.
- `src/App.tsx` — root application component.
- `src/App.css` — application-level styling.
- `src/index.css` — global styling foundation.
- `src/assets/` — frontend visual assets.

As Nexora features are implemented, reusable UI components, pages, layouts, charts, forms, and prediction-specific components will be documented here.

## API Integration

The frontend is intended to communicate with the Nexora FastAPI backend through HTTP API calls.

The intended application flow is:

```text
Frontend
   ↓
Backend/API
   ↓
Market Data
   ↓
Data Processing
   ↓
ML Prediction
   ↓
Risk / Decision Layer
   ↓
Prediction / Decision Result
   ↓
Frontend
```

The current frontend foundation does not yet contain a completed production API integration. API service modules, request/response schemas, loading states, error handling, and endpoint documentation will be added alongside the backend implementation.

## UI/UX Conventions

Nexora's frontend should follow these conventions:

- Keep interfaces clean, professional, and data-focused.
- Maintain consistent spacing, typography, sizing, and component behavior.
- Prefer reusable UI components over duplicated markup.
- Use clear visual hierarchy for stock data, predictions, risks, and decisions.
- Use charts only when they improve interpretation of data.
- Provide meaningful loading, empty, success, and error states as workflows are implemented.
- Keep interactions understandable for both technical and non-technical users.
- Maintain responsive behavior across supported screen sizes.
- Avoid visual decoration that reduces clarity or hides important financial information.

## Nexora Branding

The frontend follows the Nexora visual identity.

Branding principles include:

- Use the official Nexora logo/assets from `../assets/`.
- Maintain consistent Nexora typography and visual hierarchy.
- Use a professional, modern interface appropriate for an AI-powered financial analysis product.
- Keep prediction and decision-support information visually prominent without implying guaranteed financial outcomes.

The project logo used in this documentation is:

```text
Nexora — AI Stock Decision Support & Prediction Tool
```

## Development Quality Checks

Before committing frontend changes, run:

```bash
npm run lint
npm run build
```

Both checks are part of the initial GitHub Actions CI pipeline.

## Documentation Status

**Component:** Frontend  
**Project:** Nexora — AI Stock Decision Support & Prediction Tool  
**Status:** Foundation initialized; documentation prepared for the current implementation stage.

The root `README.md` and Master Checklist remain the project-level sources of truth for overall project status and scope.
