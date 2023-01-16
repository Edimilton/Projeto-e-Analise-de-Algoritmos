# Suponha que lhe seja dada uma nuvem de n pontos, determine a envoltória convexa destes pontos pelo método de Jarvis March (papel de embrulho);

def coord_ext_esq(coordenadas, n):
    minimo = 0
    for i in range(1,n):
        if coordenadas[i][0] == coordenadas[minimo][0]:
            if coordenadas[i][1] > coordenadas[minimo][1]:
                minimo = i
        elif coordenadas[i][0] < coordenadas[minimo][0]:
            minimo = i
    return minimo

  
def sentido(p, q, r):
    sent = ((r[0] - q[0]) * (q[1] - p[1])) - ((r[1] - q[1]) * (q[0] - p[0]))
    if sent < 0: return True
    else: return False

  
def envoltoria_convexa(coordenadas, n):

    if n < 3:
        print("Necessario ter 3 coordenadas")
        return
      
    coord_envolt = []
    l = coord_ext_esq(coordenadas, n)
    p = l
    q = (p + 1) % n
    coord_envolt.append(p)
  
    for i in range(n):
        if sentido(coordenadas[p], coordenadas[i], coordenadas[q]):
            q = i
    p = q
  
    while p != l:
        coord_envolt.append(p)
        q = (p + 1) % n
        for i in range(n):
            if sentido(coordenadas[p], coordenadas[i], coordenadas[q]):
                q = i
        p = q
 
    for i in coord_envolt:
        print(coordenadas[i][0], coordenadas[i][1])
 

def main():
  coordenadas = [(0, 4), (1, 3),(2, 2),(3, 1),(4, 4),(0, 0),(3, 3)]
  n = len(coordenadas)
  envoltoria_convexa(coordenadas, n)

if __name__ == '__main__':
  main()