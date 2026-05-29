#OP.VET_LT02.4
#Declaração de variáveis

#Início

import random

def func_media (vetor):
    soma= 0
    med: float = 0
    for i in vetor:
        soma += i
    med= (soma / len (vetor))
    print (f"A média das notas do grupo, equivale a: {med: .2f}")
    return med


def func_acima (vetor):
    lowm = []
    cont: int = 0
    med= func_media (vetor)
    for i in range (len(vetor)):
        if (vetor [i] >= med):
            cont += 1
        else:
            lowm.append (i+1)
    print ("A quantidade de alunos acima foram:", cont)
    print ("As posições dos alunos abaixo", lowm)
        
        

def main ():
    notas = []
    tamanho = 30   
    num: int = 0

    for i in range (tamanho):
        num = (random.randint (0, 10000))
        num = num / 1000
        notas.append (num)
    
    func_acima (notas)

if (__name__ == "__main__"):
    main ()
