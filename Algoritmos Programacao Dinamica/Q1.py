# Estude o problema de Edição de Sequências (Seção 6.8 do Udi Manber, pag.155) e adapte este algoritmo para propor outra solução para o problema da Mais Longa Subsequência Comum.

def min_edit_dist(A, m, B, n, matriz):
  for i in range(1, m + 1):
      for j in range(1, n + 1):
        if (A[i - 1] == B[j - 1]):
          matriz[i][j] = (1 + matriz[i - 1][j - 1][0], "D")
        elif matriz[i - 1][j][0] > matriz[i][j - 1][0]:
          matriz[i][j] = (matriz[i - 1][j][0], "A")
        else:
          matriz[i][j] = (matriz[i][j - 1][0], "E")

def imprime_lsc(matriz,i,j,x):
  if matriz[i][j] != (0, '*'):
    if matriz[i][j][1] == "D":
      imprime_lsc(matriz, i-1, j-1, x)
      print(x[i-1])
    elif matriz[i][j][1] == "A":
      imprime_lsc(matriz, i-1, j, x)
    else:
      imprime_lsc(matriz, i, j-1, x)

      
#teste
def main():
  A = "DNDANANA"
  B = "NDAANN"
  m = len(A)
  n = len(B)
  
  matriz = [[(0,"*") for i in range(n+1)] for j in range(m+1)]
  
  min_edit_dist(A,m,B,n,matriz)
  imprime_lsc(matriz,m,n,A)

if __name__ == '__main__':
	main()
