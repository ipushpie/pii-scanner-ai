from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.services.pii_scanner import PIIScanner
from app.schemas.document import ScanResponse, ScanData
from app.database import get_db
from app.models.document import ScannedDocument
import json

router = APIRouter(prefix="/documents", tags=["Documents"])
pii_scanner = PIIScanner()

@router.post("/scan", response_model=ScanResponse)
async def scan_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    detected_pii = await pii_scanner.scan_document(file.file.read(), file.filename, db)
    response_data = ScanData(filename=file.filename, detected_pii=detected_pii["detected_pii"])
    
    return ScanResponse(success=True, message="Document scanned successfully", data=response_data)

@router.get("/scanned", response_model=list[ScanData])
async def get_scanned_documents(db: Session = Depends(get_db)):
    """
    Retrieve all scanned documents
    """
    scanned_docs = db.query(ScannedDocument).all()
    return [
        ScanData(filename=doc.filename, detected_pii=json.loads(doc.detected_pii) if doc.detected_pii else [])  # Convert JSON string back to list
        for doc in scanned_docs
    ]
