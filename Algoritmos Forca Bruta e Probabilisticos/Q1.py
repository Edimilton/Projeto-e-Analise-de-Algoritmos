# Considere o Problema da Mochila com as seguintes variações: (i) há um número infinito de itens de mesmo tamanho, para cada item do conjunto de itens; (ii) cada item tem associado a ele um valor positivo. Desta forma, um dado item pode ser escolhido repetidas vezes na composição da solução. Usando a técnica de backtracking, elabore um algoritmo para determinar o subconjunto de itens que preenchem exatamente a mochila de tamanho K e cuja soma dos valores dos itens da solução seja a maior possível. Por exemplo, para um conjunto de itens de tamanhos S = {2, 3, 4, 5} com valores V = {10, 5, 20, 2}, respectivamente, e capacidade da mochila K = 6, soluções possíveis poderiam ser S1={2, 2, 2}, S2={3, 3}, S3={2, 4}. No entanto, estas soluções valem, respectivamente, 30, 10, 30. Portanto, sua resposta seria ou a solução S1 ou a S3.

def knapsack_peso_repetidos(pesos,valores, capacidade, n, k):
  
    if capacidade <= 0 or k >= n:
      return 0

    soma_com_valor = 0
    soma_sem_valor = 0
  
    if pesos[k] <= capacidade:
      soma_com_valor = valores[k] + knapsack_peso_repetidos(pesos,valores, capacidade - pesos[k], n, k)
      
    soma_sem_valor = knapsack_peso_repetidos(pesos,valores, capacidade, n, k + 1)

    if soma_com_valor > soma_sem_valor:
      return soma_com_valor
    else:
      return soma_sem_valor

def main():
  valores = [40, 100, 160]
  pesos = [10, 20, 30]
  capacidade = 50
  n = len(valores)
  
  print(knapsack_peso_repetidos(pesos, valores, capacidade, n, 0))

if __name__ == '__main__':
  main()