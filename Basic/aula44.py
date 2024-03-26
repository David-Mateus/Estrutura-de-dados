"""
Lista de listas e seus índices
"""
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda', (0,2,3,4)]
]
# print(salas[2][3][3])

#Para buscar valores dentro de lista dentro de outra lista [lista1][lista2]

# For para percorrer lista dentro de lista
# Para cada sala em salas
# retorne os alunos
# for no for mais externo
for sala in salas:
    # for no for mais interno
    for alunos in sala:
        print(alunos)