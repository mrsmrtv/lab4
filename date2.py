from datetime import date, timedelta

print("Yesterday: ",date.today()-timedelta(days=1))
print("Today:",date.today())
print("Tommorow: ",date.today()+timedelta(days=1))
