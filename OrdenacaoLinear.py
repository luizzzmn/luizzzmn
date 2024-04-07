import random
from random import shuffle
from time import time
import matplotlib.pyplot as plt
import numpy as np
class OrdenacaoLinear:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for j in range(n-1):
            for i in range(n-1):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]

    @staticmethod
    def selection_sort(lista):
        n = len(lista)
        for j in range(n-1):
            min_index = j
            for i in range(j+1, n):
                if lista[i] < lista[min_index]:
                    min_index = i
            lista[j], lista[min_index] = lista[min_index], lista[j]

    @staticmethod
    def insertion_sort(lista):
        n = len(lista)
        for i in range(1, n):
            key = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > key:
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = key

    @staticmethod
    def counting_sort(lista):

      # criando listas e achando maior valor
      maior = max(lista)
      count = [0] * (maior + 1)
      output = [0] * len(lista)

      # contando elementos da lista
      for i in range(len(lista)):
        num = lista[i]
        count[num] += 1

      # somando frequencia acumulada
      for i in range(1,len(count)):
        count[i] = count[i-1] + count[i]

      # colocando elementos nas posições certas no output
      for i in range(len(lista)):
        output[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1

      # alterando lista original
      lista = output


# função para executar os algoritmos mais fácil

def criar_lista(tamanho=False):
  if not tamanho: tamanho = int(input("tamanho da lista para ordenar: "))
  lista = [x for x in range(tamanho)]
  shuffle(lista)
  return lista

def executar(algoritmo, tamanho_da_lista = False, num_execucoes = 1, mostrar_tempo_cada_execucao = True, mostrar_tempo_medio = True):

  print(algoritmo + ':')
  tempo_total = 0

  if mostrar_tempo_cada_execucao and num_execucoes > 1 and tamanho_da_lista:
    print(f"Tempos de cada execução de {tamanho_da_lista} elementos:")

  for i in range(num_execucoes):

    if tamanho_da_lista: lista = criar_lista(tamanho_da_lista)
    else: lista = criar_lista()

    tempo_inicial = time()

    match algoritmo:

      case "bubble sort":
        OrdenacaoLinear.bubble_sort(lista)

      case "selection sort":
        OrdenacaoLinear.selection_sort(lista)

      case "insertion sort":
        OrdenacaoLinear.insertion_sort(lista)

      case "counting sort":
        OrdenacaoLinear.counting_sort(lista)

      case _:
        print("Digitou o nome errado.")
        return

    tempo_final = time()
    tempo_total += tempo_final - tempo_inicial

    if mostrar_tempo_cada_execucao: print(f"{'Tempo da execução' if num_execucoes==1 else ''}{i+1 if num_execucoes>1 else ''}: {tempo_final - tempo_inicial:.5f}s")

  if mostrar_tempo_medio and num_execucoes > 1: print(f"Tempo médio das {num_execucoes} execuções: {tempo_total / num_execucoes:.5f}s")
  print()
  return round(tempo_total / num_execucoes, 5)

executar('bubble sort', 1000, 2)
executar('selection sort', 1000, mostrar_tempo_medio=False)
executar('insertion sort', 1000, 3, False, True)
print()

counting_tempos = [
  executar('counting sort', 1000),
  executar('counting sort', 10000),
  executar('counting sort', 100000),
  executar('counting sort', 1000000)
]

bubble_tempos = [
  executar('bubble sort', 1000),
  executar('bubble sort', 10000),
  800,    #executar('bubble sort', 100000), # o certo seria estar o executar aqui
  8000    #executar('bubble sort', 1000000)
]

selection_tempos = [
  executar('selection sort', 1000),
  executar('selection sort', 10000),
  400,    #executar('selection sort', 100000),
  4000    #executar('selection sort', 1000000)
]

insertion_tempos = [
  executar('insertion sort', 1000),
  executar('insertion sort', 10000),
  500,    #executar('insertion sort', 100000),
  5000    #executar('insertion sort', 1000000)
]



tamanho_input = ['1000','10000', '100000', '1000000']

plt.ylabel("Tempo de Execução (em segundos)")
plt.xlabel("Tamanho do input")

plt.plot(tamanho_input, bubble_tempos, label='Bubble')
plt.plot(tamanho_input, selection_tempos, label='Selection')
plt.plot(tamanho_input, insertion_tempos, label='Insertion')
plt.plot(tamanho_input, counting_tempos, label='Counting')

plt.legend(loc='upper left')
