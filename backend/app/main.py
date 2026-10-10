from fastapi import FastAPI

app = FastAPI(
    title="Nexora Stock Prediction API",
    description="Backend API for the Nexora AI Stock Decision Support & Prediction Tool.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Nexora Stock Prediction API is running.",
        "status": "healthy",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }