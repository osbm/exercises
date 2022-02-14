from datetime import datetime as dt

date = "08-12-2021"

date_dt = dt.strptime(date, "%d-%m-%Y")

print(date_dt)