player1 = str(input("Qual o nome do Player 1: "))
player2 = str(input("Qual o nome do Player 2: "))
jogo_da_velha = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
jogadas_restantes = 9
fim = False
acertar = False
certo = 0
inverter = [2,1,0] #Utilizada para inverter a diagonal2
vez = []
vez.append(player1)
vez.append(player2)
while not fim:
    for jogador in range(2):
        if not fim:
            acertar = False
            print("=-" * 10)
            print(f"Vez do jogador {vez[jogador]}")
            print("=-" * 10)
            while not acertar:
                linha = (int(input(f"{vez[jogador]}, qual linha você escolhe? ")))
                coluna = (int(input("E qual a coluna? ")))
                if jogo_da_velha[linha][coluna] == "_":
                    if jogador == 0:
                        jogo_da_velha[linha][coluna] = "X"
                        acertar = True
                    else:
                        jogo_da_velha[linha][coluna] = "O"
                        acertar = True
                    for mostrar in range(3):
                        print(" ".join(jogo_da_velha[mostrar]), end='')
                        print()
                else:
                    print("Essa casa já está marcada!")
                    print("=-" * 10)
            for linha1 in range(3):
                if jogo_da_velha[0][linha1] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for linha2 in range(3):
                if jogo_da_velha[1][linha2] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for linha3 in range(3):
                if jogo_da_velha[2][linha3] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for diagonal1 in range(3):
                if jogo_da_velha[diagonal1][diagonal1] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for diagonal2 in range(2, -1, -1):
                if jogo_da_velha[diagonal2][inverter[diagonal2]] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for coluna1 in range(3):
                if jogo_da_velha[coluna1][0] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for coluna1 in range(3):
                if jogo_da_velha[coluna1][1] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for coluna1 in range(3):
                if jogo_da_velha[coluna1][2] == "X":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for linha1 in range(3):
                if jogo_da_velha[0][linha1] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for linha2 in range(3):
                if jogo_da_velha[1][linha2] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for linha3 in range(3):
                if jogo_da_velha[2][linha3] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for diagonal1 in range(3):
                if jogo_da_velha[diagonal1][diagonal1] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for diagonal2 in range(2, -1, -1):
                if jogo_da_velha[diagonal2][inverter[diagonal2]] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for coluna1 in range(3):
                if jogo_da_velha[coluna1][0] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for coluna1 in range(3):
                if jogo_da_velha[coluna1][1] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            for coluna1 in range(3):
                if jogo_da_velha[coluna1][2] == "O":
                    certo += 1
                    if certo == 3:
                        fim = True
            certo = 0
            if fim:
                print("=-" * 10)
                print(f"O jogador {vez[jogador]} ganhou!")
                print("=-" * 10)
                print("=-=-=-=-FIM=-=-=-=-")
            jogadas_restantes -= 1
            if jogadas_restantes == 0:
                print("O jogo deu velha")
                fim = True