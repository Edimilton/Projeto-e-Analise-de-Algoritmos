# Um ponto p domina outro ponto q se ambas as coordenadas x e y de p forem maiores ou iguais que as respectivas coordenadas de q. Um ponto p é um ponto maximal num conjunto de pontos A se nenhum ponto em A domina p. Por exemplo, se A = {(2,4), (4,4), (5,3)}, temos que o ponto (4,4) domina o ponto (2,4) e que os pontos (4,4) e (5,3) são ambos maximais. Dado um conjunto C de n pontos, faça: a) projete um algoritmo O(n log n) para encontrar o conjunto de pontos maximais de C. b) Para cada p ∈ C, seja D(p) o conjunto de pontos de C que são dominados por p. Elabore um algoritmo O(n log n) para computar a cardinalidade de D(p) para todo p ∈ C.

def mergeSorty(coordenadas, esq, dir):
   if coordenadas == []:
       return []
   if (dir - esq) == 1:
       return [coordenadas[esq]]
   meio = (esq + dir) // 2
   pts_esq = mergeSorty(coordenadas, esq, meio)
   pts_dir = mergeSorty(coordenadas, meio, dir)
   return intercala(pts_esq, pts_dir)


def intercala(pts_esq, pts_dir):
   i = 0
   j = 0
   k = 0
   result = []

   while i < len(pts_esq) and j < len(pts_dir):      
      if pts_esq[i][1] > pts_dir[j][1]:
        result.append(pts_esq[i])
        i += 1
      elif pts_dir[j][1] > pts_esq[i][1]:
        result.append(pts_dir[j])
        j += 1
      else:
        if pts_esq[i][0] > pts_dir[j][0]:
          result.append(pts_esq[i])
          i += 1
        else: 
          result.append(pts_dir[j])
          j += 1
      k += 1  

   while i < len(pts_esq):
     result.append(pts_esq[i])
     i += 1
   while j < len(pts_dir):
     result.append(pts_dir[j])
     j += 1
   return result


def pontos_maximais(coordenadas, n):
  coordenadas = mergeSorty(coordenadas,0,n)
  print(coordenadas)
  maximal = coordenadas[0][0]
  print("Pontos Maximais")
  print("(",coordenadas[0][0],",",coordenadas[0][1],")")
  for i in range(1,n):
    if coordenadas[i][0] > maximal:
      print("(",coordenadas[i][0],",",coordenadas[i][1],")")
      maximal = coordenadas[i][0]



coordenadas = [(5,3), (2,4), (4,4),(5,2)]
n = len(coordenadas)

pontos_maximais(coordenadas, n)


def merge_sort(coordenadas, esq, dir, cont_card):
   if coordenadas == []:
       return []
   if (dir - esq) == 1:
       return [coordenadas[esq]]

   meio = (esq + dir) // 2
   co_esq = merge_sort(coordenadas, esq, meio, cont_card)
   co_dir = merge_sort(coordenadas, meio, dir, cont_card)
   return computa(co_esq, co_dir, cont_card)

def computa(co_esq, co_dir, cont_card):
    i = 0
    j = 0
    result = []
    while i < len(co_esq) or j < len(co_dir):
      if  j >= len(co_dir) or (i < len(co_esq) and co_esq[i][1][0] < co_dir[j][1][0]):
        result.append(co_esq[i])
        cont_card[co_esq[i][0]] += j
        i += 1
      else:
        result.append(co_dir[j])
        j += 1
    return result


def computa_card(coordenadas, esq, dir):
  cont_card = [0] * dir
  index_coord = ["*"] * dir
  nums = mergeSorty(coordenadas, esq, dir)
  for i in range(dir):
    index_coord[i] = (i,nums[i])
  merge_sort(index_coord, esq, dir, cont_card)
  print("Cardialidade de p")
  for i in range(dir):
    print(coordenadas[i],"=",cont_card[i])


computa_card(coordenadas, 0, len(coordenadas))