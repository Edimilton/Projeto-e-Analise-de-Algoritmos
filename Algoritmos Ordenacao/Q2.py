# Considere um heap máximo H de n elementos. a) Elabore um algoritmo para encontrar e remover o elemento de menor valor de H, mantendo a propriedade de heap máximo durante o processo de busca e remoção. b) Elabore um algoritmo para encontrar e remover um elemento arbitrário v em H, mantendo a propriedade de heap máximo durante o processo de busca e remoção. Considere que v existe em H. Nesta questão você não pode gastar espaço adicional a menos de variáveis simples.

def esquerda(pos):
  return (2 * pos) + 1


def direita(pos):
  return 2 * (pos + 1)


def pai(pos):
  return int((pos - 1)/ 2)


def borbulhar(vetor, pos):
  p = pai(pos)
  while pos > 0 and vetor[pos] > vetor[p]:
    vetor[pos], vetor[p] = vetor[p], vetor[pos]
    pos = p
    p = pai(pos)


def gotejar(vetor, tamanho, pos):
  while pos >= 0:
    controle = -1
    dir = direita(pos)
    esq = esquerda(pos)
    
    if dir < tamanho and vetor[dir] > vetor[pos]:
      if vetor[esq] > vetor[dir]:
        controle = esq
      else:
        controle = dir
        
    else:
      if esq < tamanho and vetor[esq] > vetor[pos]:
        controle = esq
        
    if controle >= 0 :
      vetor[controle],vetor[pos] = vetor[pos], vetor[controle]
    pos = controle
    
  return vetor


def insere(vetor, tupla):
  vetor.append(tupla)
  vetor = borbulhar(vetor, len(vetor) - 1)
  return True


def novaHeap(vetor):
  heap = []
  for i in range(len(vetor)):
    insere(heap,vetor[i])
  return heap

  
# a)
def removeMinHeap(heap, tamanho):
  no = esquerda(0)
  altura = 0
  
  while no < tamanho:
    no = esquerda(no)
    altura += 1

  nivel = 2**altura
  menor = heap[tamanho - 1]
  index = tamanho - 1
  pos = tamanho - 1
  
  while nivel > 0:
    if  heap[pos] < menor:
      menor = heap[pos]
      index = pos
    pos -= 1
    nivel -= 1

  heap[index] = heap[tamanho -1]

  borbulhar(heap, pos)
  gotejar(heap, tamanho , pos)

  return heap[:-1]

# b)
def removeHeap(heap, tamanho, x):
  for i in range(tamanho):
    if x == heap[i]:
      pos = i
      break

  heap[pos] = heap[tamanho -1]

  borbulhar(heap, pos)
  gotejar(heap, tamanho , pos)

  return heap[:-1]