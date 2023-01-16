# Seja X = {1, 2, ..., n}. Seja W uma permutação de X tal que nenhum item pode ocupar a mesma posição que ocupava originalmente em X, ou seja, wi ≠ i, para 1 ≤ i ≤ n. Usando a técnica de backtracking elabore um algoritmo para gerar todas as permutações W possíveis para X. Por exemplo, para X={1, 2, 3} a resposta seria {2, 3, 1} e {3, 1, 2}.

def permuta(X, esq, dir):  
    if esq == dir:
      for i in range(dir):
        print(X[i][1], end=" ")
      print()
    else:
        for i in range(esq,dir):
          if X[esq][0] != i and X[i][0] != esq:
            X[esq], X[i] = X[i], X[esq]
            permuta(X, esq+1, dir)
            X[esq], X[i] = X[i], X[esq]


def permuta_sem_origem(X, esq, dir):
  for i in range(dir):
    X[i] = (i,X[i])
  permuta(X,esq,dir)

def main():
  X = [1,2,3,4]
  esq = 0
  dir = len(X)
  
  permuta_sem_origem(X, esq, dir)

if __name__== '__main__':
  main()


