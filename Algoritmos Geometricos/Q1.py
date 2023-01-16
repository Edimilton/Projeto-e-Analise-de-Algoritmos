# Problema da Linha do Horizonte (Udi Manber – seção 5.6)

def linha_do_horizonte(edificios, esq, dir):
   if edificios == []:
       return []
   if (dir - esq) == 1:
       return [(edificios[esq][0], edificios[esq][1]), (edificios[esq][2], 0)] 

   meio = (esq + dir) // 2
   edf_esq = linha_do_horizonte(edificios, esq, meio)
   edf_dir = linha_do_horizonte(edificios, meio, dir)
   return intercala(edf_esq, edf_dir)

def intercala(edf_esq, edf_dir):
   alturaA = 0
   alturaB = 0
   i = 0
   j = 0
   n = len(edf_esq)
   m = len(edf_dir)
   coord_linhas = []

   while i < n and j < m:
       if edf_esq[i][0] < edf_dir[j][0]:
           alturaA = edf_esq[i][1]
           borda = edf_esq[i][0]
           i += 1
       elif edf_dir[j][0] < edf_esq[i][0]:
           alturaB = edf_dir[j][1]
           borda = edf_dir[j][0]
           j += 1
       else:
           alturaA = edf_esq[i][1]
           alturaB = edf_dir[j][1]
           borda = edf_dir[j][0]
           i += 1
           j += 1
       if coord_linhas == [] or coord_linhas[-1][1] != max(alturaA, alturaB):
           coord_linhas.append((borda, max(alturaA, alturaB))) 

   while i < n:
     coord_linhas.append(edf_esq[i])
     i += 1
   while j < m:
     coord_linhas.append(edf_dir[j])
     j += 1
   return coord_linhas

def main():
  coordenadas = [(1, 8, 5), (3, 12, 6), (4, 12, 5), (5, 17, 18)]
  esq = 0
  dir = len(coordenadas)
  print(linha_do_horizonte(coordenadas,esq,dir))]

if __name__ == '__main__':
	main()