# %%
# Dicionário com uma lista de cursos dentro
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38,
          'cursos': ['Inglês', 'Português']}
type(pessoa)
dir(dict)
len(pessoa)

pessoa
pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]
# pessoa['tags']
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade') # Pega o valor no dicionário
pessoa.get('tags')
pessoa.get('tags', [])
