import pandas as pd
from datetime import datetime,timedelta

start='20041201'
end='20041205'

date_range=pd.date_range(start=start, end=end)
print(date_range)

for date in date_range:
    print(date)