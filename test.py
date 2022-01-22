import datetime

a = datetime.datetime.now()
b = 0
for i in range(0,999999):
    b = b + 1

b = datetime.datetime.now()

print(b-a)

