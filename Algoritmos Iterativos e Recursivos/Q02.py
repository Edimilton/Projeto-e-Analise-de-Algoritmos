# Considere que você trabalha para a central de monitoramento dos dados da COVID no ministério da saúde. A central tem a sua disposição dados dos casos de infectados por COVID durante vários meses. Em uma dada janela de tempo, suponha que os dados obedeçam ao seguinte padrão: há uma sequência estritamente crescente de número de infectados, seguida de uma sequência estritamente decrescente. São muitas cidades e você tem muitos dados, em várias janelas de tempo. Assim, para facilitar a análise dos dados, você foi solicitado a elaborar um programa que dado os registros diários de infectados em uma janela de tempo que obedeça ao padrão acima, determina a data em  que ocorreu o maior número de infectados, naquela janela de tempo. Os registros diários de uma dada janela de tempo estão armazenados em um vetor, em memória primária. O seu algoritmo deve possuir complexidade O(log n), onde n é a quantidade de registros diários em uma janela de tempo.

def data_maior_num_infec(vetor, esq, dir):
    if dir == esq: 
      return dir
    meio = int((esq + dir) / 2)
  
    if vetor[meio] > vetor[meio+1]:
      return data_maior_num_infec(vetor, esq, meio)
    else: 
      return data_maior_num_infec(vetor, meio + 1, dir)

# print(data_maior_num_infec(lista, 0, len(lista)-1))