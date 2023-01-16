# Considere o problema da questão 2. Pesquise como calcular a quantidade de permutações W possíveis para X. Com base neste número, elabore um algoritmo probabilístico para resolver o mesmo problema da questão 2. Qual técnica está utilizando?

from random import randint

def notElem(x , lista):
  for i in lista:
    if x == i:
      return False
  return True

 
def index_diferente(X,n):
  for i in range(n):
    if X[i][0] == i:
      return False
  return True


def fatorial(n):
  if n==0 or n==1:
    return 1
  else: 
    return n * fatorial(n - 1)


def fatorial_sem_origem(n):
  result = 0
  for i in range(n+1):
    result += ((-1)**i)/fatorial(i)
  result = fatorial(n) * result
  return result


def permutacao(X, n):

  for i in range(n):
    X[i] = (i,X[i])

  maxima_permutacao = int(fatorial_sem_origem(n))
  permutacoes = [0]*maxima_permutacao
  k = 0
  
  while k < maxima_permutacao:
      j = randint(0,n-1)
      i = randint(0,n-1)
      
      X[i], X[j] = X[j], X[i]
      if index_diferente(X,n):
        if notElem(X, permutacoes):
          permutacoes[k] = X[:]
          k = k + 1
      
  for i in permutacoes:
    for j in range(n):
      print(i[j][1], end=" ")
    print()


def main():
  X = [1, 2, 3, 4]
  n = len(X)
  permutacao(X, n)

if __name__ == '__main__':
  main()


"""
2 1 4 3   V
2 3 4 1   V
2 4 1 3   V
3 1 4 2   V
3 4 1 2   V
3 4 2 1   V
4 3 2 1   V
4 3 1 2   V
4 1 2 3   V
"""