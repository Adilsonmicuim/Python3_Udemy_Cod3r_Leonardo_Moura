# Video 41

from decimal import Decimal, getcontext

a = 1.1
b = 2.2
soma = (Decimal(a)+Decimal(b))
print(soma)

print("+++++++++++++++++++++++")
soma = (Decimal.max(Decimal(a), Decimal(b)))
print(soma)

print("+++++++++++++++++++++++")
Decimal.max(Decimal(a), Decimal(b))
soma = (Decimal(a)+Decimal(b))
print(soma)

print("+++++++++++++++++++++++")
getcontext().prec = 4
soma = (Decimal(a)+Decimal(b))
print(soma)

