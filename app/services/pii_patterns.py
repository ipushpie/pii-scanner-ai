import re

# Define regex patterns for different types of PII
PII_PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone": r"\+?\d[\d -]{8,12}\d",  # Matches international phone numbers
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",  # Matches SSN format
    "credit_card": r"\b(?:\d{4}[- ]?){3}\d{4}\b",  # Matches credit card numbers
    "address": r"\d{1,5}\s\w+(\s\w+)*,\s\w+,\s\w{2}\s\d{5}",  # Matches US addresses
}

def scan_for_pii(text: str) -> list:
    detected_pii = []
    
    for pii_type, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        detected_pii.extend(matches)  # Add matches to the list
            
    return detected_pii 