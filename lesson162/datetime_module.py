# Creating dates with the datetime module
# datetime(year, month, day)
# datetime(year, month, day, hours, minutes, seconds)
# datetime.strptime('DATE', 'FORMAT')
# datetime.now()
# https://en.wikipedia.org/wiki/Unix_time
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# For timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Installing pytz
# pip install pytz types-pytz
from datetime import datetime

# from pytz import timezone

data = datetime.now()
print(data.timestamp())  # This is stored in the database
print(datetime.fromtimestamp(1670849077))
# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
