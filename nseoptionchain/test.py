from datetime import *
import os

now_time = datetime.now()
cutoff_time = "15:40:00"  # we want to stop pulling option chain after this time
today_date = now_time.strftime("%d/%m/%Y")
cutoff_datetime_str = today_date+" "+cutoff_time
cutoff_datetime = datetime.strptime(cutoff_datetime_str, "%d/%m/%Y %H:%M:%S")
print(cutoff_datetime)

if now_time > cutoff_datetime:
    print("time is greater than 15:40")
else:
    print("time is less than 15:40")

print(os.getcwd())
