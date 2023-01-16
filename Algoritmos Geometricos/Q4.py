# Seja um conjunto de n retângulos, que se interceptam dois a dois, e cujas arestas são paralelas aos eixos x ou y. Elabore um algoritmo para determinar a área do retângulo de interseção dos retângulos de entrada.

def inter_dois_retang(A, B):
    AX = max(A[0][0], B[0][0])
    AY = max(A[0][1], B[0][1])
    BX = min(A[1][0], B[1][0])
    BY = min(A[1][1], B[1][1])
    return [(AX,AY),(BX,BY)]

def interseccao(retangulos, n):
    retangulo = retangulos[0]
    for i in range(1,n):
      retangulo = inter_dois_retang(retangulo, retangulos[i])
    print("Area da interseccao:",(retangulo[1][0] - retangulo[0][0]) * (retangulo[1][1] - retangulo[0][1]))

A = [(2, 1), (5, 5)]
B = [(3, 2), (5, 7)]
C = [(4, 3), (7, 9)]
retangulos = [A,B,C]


interseccao(retangulos,len(retangulos))
