# Suponha que você trabalha para uma agência de comunicação que usa a informação das redes sociais, em todo o mundo. Você foi requisitado a elaborar um algoritmo para identificar as cem pessoas mais influentes da rede, a fim de engajá-las numa campanha publicitária. A agência dispõe de um arquivo cujos registros incluem o nome da pessoa e a quantidade de amigos que ela possui na rede. A pessoa x é mais influente que a pessoa y se o número de amigos de x for maior que o número de amigos de y, na rede social. Você pode supor que os dados do arquivo cabem em memória primária. Se duas ou mais pessoas forem igualmente influentes, você pode escolher arbitrariamente entre elas quando estiver coletando os últimos dados. Elabore duas soluções conceitualmente distintas para este problema e decida, baseado na complexidade, qual a melhor solução dentre as duas que idealizou. Observe que como as soluções são conceitualmente distintas, se você, por exemplo, resolver usar um algoritmo com propósito P como parte de uma solução, não poderá usar nenhum outro algoritmo que tenha o mesmo propósito P na segunda solução, mesmo que os dois algoritmos sejam diferentes.

def mergeSort(lista):
    if len(lista) > 1:
        meio = int(len(lista)/2)

        lista_esq = lista[:meio]
        lista_dir = lista[meio:]

        mergeSort(lista_esq)
        mergeSort(lista_dir)

        intercala(lista, lista_esq, lista_dir)
      
    return lista

def intercala( lista, lista_esq, lista_dir):
  i = 0
  j = 0
  k = 0

  while i < len(lista_esq) and j < len(lista_dir):
    esq = lista_esq[i]
    dir = lista_dir[j]
    if esq[1] >= dir[1]:
        lista[k]=lista_esq[i]
        i += 1
    else:
        lista[k]=lista_dir[j]
        j += 1
    k += 1

  while i < len(lista_esq):
    lista[k]=lista_esq[i]
    i += 1
    k += 1

  while j < len(lista_dir):
    lista[k]=lista_dir[j]
    j += 1
    k += 1

def maximo(lista):
  if lista != []:
    num_maximo = lista[0]
  else: return
    
  for i in lista:
    if i[1] > num_maximo[1]:
      num_maximo = i
  return num_maximo

  
def mais_influentes(registros):
  influentes = []
  for i in range(100):
    mais_amigos = maximo(registros)
    pos = registros.index(mais_amigos)
    registros[pos] = ("",0) 
    influentes.append(mais_amigos)
  return influentes


def mais_influentes_2(registros):
  lista = mergeSort(registros)
  influentes = []
  for i in range(100):
    influentes.append(lista[i])
  return influentes