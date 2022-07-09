from datetime import datetime
from datetime import date

# print(date.today())

now = datetime.now()
print(now)

print(now.strftime("%d-%m-%Y %H:%M:%S")) #number month
print(now.strftime("%d-%B-%Y %H:%M:%S")) #full month
print(now.strftime("%d-%b-%Y %H:%M:%S")) #short month

