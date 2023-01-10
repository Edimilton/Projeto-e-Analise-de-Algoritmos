# Suponha que você tenha um vetor de n registros para ordenar cujas chaves só podem assumir os valores -1, 0 ou 1. Os registros possuem vários dados além da chave. Um algoritmo para ordenar este conjunto de registros pode possuir um subconjunto das seguintes características: a) O algoritmo roda em O(n); b) O algoritmo é estável, ou seja, registros de mesmo valor de chave aparecem no vetor de saída do algoritmo na mesma ordem que estavam no vetor de entrada; c) O algoritmo ordena no local, ou seja, sem gastar espaço adicional a menos de variáveis simples. Elabore duas soluções conceitualmente distintas para esse problema, sendo uma delas i) satisfazendo os critérios (a) e (b) e a outra ii) satisfazendo os critérios (a) e (c).

def ordena_reg(vetor):
  vm1 = []
  v0 = []
  v1 = []

  for num in vetor:
    if num == -1: vm1.append(num)
    elif num == 0: v0.append(num)
    else: v1.append(num)

  for num in range(len(vm1)):
    vetor[num] = vm1[num]
    
  for num in range(len(v0)):
     vetor[num + len(vm1)] = v0[num]
    
  for num in range(len(v1)):
    vetor[num + len(vm1) + len(v0)] = v1[num] 
  
  return vetor

def ordena_reg_b(vetor, esq, dir):

  i = esq
  j = dir
  
  while i < j:
    while (vetor[i] == -1) and (i < dir):
      i +=1
    while (vetor[j] != -1) and (j > esq):
      j -=1
    if (i < j):
      aux = vetor[i]
      vetor[i] = vetor[j]
      vetor[j] =  aux

  j = dir
  
  while i < j:
    while (vetor[i] == 0) and (i < dir):
      i +=1
    while (vetor[j] != 0) and (j > esq):
      j -=1
    if (i < j):
      aux = vetor[i]
      vetor[i] = vetor[j]
      vetor[j] =  aux

  return vetor
