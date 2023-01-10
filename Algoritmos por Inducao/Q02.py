from binarytree import BinaryTree

# Dada uma árvore binária de inteiros e dois limites de intervalo, inferior e superior, determine a soma dos elementos da árvore que estão neste intervalo de valores (intervalo fechado).

''''
tree = BinaryTree()
tree.add(9)
tree.add(4)
tree.add(13)
tree.add(5)
tree.add(3)
tree.add(14)
tree.add(10) 
'''

def soma_arv_inter(arv, altura, nivel, lim_inf, lim_sup): 
  if arv == None or nivel > lim_sup:
    return 0
  else:
    if nivel < lim_inf:
      return soma_arv_inter(arv.left, altura, nivel+1, lim_inf, lim_sup) + soma_arv_inter(arv.right, altura, nivel+1, lim_inf, lim_sup)
    else:
      return arv.key + soma_arv_inter(arv.left, altura, nivel+1, lim_inf, lim_sup) + soma_arv_inter(arv.right, altura, nivel+1, lim_inf, lim_sup)


# print(soma_arv_inter(tree.r, tree.height(), 0, 0,0))