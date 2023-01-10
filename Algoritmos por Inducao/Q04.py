# Dados dois vetores de inteiros A e B, gere um terceiro vetor representando o vetor interseção dos vetores originais, nas duas situações abaixo. A solução para cada situação deve ser distinta, ou seja, você não pode reutilizar parte da solução de um item em outro item. O vetor de interseção não pode ter elementos duplicados. a) A e B estão ordenados, em ordem decrescente; b) A e B estão em ordem arbitrária.


# a)
def inters_vetor_a(vetor1, vetor2):
  pos_v1 = 0
  pos_v2 = 0
  vetor3 = []

  while pos_v1 < len(vetor1) and pos_v2 < len(vetor2):
    if vetor1[pos_v1] < vetor2[pos_v2]:
      pos_v1 += 1
    elif vetor2[pos_v2] < vetor1[pos_v1]:
      pos_v2 += 1
    else:
      vetor3.append(vetor1[pos_v1])
      pos_v1 += 1
      pos_v2 += 1  

  return vetor3

# b)
def inters_vetor_b(vetor1, vetor2):

  vetor3 = []

  for elemento_v1 in vetor1:
    for elemento_v2 in vetor2:
      if elemento_v1 == elemento_v2:
        vetor3.append(elemento_v1)

  return vetor3


# c = [18,2,14,80,56,123]
# d = [11,123,18,34,56,1,145,14]

# print(inters_vetor_b(c,d))