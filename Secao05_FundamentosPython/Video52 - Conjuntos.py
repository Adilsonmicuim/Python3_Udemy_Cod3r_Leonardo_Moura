# Conjunto: É delimitado por chaves só tem valores, 1- não é indexado, 2- não garante ordenação, 3- não aceita repetição.
a = {1, 2, 3}
type(a)
# a[0]
a = set('coddddd3r')
print(a)
print('3' in a, 4 not in a)
{1, 2, 3} == {3, 2, 1, 3} # Resposta: True - O conjunto possui os mesmos elementos.

# operacoes
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2) # Resposta: {1, 2, 3}
c1.intersection(c2) # Resposta {2}
#c1.update(c2)
c1

c2 <= c1 # C2 é subconjunto de C1
c1 >= c2 # C1 é super conjunto de C2

{1, 2, 3} - {2}
c1 - c2
c1 -= {2} # Atribuição subtrativa
c1
