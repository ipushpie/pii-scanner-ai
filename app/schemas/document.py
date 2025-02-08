from pydantic import BaseModel
from app.schemas.base import BaseResponse

class ScanData(BaseModel):
    filename: str
    detected_pii: list  # You can define this more specifically based on your needs

class ScanResponse(BaseResponse[ScanData]):
    pass 