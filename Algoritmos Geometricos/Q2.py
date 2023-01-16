# Considere um conjunto de n ruas de uma cidade, todas elas definidas por uma equação de reta, ax + by + c = 0. Você tem um amigo que mora a certa distância de você. Seu objetivo é elaborar um algoritmo para determinar qual o menor número de ruas que terá que cruzar para sair da sua casa e chegar à casa de seu amigo. Por exemplo, para as retas x = 0, y = 0 e x + y - 2 = 0, sua casa na posição (1,1) e a de seu amigo na posição (-3,-1), você terá que cruzar duas ruas, que são as definidas pelas retas x = 0 e y = 0.

def cruzar_ruas(inicio, fim, retas, n):
    ruas = 0
    for i in range(n):
        if ((retas[i][0]* inicio[0] + retas[i][1] * inicio[1] + retas[i][2]) > 0):
          sinal_ini = 1
        else: 
          sinal_ini = -1
        if ((retas[i][0]* fim[0] + retas[i][1] * fim[1] + retas[i][2]) > 0):
          sinal_fim = 1
        else: 
          sinal_fim = -1
          
        if sinal_ini * sinal_fim < 0:
            ruas += 1
    print("Numero de ruas cruzadas:",ruas)

inicio = (1, 1)
fim = (-2, -1)
  
retas = [(1, 0, 0),(0, 1, 0),(1, 1, -2)]
n = len(retas)

cruzar_ruas(inicio, fim, retas, n)