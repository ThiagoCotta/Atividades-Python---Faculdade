from random import*
def exibir_matriz(matriz):
    print(" "*5, end="")
    for i in range(dimensao):
        if i < 10:
            print(f"[0{i}]", end="")
        else:
            print(f"[{i}]", end="")
    print()
    for i in range(dimensao):
        if i < 10:
            print(f"[0{i}] [ ", end="")
        else:
            print(f"[{i}] [ ", end="")
        for j in range(dimensao):
            if j == dimensao - 1:
                print(f"{matriz[i][j]} ", end="")
            else:
                print(f"{matriz[i][j]}   ", end="")
        print("]")
    print()


def exibir_matriz_player(matriz_player):
    print(" "*5, end="")
    for i in range(dimensao):
        if i < 10:
            print(f"[0{i}]", end="")
        else:
            print(f"[{i}]", end="")
    print()
    for i in range(dimensao):
        if i < 10:
            print(f"[0{i}] [ ", end="")
        else:
            print(f"[{i}] [ ", end="")
        for j in range(dimensao):
            if j == dimensao - 1:
                print(f"{matriz_player[i][j]} ", end="")
            else:
                print(f"{matriz_player[i][j]}   ", end="")
        print("]")
    print()

print("Facil = 1")
print("Normal = 2")
print("Difícil = 3")
dificuldade = False
while not dificuldade:
    nivel = int(input("Qual você gostaria de jogar? "))
    if nivel >= 1 and nivel <= 3:
        dificuldade = True

nivel = 15

matriz = []
matriz_player = []
dimensao = nivel
bombas = nivel

for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        linha.append(0)
    matriz.append(linha)

for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        linha.append(0)
    matriz_player.append(linha)

for contador in range(bombas):
    linha = randint(0, dimensao -1)
    coluna = randint(0, dimensao -1)
    matriz[linha][coluna] = "☼"
    if linha - 1 >= 0 and coluna - 1 >= 0:
        if matriz[linha-1][coluna-1] == 0:
            matriz[linha-1][coluna-1] = 1
        else:
            if matriz [linha-1][coluna-1] != "☼":
                matriz[linha-1][coluna-1] += 1

    if linha - 1 < dimensao:
        if matriz[linha-1][coluna] == 0:
            matriz[linha-1][coluna] = 1
        else:
            if matriz [linha-1][coluna] != "☼":
                matriz[linha-1][coluna] += 1

    if linha - 1 < dimensao and coluna + 1 < dimensao:
        if matriz[linha-1][coluna+1] == 0:
            matriz[linha-1][coluna+1] = 1
        else:
            if matriz [linha-1][coluna+1] != "☼":
                matriz[linha-1][coluna+1] += 1

    if coluna - 1 < dimensao:
        if matriz[linha][coluna-1] == 0:
            matriz[linha][coluna-1] = 1
        else:
            if matriz[linha][coluna-1] != "☼":
                matriz[linha][coluna-1] += 1

    if coluna + 1 < dimensao:
        if matriz[linha][coluna+1] == 0:
            matriz[linha][coluna+1] = 1
        else:
            if matriz [linha][coluna+1] != "☼":
                matriz[linha][coluna+1] += 1

    if linha + 1 < dimensao and coluna - 1 < dimensao:
        if matriz[linha+1][coluna-1] == 0:
            matriz[linha+1][coluna-1] = 1
        else:
            if matriz [linha+1][coluna-1] != "☼":                
                matriz[linha+1][coluna-1] += 1

    if linha + 1 < dimensao:
        if matriz[linha+1][coluna] == 0:
            matriz[linha+1][coluna] = 1
        else:
            if matriz [linha+1][coluna] != "☼":
                matriz[linha+1][coluna] += 1

    if linha + 1 < dimensao and coluna + 1 < dimensao:
        if matriz[linha+1][coluna+1] == 0:
            matriz[linha+1][coluna+1] = 1
        else:
            if matriz[linha+1][coluna+1] != "☼":                    
                matriz[linha+1][coluna+1] += 1

for j in range(dimensao):
    if matriz[dimensao - 1][j] != 0:
        if matriz[dimensao - 2][j] == 0:
            matriz[dimensao - 1][j] = 0

for i in range(dimensao):
    if matriz[i][dimensao - 1] != 0:
        if matriz[i][dimensao - 2] == 0:
            matriz[i][dimensao - 1] = 0

for i in range(dimensao):
    for j in range(dimensao):
        if matriz[i][j] == 0:
            matriz_player[i][j] = "_"
        else:
            matriz_player[i][j] = "█"


exibir_matriz_player(matriz_player)

bombas_restantes = bombas
vence = False
perder = False
while not perder and not vence:
    acertar = False
    while not acertar:
        print(f"Ainda tem {bombas_restantes} bombas restantes!")
        lin1 = int(input(f"Escolha uma linha de 0 a {dimensao - 1}: "))
        col1 = int(input(f"Escolha uma coluna de 0 a {dimensao - 1}: "))
        print("[1 = ABRIR, 2 = MARCAR]")
        escolhas = int(input("Qual você escolhe? "))
        if lin1 >= 0 and lin1 < dimensao:
            if col1 >= 0 and col1 < dimensao:
                if escolhas == 1 or escolhas == 2:
                    if matriz_player[lin1][col1] != "_":
                        acertar = True
                    else:
                        print("Está casa já está revelada e encontra-se vazia!")
    if escolhas == 1:
        if matriz[lin1][col1] != "☼":
            matriz_player[lin1][col1] = matriz[lin1][col1]
            exibir_matriz_player(matriz_player)
        else:
            perder = True
            print("Você perdeu!")
            exibir_matriz(matriz)
    else:
        if matriz[lin1][col1] == "☼":
            matriz_player[lin1][col1] = "↨"
            exibir_matriz_player(matriz_player)
            bombas_restantes -= 1
            if bombas_restantes == 0:
                vence = True
        else:
            perder = True
            print("Você perdeu!")
            exibir_matriz(matriz)
        
if vence:
    print("Você ganhou!!!!")