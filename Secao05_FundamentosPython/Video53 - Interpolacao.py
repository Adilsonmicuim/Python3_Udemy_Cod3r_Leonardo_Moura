# %%
from string import Template

nome, idade = 'Ana', 30.98

print('Nome: %s Idade: %d' % (nome, idade))  # mais antiga (%s: elementos tipo string, %d: elementos tipo int).
# print('Nome: %s Idade: %f' % (nome, idade))  # mais antiga
# print('Nome: %s Idade: %.2f' % (nome, idade))  # mais antiga
print('Nome: {0} Idade: {1}'.format(nome, idade))  # python < 3.6
print(f'Nome: {nome} Idade: {idade}')  # python >= 3.6  - f': String


s = Template('Nome: $nom Idade: $idade')
print(s.substitute(nom=nome, idade=idade))
