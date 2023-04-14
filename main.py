

import datetime
from application import salary as salary
from application.db import people as people


if __name__ == '__main__':
    date = datetime.date.today()
    print(date)
    salary.calculate_salary("Test")
    people.get_employees("Test 2")
