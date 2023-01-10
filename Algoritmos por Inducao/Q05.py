# Dada uma expressão contendo parênteses, literais e operadores aritméticos, elabore um algoritmo para determinar se a expressão está com os parênteses balanceados, ou seja, se para cada parêntese aberto há um parêntese fechando e se os pares de parênteses estão adequadamente aninhados. Você pode supor que a expressão será fornecida como uma string e que a reposta de seu algoritmo será um booleano, onde True significa que a expressão é correta e False, incorreta.

def express_balanc(exp):
  cont = 0

  for item in exp:
    if item == '(':
      cont += 1
    elif item == ')':
      cont -= 1
    if cont < 0:
      break

  if cont == 0:
    return True
  else:
    return False

# exp = ')(a + b)) + (c * d)'

#print(express_balanc(exp))