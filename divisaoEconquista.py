def mergesort(lista):
  if len(lista) <= 1:
    return lista
  meio = len(lista) // 2
  esquerda = lista[:meio]
  direita = lista[meio:]

  esquerda = mergesort(esquerda)
  direita = mergesort(direita)

  return merde(esquerda, direita)

def merge(esquerda,direita):
  resultado = []
  i = 0, j = 0
  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      resultado.append(esquerda[i])
      i += 1
    else:
      resultado.append(direita[j])
      j += 1
    while i < len(esquerda[i]):
      resultado.append(esquerda[i])
      i += 1
    while j < len(direita[j]):
      resultado.append(direita[j])
      j += 1

  return resultado


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista)//2]
        menores = [x for x in lista if x < pivot]
        iguais = [x for x in lista if x == pivot]
        maiores = [x for x in lista if x > pivot]
        return quicksort(menores) + iguais + quicksort(maiores)
      
