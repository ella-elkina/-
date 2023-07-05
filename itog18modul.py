k = int(input("Введите количество приобретаемых билетов: "))
s = 0
for i in range(k):
    age=int(input("введите возраст: "))
    if 18<=age<=24:
        s+=990
    else:
        if age >=25:
            s+=1390
if k>3:
    s = s * 0.9

print("Стоимость билетов: ", s)