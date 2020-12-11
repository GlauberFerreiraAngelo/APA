import numpy as np
arquivo = open('instance2.data','r')

numero_de_postos = 0
numero_de_habitantes = 0
numero_de_postos_escolhidos = 0

arquivo.readline()
numero_de_postos = int(arquivo.readline())
arquivo.readline()
arquivo.readline()
numero_de_habitantes = int(arquivo.readline())
arquivo.readline()
arquivo.readline()
numero_de_postos_escolhidos = int(arquivo.readline())
arquivo.readline()
arquivo.readline()

matriz = []
for n_lin in range(numero_de_postos):
    linha = [] # cria uma linha para a matriz
    teste =  arquivo.readline().split(" ")
    linha.append(int(teste[0]))
    linha.append(int(teste[1]))
    matriz.append(linha)
#print(matriz)

arquivo.readline()
arquivo.readline()

matrizHxP = []
for n_lin in range(numero_de_habitantes):
    linha2 = [] # cria uma linha para a matriz
    teste2 =  arquivo.readline().split(" ")
    for n_col in range(len(teste2)):
        if teste2[n_col] > " ":
            linha2.append(int(teste2[n_col]))
            
    matrizHxP.append(linha2)
#print(matrizHxP)


for n_lin in range(numero_de_postos):
    print(matriz[n_lin][0], matriz[n_lin][1])


aux=""
for n_lin in range(numero_de_habitantes):
    for n_col in range(numero_de_postos):
        aux = aux+""+str(matrizHxP[n_lin][n_col])

print('numero de postos: ', numero_de_postos )
print('numero de habitantes: ', numero_de_habitantes )
print('numero de postos escolhidos: ', numero_de_postos_escolhidos )

arquivo.close()

vetorVerificar = []
quantidade = numero_de_postos_escolhidos
matriz_numero_de_postos_escolhidos = []
while(quantidade > 0):
    maior = 0
    ID_do_posto = 0

    linha2 = [] # cria uma linha para a matriz
    
    Raio_de_cobertura_do_posto = 0
    for n_lin in range(numero_de_postos):
       if(matriz[n_lin][1] >= maior):
           if(matriz[n_lin][0] in vetorVerificar):
               b = 0
           else:    
               maior = matriz[n_lin][1]
               ID_do_posto = matriz[n_lin][0]
               Raio_de_cobertura_do_posto = matriz[n_lin][1]         

    linha2.append(ID_do_posto)
    linha2.append(Raio_de_cobertura_do_posto)
    matriz_numero_de_postos_escolhidos.append(linha2)
    vetorVerificar.append(ID_do_posto)
    quantidade -= 1

print(matriz_numero_de_postos_escolhidos)

def imprime_matriz(matriz):

    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j], end = " ")
    print()

imprime_matriz(matrizHxP)  
