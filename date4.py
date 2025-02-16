from datetime import datetime
dt1 = datetime.strptime(input(),"%Y-%m-%d")
dt2 = datetime.strptime(input(),"%Y-%m-%d")
print("Dif = ",abs((dt2 - dt1).total_seconds()))