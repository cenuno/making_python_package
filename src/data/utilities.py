"""
Create function to test if today is my birthday
"""
from datetime import datetime


def is_bday(bday_date: str) -> bool:
    """Tests if today is your birthday"""
    output = datetime.today().strftime("%Y-%m-%d") == bday_date
    if output:
        print("Cheers! Today is your birthday")
    else:
        print("While today is not your birthday, you should still celebrate!")

