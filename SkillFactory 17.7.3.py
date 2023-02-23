money = float(input("Сумма на депозит:"))


per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}


TKB = float((per_cent['ТКБ']) * (money/100))
CKB = float((per_cent['СКБ']) * (money/100))
VTB = float((per_cent['ВТБ']) * (money/100))
SBER = float((per_cent['СБЕР']) * (money/100))


deposit = [TKB, CKB, VTB, SBER]

print("Прибыль по процентам в каждом из банков =", deposit)


print("Максимальня прибыль за год:", max(deposit))