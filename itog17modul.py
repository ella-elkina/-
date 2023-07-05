per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money = int(input('Введите сумму денег, которую планируете положить: '))

for i in per_cent.values():
    chet= i * money / 100
    deposit.append(chet)

max_money = max(deposit)
otvet = 'Максимальная сумма, которую вы можете заработать — %d' %max_money
print(deposit)
print(otvet)
