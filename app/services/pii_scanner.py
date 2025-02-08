from app.models.document import ScannedDocument
from app.database import get_db
from sqlalchemy.orm import Session
from app.services.pii_patterns import scan_for_pii  # Import the PII scanning function
import json  # Import json module

class PIIScanner:
    def __init__(self):
        # TODO: Initialize PII detection models or patterns
        pass

    async def scan_document(self, file_content: bytes, filename: str, db: Session) -> dict:
        """
        Scan document content for PII and save to the database
        """
        text = file_content.decode('utf-8')  # Decode bytes to string
        detected_pii = scan_for_pii(text)  # Scan for PII using regex patterns

        # Save to database
        scanned_doc = ScannedDocument(filename=filename, detected_pii=json.dumps(detected_pii))  # Convert list to JSON string
        db.add(scanned_doc)
        db.commit()
        db.refresh(scanned_doc)

        return {"detected_pii": detected_pii}  # Ensure this is a list 