# Sejam A: a1, a2,.., an e B: b1, b2...,bm duas cadeias de caracteres. Diz-se que a cadeia B é subsequência da cadeia A se existir uma sequência de índices 1 ≤ i1 ≤ i2 ≤ ... ≤ ik ≤ n, tal que para todo j, 1 ≤ j≤ k, Aij = Bj. Por exemplo, A: disciplina; B: isca; B é subsequência de A, pois possui uma sequência crescente de índices, i1=2,i2=3,i3=4,i4=10 de tal forma que obedece ao estabelecido na definição. Observe que A2 = B1 = i, A3 = B2 = s, A4 = B3 = c e A10 = B4 = a. Já C: ida não é subsequência de A, pois os índices de i, d, a são, respectivamente, 2, 1, 10 e esta sequência de índices não é crescente, ou seja, i e d não estão na mesma ordem que em A. Dadas duas cadeias de caracteres A e B, elabore algoritmos para i. Determinar se B é subsequência de A; ii. Supondo que pode haver mais de uma possibilidade de índices que comprove que B é subsequência de A, devolver aquela sequência de índices cuja soma seja a maior possível, dentre todas as possibilidades existentes. 

# i)
def subsequencia(a,b):
  tanh_b = len(b)
  i = 0
  for letra in a:
    if letra == b[i]: 
      i +=  1
      if i == tanh_b:   
        return True
  return False

# print(subsequencia("disciplina", "isca"))

  
# ii)
def maior_subsequencia(a,b):
  tanh_a = len(a) - 1
  i = len(b) - 1 
  indices = [-1] * len(b)
  for k in range(tanh_a, -1, -1):
    if a[k] == b[i]: 
      indices[i] = k
      i -=  1
      if i < 0:   
        return indices

# print(maior_subsequencia("disciplina", "isca"))