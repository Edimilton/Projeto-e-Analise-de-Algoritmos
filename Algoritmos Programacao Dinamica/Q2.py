# Suponha que você tenha a sua disposição o número de casos de morte pela COVID em uma janela de tempo. Estes números podem crescer e decrescer ao longo dos dias. Elabore um algoritmo para determinar as datas da mais longa subsequência crescente de mortes, em uma dada janela de tempo. Caso haja mais de uma subsequência mais longa, devolva arbitrariamente uma delas.

def lsc(seq, n, matriz):
    seq_ord = sorted(list(set(seq)))
    m = n
  
    for i in range(1,n+1):
        for j in range(1,m+1):
            if seq[i-1] == seq_ord[j-1]:
              matriz[i][j] = (1+matriz[i-1][j-1][0],"D")
            elif matriz[i-1][j][0] > matriz[i][j-1][0]:
              matriz[i][j] = (matriz[i-1][j][0], "A")
            else: 
              matriz[i][j] = (matriz[i][j-1][0], "E")

          
def imprime_lsc(matriz,i,j,x):

  if matriz[i][j] != (0, '*'):
    if matriz[i][j][1] == "D":
      imprime_lsc(matriz, i-1, j-1, x)
      print(x[i-1])
    elif matriz[i][j][1] == "A":
      imprime_lsc(matriz, i-1, j, x)
    else:
      imprime_lsc(matriz, i, j-1, x)

def print_matrix(m):
    for j in m:
      for i in j:
        print(i, end = " ")
      print()
      
      
#teste
def main():
  mortes = [800,900,850,955,750,1100,1005,1215,1155]
  
  datas = ["01/02/2021", "02/02/2021", "03/02/2021", "04/02/2021", "05/02/2021", "06/02/2021", "07/02/2021", "08/02/2021", "09/02/2021"]
  
  n = len(mortes)
  m = n
  matriz = [[(0,"*") for i in range(n+1)] for j in range(m+1)]
  lsc(mortes, n, matriz)
      
  print_matrix(matriz)
  
  imprime_lsc(matriz,n,m,datas)

if __name__ == '__main__':
	main()