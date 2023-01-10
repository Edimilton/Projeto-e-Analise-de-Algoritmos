# Dado um vetor de inteiros de n elementos, elabore um algoritmo para determinar quantos destes números são negativos.

# vetor = [1,-3,7,-8,9,2]

def is_neg(n):
  if n < 0:
    return 1
  else:
    return 0

def qts_neg(vetor):
  if vetor == []:
    return 0
  else:
    n = vetor[0]
    return is_neg(n) + qts_neg(vetor[1:])

#print(qts_neg(vetor))