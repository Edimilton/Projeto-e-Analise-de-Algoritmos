# Suponha que você tenha um jogo de encaixe que consiste em um tabuleiro na forma de uma grade reticulada de células de tamanho 1 cm ⨉ 1 cm e peças de tamanho 1cm ⨉ 1cm, que podem ser coloridas e servem para formar figuras no tabuleiro. Elabore um algoritmo para determinar a área e perímetro de figuras montadas neste tabuleiro.

def area_perimetro(tabuleiro, linhas, colunas):
    area = 0
    perimetro = 0
    for i in range(linhas):
        for j in range(colunas):
          if tabuleiro[i][j] == 1:
            lados_ocupados = 0
            if i > 0 and tabuleiro[i - 1][j] == 1:
                lados_ocupados += 1
            if i < linhas-1 and tabuleiro[i + 1][j] == 1:
                lados_ocupados += 1
            if j > 0 and tabuleiro[i][j - 1] == 1:
                lados_ocupados += 1
            if j < colunas-1 and tabuleiro[i][j + 1] == 1:
                lados_ocupados += 1
            perimetro += 4 - lados_ocupados
            area += 1
    print("Perimetro da figura:",perimetro)
    print("Area da figura:",area)


def main():
  tabuleiro = [[0, 1, 1, 0, 0],
               [0, 1, 1, 0, 0],
               [0, 1, 1, 1, 0],
               [0, 0, 1, 1, 0],
               [1, 0, 0, 0, 0]]
  
  linhas = 5
  colunas = 5
  area_perimetro(tabuleiro, linhas, colunas)

if __name__ == '__main__':
  main()