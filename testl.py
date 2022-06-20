import datetime
from random import randint, seed



# generate some integers
for _ in range(10):
	day = randint(1, 30)
	print(day)


for _ in range(10):
	year = randint(2000, 2010)
	print(year)

for _ in range(10):
	year = randint(1, 12)
	print(year)


month_num = "3"

full_month_name = datetime.datetime.strptime(month_num, "%m").strftime("%B")
print(full_month_name)