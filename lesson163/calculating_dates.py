# datetime.timedelta and dateutil.relativedelta (calculating dates)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
start_date = datetime.strptime('20/04/1987 09:30:30', fmt)
end_date = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(end_date, start_date)
print(delta.days, delta.years)
# print(end_date - delta)
# print(end_date)
# print(end_date + relativedelta(seconds=60, minutes=10))

# delta = end_date - start_date
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(end_date > start_date)
# print(end_date < start_date)
# print(end_date == start_date)
