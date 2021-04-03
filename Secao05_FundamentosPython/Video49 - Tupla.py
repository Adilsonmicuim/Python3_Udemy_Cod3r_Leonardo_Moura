# %%
tupla = tuple()
tupla = ()
type(tupla)
dir(tupla)
# help(tuple)
type(tupla)

tupla = ('um')
type(tupla)  # Resultado: <class 'str'>

tupla = ('um',)  # Tupla de único elemento colocar virgula no final
type(tupla)  # Resultado: <class 'tuple'>
tupla[0]  # Resultado: 'um'
# tupla[0] = 'novo'


cores = ('verde', 'amarelo', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]

cores.index('amarelo')
cores.count('Azul')
len(cores)
