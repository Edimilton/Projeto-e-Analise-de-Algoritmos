# Suponha que você trabalha numa empresa como gerente de um grande projeto. Você precisa escolher em um dado momento qual o conjunto de tarefas a ser realizadas no próximo passo. Cada tarefa tem associado a ela um valor, representando uma medida de avanço do projeto, que é um inteiro, uma data de início e uma duração, em número de dias. A escolha a ser feita não pode selecionar tarefas cujos intervalos de tempo de execução se intersectem. O seu objetivo é elaborar um algoritmo para selecionar um de conjunto das tarefas disponíveis que possam ser realizadas no próximo passo, de tal forma a maximizar a soma dos valores de avanço do projeto.

def avanco_sem_conflito(tarefas, n):

  organiza_tarefas(tarefas)

  quick_sort(tarefas, 0, len(tarefas)-1)

  valores = [None] * n
  
  valores[0] = tarefas[0][0]

  for i in range(1,n):
    
    valor = tarefas[i][0]
    sem_conflito = busca_sem_conflito(tarefas, i)
    
    if (sem_conflito != -1):
      valor += valores[sem_conflito]

    if (valores[i-1] < valor):
      valores[i] = valor
    else:
      valores[i] = valores[i-1]

  print("Valor do maximo avanco possivel:", valores[n-1])

def busca_sem_conflito(tarefas, i):
    for j in range(i - 1, -1, -1):
        if tarefas[j][2] <= tarefas[i][1]:
            return j 
    return -1  

def particiona(vetor, esq, dir):
  pivo = vetor[dir][2]
  i = esq - 1
  for j in range(esq, dir):
    if vetor[j][2] <= pivo:
      i = i + 1
      (vetor[i], vetor[j]) = (vetor[j], vetor[i])
  (vetor[i + 1], vetor[dir]) = (vetor[dir], vetor[i + 1])
  return i + 1

def quick_sort(vetor, esq, dir):
  if esq < dir:
    pi = particiona(vetor, esq, dir)
    quick_sort(vetor, esq, pi - 1)
    quick_sort(vetor, pi + 1, dir)

def organiza_tarefas(tarefas):
  for i in tarefas:
    i[2] = i[1] + i[2]


    
#teste
def main():
  tarefas = [[2, 1, 4], [4, 2, 6], [4, 6, 3], [7, 3, 9], [2, 10, 3], [1, 11, 3]]
  
  avanco_sem_conflito(tarefas, len(tarefas))

if __name__ == '__main__':
	main()