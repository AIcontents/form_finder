import re
from datetime import datetime

def is_date(val):
    try:
        datetime.strptime(val, "%d.%m.%Y")
        return True
    except ValueError:
        try:
            datetime.strptime(val, "%Y-%m-%d")
            return True
        except ValueError:
            return False

def is_phone(val):
    return bool(re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', val))

def is_email(val):
    return bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', val))

def detect_type(value):
    if is_date(value): return "date"
    if is_phone(value): return "phone"
    if is_email(value): return "email"
    return "text"
