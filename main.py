from application.salary import calculate_salary
from application.db.people import get_employees

import datetime

if __name__ == '__main__':
    calculate_salary(70580)
    get_employees('Мария', 'Семен', 'Денис')
print(datetime.date.today())