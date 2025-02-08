from sqlalchemy import Column, Integer, String, JSON
from app.database import Base  # Assuming you have a database setup file

class ScannedDocument(Base):
    __tablename__ = "scanned_documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    detected_pii = Column(JSON)  # Change this to JSON type 