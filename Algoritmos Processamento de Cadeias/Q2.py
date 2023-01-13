# Dados um texto T de tamanhos n e uma lista de padrões Pj, 1 ≤ j ≤ p, todos de tamanho m, encontre quantas vezes ocorrem todos os padrões Pj em T, adaptando o algoritmo de Rabin-Karp, com a restrição de que o texto só pode ser processado uma única vez.

def rabinKarp(t, n, ps, mps, m):
  q = 3354393
  d = 256
  dm = 1
  ocorrencias = [0] * mps

  for i in range(m-1):
    dm = (dm*d)%q

  h1 = 0 
  padroes = []
  for padrao in ps:
    for i in range(m):
      h1 = (d*h1 + ord(padrao[i]))%q
    padroes.append(h1)
    h1 = 0
    
  h2 = 0 
  for i in range(m):
    h2 = (d*h2 + ord(t[i]))%q

  for i in range(n-m+1):

    for h1 in range(mps):
      if padroes[h1]==h2:
        ocorrencias[h1] +=1

    if i < n-m:
      h2 = (d*(h2-ord(t[i])*dm) + ord(t[i+m]))%q

  return ocorrencias

t = "A AULA ESTA FICANDO INTERESSANTE FICA NA AULA"
p = ["ESTA", "AULA", "FICA"]

print(rabinKarp(t,len(t),p,len(p),len(p[0])))