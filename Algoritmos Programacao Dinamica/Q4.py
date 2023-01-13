# Suponha que você trabalhe para uma firma de avaliadores de bens de heranças. Dois irmãos mandaram avaliar todos os itens da casa dos pais, como jóias, dinheiro em moeda estrangeira, antiguidades, obras de arte, etc. Cada item i, 1 ≤ i ≤ n, tem um valor vi a ele associado. Como a família é muito rica a lista de itens é imensa. Os irmãos não possuem preferência sobre os bens que herdarão, mas desejam que a partilha seja o mais próxima possível de forma que o irmão que ficar com a porção de maior valor não tenha que pagar muito em dinheiro ao outro irmão para compensar a diferença. Assim seu objetivo é elaborar um algoritmo que dado uma lista de bens com seus valores, divide estes bens em dois subconjuntos de forma que a diferença das somas dos valores dos itens de cada subconjunto seja a menor possível. Caso mais de uma solução de mesma diferença mínima seja possível, escolha arbitrariamente uma delas. Por exemplo, suponha que n=5 e os itens valessem V={1000, 2000, 1500, 500, 2500}. Uma partilha possível seria: I1= {1000, 2000, 500} e I2= {1500, 2500}. Neste caso a diferença entre os dois irmão é de 500 reais apenas, a menor possível entre as várias possibilidades de pares de subconjuntos.

def divide_heranca(peso, pesos, n, matriz):
    for i in range(1, n + 1):
        for j in range(1, peso + 1):
            if pesos[i-1] <= j:
                matriz[i][j] = max(pesos[i-1]
                          + matriz[i-1][j-pesos[i-1]],  
                              matriz[i-1][j])
            else:
                matriz[i][j] = matriz[i-1][j]
 
  
def resgata_heranca(matriz, n, peso, pesos):
  i = n
  j = peso
  valor_maximo = matriz[i][j]
  while valor_maximo > 0:
    if valor_maximo != matriz[i - 1][j]:
      irmao1.append(pesos[i - 1])
      valor_maximo -= pesos[i - 1]
      j -= pesos[i - 1]
    i -= 1

def herenca_irmao2(pesos, n, irmao1, m):
  irmao2 = []
  j = m - 1
  for i in range(n):
    if pesos[i] != irmao1[j]:
      irmao2.append(pesos[i])
    else:
      j -= 1
      if j < 0:
        for k in range(i+1, n):
          irmao2.append(pesos[k])
        return irmao2
    

#teste
pesos = [1000, 2000, 1500, 500, 2500]
irmao1 = []
peso = sum(pesos)//2
n = len(pesos)
matriz = [[0 for x in range(peso + 1)] for x in range(n + 1)]

def main():
  
  divide_heranca(peso, pesos, n, matriz)
  resgata_heranca(matriz,n,peso,pesos)
  
  m = len(irmao1) 
  
  print(irmao1)
  print(herenca_irmao2(pesos, n, irmao1, m))

if __name__ == '__main__':
	main()