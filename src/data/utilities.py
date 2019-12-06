"""
Create function to test if today is my birthday
"""
from datetime import datetime


def is_bday(bday_date: str) -> bool:
    """Tests if today is your birthday"""
    return datetime.today().strftime("%Y-%m-%d")) == bday_date

