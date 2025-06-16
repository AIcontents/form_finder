import pytest
from app import match_template, build_response

templates = [
    {"name": "Form A", "email": "email", "tel": "phone"},
    {"name": "Order", "name": "text", "date": "date"}
]

def test_match_found():
    query = {"email": "test@test.com", "tel": "+7 123 456 78 90"}
    assert match_template(query, templates) == "Form A"

def test_no_match_returns_typing():
    query = {"unknown": "2025-06-16"}
    assert build_response(query) == {"unknown": "date"}
