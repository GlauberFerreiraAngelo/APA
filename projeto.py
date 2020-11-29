arquivo = open('instance4.data','r')

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
print(matriz)

arquivo.readline()
arquivo.readline()

matrizHxP = []
limpa_espaco = 0;
for n_lin in range(numero_de_habitantes):
    linha2 = [] # cria uma linha para a matriz
    teste2 =  arquivo.readline().split(" ")
    for n_col in range(len(teste2)):
        #ta dando erro aqui por causa que ta passando espaços 
        if teste2[n_col] == " ":
            linha2.append(teste2[n_col])
            
    matrizHxP.append(linha2)
print(matrizHxP)



print('numero de postos: ', numero_de_postos )
print('numero de habitantes: ', numero_de_habitantes )
print('numero de postos escolhidos: ', numero_de_postos_escolhidos )

arquivo.close()
'''
matriz = []
for n_lin in range(numero_de_postos):
    linha = [] # cria uma linha para a matriz
    for n_col in range(2):
        if n_lin == n_col:
            linha.append(1)
        else:
            linha.append(2)
    matriz.append(linha)
print(matriz)

print(matriz[1][1])
'''
