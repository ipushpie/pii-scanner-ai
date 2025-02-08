from fastapi import FastAPI
from app.api.routes import document_routes

app = FastAPI(
    title="PII Scanner API",
    description="API for scanning documents for Personally Identifiable Information",
    version="1.0.0"
)

# Include routers
app.include_router(document_routes.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

