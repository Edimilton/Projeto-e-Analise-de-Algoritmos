# Considere um vetor de dados com a seguinte característica: a) os elementos iniciais do vetor são dados válidos, cujas chaves estão em ordem estritamente crescente; b) os elementos finais possuem uma chave com um valor simbólico, representando um valor infinito para aquela chave. Por exemplo, o maior valor inteiro permitido. Todos os dados não válidos possuem esta chave. Para estes elementos do vetor, a informação armazenada é irrelevante. Seja i o índice do último elemento válido do vetor. Elabore um algoritmo O(log i) para encontrar o valor deste índice. Não será aceito o uso do algoritmo de Busca Binária diretamente, pois seria O(log n) e i pode ser muito menor que n, em geral.

def busca_exp_indice(v, n):
    if v[0] == (2**31 - 1): return -1
    i = 1
  
    while i < n and v[i] < (2**31 - 1):
      i = i * 2

    if i < n:
      return busca_maior_indice(v, int(i/2), i)
    else:
      return busca_maior_indice(v, int(i/2), n-1)

def busca_maior_indice(v, esq, dir):
    if v[dir-1] != (2**31 - 1):
      return dir-1 

    meio = int((esq + dir) / 2)

    if v[meio] == (2**31 - 1):
      return busca_maior_indice(v, esq, meio)
    else:
      return busca_maior_indice(v, meio, dir)

# print(busca_exp_indice(lista, len(lista)))