from fastapi import FastAPI
from app.api.routes import document_routes
from app.database import engine, Base  # Import the engine and Base

app = FastAPI(
    title="PII Scanner API",
    description="API for scanning documents for Personally Identifiable Information",
    version="1.0.0"
)

# Create the database tables if they do not exist
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(document_routes.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

