# Suponha que sua entrada seja um vetor de n registros contendo (cpf, nome, gênero, idade). Adapte o HeapSort para ordenar este vetor de acordo com a idade, em ordem decrescente. Caso várias pessoas possuam a mesma idade, o desempate se dará pelo gênero, de forma que pessoas de uma mesma idade do gênero feminino precedam as do gênero masculino de mesma idade e, por sua vez, estas precedam as dos demais gêneros de mesma idade. Você pode usar os símbolos ‘F’, ‘M’ e ‘X’, para designar os gêneros feminino, masculino e demais gêneros, respectivamente.

def esquerda(pos):
  return (2 * pos) + 1


def direita(pos):
  return 2 * (pos + 1)


def pai(pos):
  return int((pos - 1)/ 2)


def borbulhar(vetor, pos):
  p = pai(pos)
  while pos > 0 and vetor[pos][3] <= vetor[p][3]:
    if vetor[pos][3] < vetor[p][3]:
      vetor[pos], vetor[p] = vetor[p], vetor[pos]
    else:
      if vetor[pos][2] > vetor[p][2]:
        vetor[pos], vetor[p] = vetor[p], vetor[pos]
    pos = p
    p = pai(pos)


def gotejar(vetor, tamanho, pos):
  while pos >= 0:
    controle = -1
    dir = direita(pos)
    esq = esquerda(pos)
    
    if dir < tamanho and vetor[dir][3] < vetor[pos][3]:
      if vetor[dir][3] <= vetor[esq][3]:
        if vetor[dir][3] < vetor[esq][3]:
          controle = dir
        elif vetor[dir][2] > vetor[esq][2]:
          controle = dir
        else: 
          controle = esq
      else:
        controle = esq
        
    elif esq < tamanho and vetor[esq][3] < vetor[pos][3]:
      controle = esq

    elif dir < tamanho and vetor[dir][3] == vetor[pos][3]:
      if vetor[dir][2] > vetor[pos][2]:
        if vetor[dir][3] == vetor[esq][3]:
          if vetor[dir][2] > vetor[esq][2]:
            controle = dir
          else:
            controle = esq
        else: 
          controle = dir
          
      else:
        if vetor[esq][3] == vetor[pos][3]:
          if vetor[esq][2] > vetor[pos][2]:
            controle = esq

    elif esq < tamanho and vetor[esq][3] == vetor[pos][3]:
      if vetor[esq][2] > vetor[pos][2]:
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


def heapsort(vetor, tamanho):
  while tamanho > 1:
    vetor[tamanho -1], vetor[0] = vetor[0], vetor[tamanho -1] 
    tamanho -= 1
    vetor = gotejar(vetor, tamanho, 0)
  return vetor

