# Dados dois vetores de inteiros ordenados em ordem crescente, gere um terceiro vetor com os dados dos vetores de entrada também ordenados em ordem crescente, mas sem elementos repetidos.

def uniao_vetor(vetor1, vetor2):
  pos_v1 = 0
  pos_v2 = 0
  vetor3 = []

  while pos_v1 < len(vetor1) and pos_v2 < len(vetor2):
    if vetor1[pos_v1] < vetor2[pos_v2]:
      vetor3.append(vetor1[pos_v1])
      pos_v1 += 1
    elif vetor2[pos_v2] < vetor1[pos_v1]:
      vetor3.append(vetor2[pos_v2])
      pos_v2 += 1
    else:
      vetor3.append(vetor1[pos_v1])
      pos_v1 += 1
      pos_v2 += 1  
  
  while pos_v1 < len(vetor1):
    vetor3.append(vetor1[pos_v1])
    pos_v1 += 1

  while pos_v2 < len(vetor2):
    vetor3.append(vetor2[pos_v2])
    pos_v2 += 1

  return vetor3

# a = [1,2,34,56,123]
# b = [1,3,7,34,56,122,145,155,165]

# print(uniao_vetor(a,b))