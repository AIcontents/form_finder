import pytest
from app import match_template, build_response

templates = [
    {
        "name": "Form A",
        "email": "email",
        "tel": "phone"
    },
    {
        "name": "Order",
        "customer_name": "text",
        "order_date": "date"
    }
]
def test_match_form_a():
    query = {"email": "test@test.com", "tel": "+7 123 456 78 90"}
    assert match_template(query, templates) == "Form A"

def test_match_order():
    query = {"customer_name": "Ivan", "order_date": "2025-06-16"}
    assert match_template(query, templates) == "Order"

def test_match_with_extra_fields():
    query = {
        "email": "test@test.com",
        "tel": "+7 123 456 78 90",
        "extra": "some value"
    }
    assert match_template(query, templates) == "Form A"
    
def test_no_match():
    query = {"tel": "not a phone", "customer_name": "Ivan"}
    assert match_template(query, templates) is None

def test_build_response_date():
    query = {"birth": "2024-01-01"}
    assert build_response(query) == {"birth": "date"}

def test_build_response_mixed():
    query = {"user": "hello", "mail": "aaa@bbb.ru"}
    assert build_response(query) == {"user": "text", "mail": "email"}
