# Suponha que você tem um padrão P de tamanho m e vários textos Ti, 1 ≤ i ≤ n, de tamanho ki. O índice de relevância de um texto Ti em relação ao padrão P é dado pela quantidade de vezes que P ocorre em Ti. Elabore duas soluções para retornar o índice do texto Ti mais relevante em relação a P. Caso dois textos possuam a mesma relevância, deve retornar todos os textos de maior relevância. Em uma das soluções você deve adaptar o KMP e na outra o Horspool.

# a)
def computaNext(p, m, next):
  next[0] = 0
  next[1] = 1
  
  for i in range(2, m):
  
    j = next[i-1] + 1
    
    while p[i-1] != p[j-1] and j > 0:
      j = next[j-1] + 1
    
    next[i] = j

    
def kmp(t, n, p, m):
  next = [0] * m
  computaNext(p, m, next) 
  
  i = 0
  j = 0
  relevancia = 0
  
  while i < n:
    if p[j] == t[i]:
      j = j+1
      i = i+1
    else:
      j = next[j]+1
      if j == 0:
        i += 1
    if j == m:
      j = 0
      relevancia += 1
    
  return relevancia


#b)
def computaDeslocamento(p, m, d):
  for j in range(m-1):
    d[ord(p[j])] = m-1-j


def horspool(t, n, p, m):
  d = [m] * 256
  
  computaDeslocamento(p, m, d)  

  i = m - 1
  relevancia = 0
  
  while i < n:
    k = 0
    
    while k < m and p[m-1-k] == t[i-k]:
      k += 1
      
    i += d[ord(t[i])]

    if k == m:
      relevancia += 1

  return relevancia


def maior_relevancia(textos, padrao):
  tanh_ts = len(textos)
  tanh_p = len(padrao)
  txt_relevancia = []
  
  for texto in textos:
    tanh_t = len(texto)
    #txt_relevancia.append(kmp(texto, tanh_t, padrao, tanh_p))
    txt_relevancia.append(horspool(texto, tanh_t, padrao, tanh_p))

  maior = max(txt_relevancia)
  indices = []
  
  for i in range(tanh_ts):
    if txt_relevancia[i] == maior:
      indices.append(i)

  return indices



textos = ["xxxyxy","xxyxxyx","xxyxxyxxyx","xxyxxyxxyx"]
padrao = "xyx"

print(maior_relevancia(textos,padrao))