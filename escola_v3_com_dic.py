#!/usr/bin/env python3
"""Relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.0.2"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Julia"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Inglês": aula_ingles,
    "Música": aula_musica,
    "Dança": aula_danca,
}

# Listar alunos em cada atividade por sala

for atividade, alunos in atividades.items():

    print(f"Alunos de {atividade}: {alunos}")


    print(sala1)
    
    #sala que tem interseção com a atividade    
 #     atividade_sala1 = set(sala1) & set(alunos)
 #     atividade_sala2 = set(sala2).intersection(set(alunos))
 # 
 #     print("sala 1:" ,atividade_sala1)
 #     print("sala 2:",atividade_sala2)        
 #     print("-"*40)
