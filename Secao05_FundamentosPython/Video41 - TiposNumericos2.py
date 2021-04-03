# %%
import decimal
from decimal import Decimal, getcontext

# 1.1 + 2.2
Decimal(1) / Decimal(7)

getcontext().prec = 4 #Precisão de 4 casas decimais
Decimal(1) / Decimal(7)
Decimal.max(Decimal(1), Decimal(7))
dir(Decimal)

1.1 + 2.2
getcontext().prec = 10
Decimal(1.1) + Decimal(2.2)

dir(decimal) #Para funcionar precisa importar o decimal
dir()


a = 1.1
b = 2.2
soma = (Decimal(a)+Decimal(b))
print(soma)
print("+++++++++++++++++++++++")
getcontext().prec = 3
soma = (Decimal(a)+Decimal(b))
print(soma)