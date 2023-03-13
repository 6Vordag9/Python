import calendar
result=0
typeYers=1
year = int(input('Введите год: '))
if calendar.isleap(year):
    print('Год високосный.')
    typeYers=1
else:
    print('Год не високосный.')
    typeYers=0
for i in range(1,13):
    if i==2:
        if typeYers==0:
            for j in range(1,29):
                x = [int(a) for a in str(j)]
                result+=sum(x)
        else:
             for j in range(1,30):
                x = [int(a) for a in str(j)]
                result+=sum(x)
    elif i in (4,6,9,11):
        for j in range(1,31):
            x = [int(a) for a in str(j)]
            result+=sum(x)
    else:
         for j in range(1,32):
            x = [int(a) for a in str(j)]
            result+=sum(x)
print(result)
        
    