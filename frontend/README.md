<p align="center">
  <img src="../assets/Nexora’s_Stock_Prediction_Tool.png" alt="Nexora Stock Prediction Tool" width="700">
</p>

# Nexora Frontend

The frontend is the user-facing application for **Nexora --- AI Stock
Decision Support & Prediction Tool**.

## Technology Stack

- **Framework/library:** React + TypeScript
- **Build tool:** Vite
- **Routing:** React Router
- **State management:** React Context + hooks initially
- **Charting:** Recharts
- **UI/icons:** Lucide React + custom Nexora UI components
- **Styling:** CSS Modules + global CSS/design tokens

## Current Foundation

The frontend has been initialized as a Vite React + TypeScript application.

Current quality checks:

```text
npm run lint
npm run build
```

These checks are also executed by the GitHub Actions CI workflow.

## Setup

From the repository root:

```bash
cd frontend
npm install
npm run dev
```

The Vite development server provides the local frontend development environment.

## Production Build

```bash
npm run build
```

## Lint

```bash
npm run lint
```

## Documentation Scope

As frontend implementation progresses, this document will be expanded to
cover:

- Application structure
- Routes
- Components
- API communication
- UI/UX conventions
- State management
- Charts and visualizations
- Testing
- Build and deployment considerations

The root `README.md` and Master Checklist remain the project-level sources
of truth for overall project status and scope.

## Document Status

**Component:** Frontend  
**Project:** Nexora --- AI Stock Decision Support & Prediction Tool  
**Status:** Foundation initialized
