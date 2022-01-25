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


def exibir_bot_matriz(bot_matriz):
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
                print(f"{bot_matriz[i][j]} ", end="")
            else:
                print(f"{bot_matriz[i][j]}   ", end="")
        print("]")
    print()


def exibir_matriz_cega(matriz):
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
                print(f"{matriz_cega[i][j]} ", end="")
            else:
                print(f"{matriz_cega[i][j]}   ", end="")
        print("]")
    print()


dificuldade = False
while not dificuldade:
    tamanho = int(input("1 = Fácil, 2 = Normal e 3 = Difícil: "))
    if tamanho <= 0 or tamanho >= 4:
        print("Dificuldade inválida")
    else:
        dificuldade = True
        if tamanho == 1:
            dimensao = 200
        else:
            if tamanho == 2:
                dimensao = 25
            else:
                dimensao = 30

matriz = []
bot_matriz = []
matriz_cega = []

for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        linha.append("░")
    matriz.append(linha)

for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        linha.append(0)
    bot_matriz.append(linha)

for i in range(dimensao):
    linha = []
    for j in range(dimensao):
        linha.append("░")
    matriz_cega.append(linha)

couracado = 5
cruzado = 4
destroyer = 2
submarino = 1
hydroaviao = 3

embarcacoes_valor = [couracado, cruzado, cruzado, destroyer, destroyer, destroyer, submarino, submarino, submarino, submarino, hydroaviao, hydroaviao, hydroaviao, hydroaviao]
embarcacoes_nome = ["agua","submarino", "destroyer", "hydroaviao", "cruzado", "couraçado"]

for contador in range(len(embarcacoes_valor)):
    acertar = False
    while not acertar:
        vaga = 0
        posicao_linha = randint(0, dimensao - 1)
        posicao_coluna = randint(0, dimensao -1)
        posicao = randint(1,2)
        if posicao == 1:
            if bot_matriz[posicao_linha][posicao_coluna] == 0:
                if posicao_linha + embarcacoes_valor[contador] + 1 < dimensao and posicao_coluna - 1 >= 0 and posicao_coluna + 1 < dimensao:
                    for verificar1 in range((embarcacoes_valor[contador])+2):
                        if bot_matriz[posicao_linha - 1 + verificar1][posicao_coluna - 1] == 0 and bot_matriz[posicao_linha + verificar1][posicao_coluna] == 0 and bot_matriz[posicao_linha + verificar1][posicao_coluna + 1] == 0:
                            vaga += 1
                            if vaga == embarcacoes_valor[contador] + 2:
                                for preencher_barco1 in range(embarcacoes_valor[contador]):
                                    bot_matriz[posicao_linha + preencher_barco1][posicao_coluna] = embarcacoes_valor[contador]
                                acertar = True
        else:
            if bot_matriz[posicao_linha][posicao_coluna] == 0:
                if posicao_coluna + embarcacoes_valor[contador] + 1 < dimensao and posicao_linha - 1 >= 0 and posicao_linha + 1 < dimensao and posicao_coluna - 1 >= 0:
                    for verificar2 in range((embarcacoes_valor[contador])+2):
                        if bot_matriz[posicao_linha - 1][posicao_coluna - 1 + verificar2] == 0 and bot_matriz[posicao_linha + 1][posicao_coluna -1 + verificar2] == 0 and bot_matriz[posicao_linha][posicao_coluna -1 + verificar2] == 0:
                            vaga += 1
                            if vaga == embarcacoes_valor[contador] + 2:
                                for preencher_barco2 in range(embarcacoes_valor[contador]):
                                    bot_matriz[posicao_linha][posicao_coluna + preencher_barco2] = embarcacoes_valor[contador]
                                acertar = True

print("Escolha a posição das suas embarcações!")
exibir_matriz(matriz)

for contador in range(len(embarcacoes_valor)):
    acertar = False
    vaga = 0
    while not acertar:
        #/////posição 1//////
        c_esquerda_vaga1 = False
        c_centro_vaga1 = False
        c_direita_vaga1 = False
        b_linha_vaga = False
        c_linha_vaga = False
        #/////posição 2//////
        linha_vaga_cima2 = False
        linha_vaga_centro2 = False
        linha_vaga_baixo2 = False
        e_coluna_vaga2 =  False
        d_coluna_vaga2 = False
        print(f"Esse é o formato da sua embarcação!")
        print("█ " * embarcacoes_valor[contador])
        print("1 = Vertical")
        print("2 = Horizontal")
        posicao = int(input("Qual posição você deseja? "))
        posicao_linha = int(input(f"Escolha a linha: "))
        posicao_coluna = int(input(f"Escolha a coluna: "))
        if posicao < 1 or posicao > 2:
            print("Posição inválida")
        else:
            if posicao_linha >= dimensao or posicao_coluna >= dimensao:
                print("Valor inválido!")
            else:
                if matriz[posicao_linha][posicao_coluna] != "░":
                    print("Casa inválida!")
                else:
                    if posicao == 1:
                        if posicao_linha + embarcacoes_valor[contador] > dimensao:
                            print("Linha inválida!")
                        else:
                            vaga = 0
                            if posicao_coluna - 1 >= 0:
                                for verificar_coluna_esquerda in range(embarcacoes_valor[contador]):
                                    if matriz[posicao_linha + verificar_coluna_esquerda][posicao_coluna - 1] == "░":
                                        vaga += 1
                                        if vaga == embarcacoes_valor[contador]:
                                            c_esquerda_vaga1 = True
                            else:
                                c_esquerda_vaga1 = True

                            vaga = 0
                            for verificar_coluna_centro in range(embarcacoes_valor[contador]):
                                if matriz[posicao_linha + verificar_coluna_centro][posicao_coluna] == "░":
                                    vaga += 1
                                    if vaga == embarcacoes_valor[contador]:
                                        c_centro_vaga1 = True

                            vaga = 0
                            if posicao_coluna + 1 < dimensao:
                                for verificar_coluna_direita in range(embarcacoes_valor[contador]):
                                    if matriz[posicao_linha + verificar_coluna_direita][posicao_coluna + 1] == "░":
                                        vaga += 1
                                        if vaga == embarcacoes_valor[contador]:
                                            c_direita_vaga1 = True
                            else:
                                c_direita_vaga1 = True

                            if posicao_linha - 1 >= 0:
                                c_esquerda_linha = False
                                c_centro_linha = False
                                c_direita_linha = False
                                if posicao_coluna - 1 >= 0:
                                    if matriz[posicao_linha - 1][posicao_coluna - 1] == "░":
                                        c_esquerda_linha = True
                                else:
                                    c_esquerda_linha = True

                                if matriz[posicao_linha - 1][posicao_coluna] == "░":
                                    c_centro_linha = True

                                if posicao_coluna + 1 < dimensao:
                                    if matriz[posicao_linha - 1][posicao_coluna + 1] == "░":
                                        c_direita_linha = True
                                else:
                                    c_direita_linha = True
                                    
                                if c_esquerda_linha and c_centro_linha and c_direita_linha:
                                    c_linha_vaga = True
                            else:
                                c_linha_vaga = True
                            
                            if posicao_linha + 1 + embarcacoes_valor[contador] < dimensao:
                                b_esquerda_linha = False
                                b_centro_linha = False
                                b_direita_linha = False
                                if posicao_coluna - 1 >= 0:
                                    if matriz[posicao_linha + 1 + embarcacoes_valor[contador]][posicao_coluna - 1] == "░":
                                        b_esquerda_linha = True
                                else:
                                    b_esquerda_linha = True

                                if matriz[posicao_linha + 1 + embarcacoes_valor[contador]][posicao_coluna] == "░":
                                    b_centro_linha = True

                                if posicao_coluna + 1 < dimensao:
                                    if matriz[posicao_linha + 1 + embarcacoes_valor[contador]][posicao_coluna + 1] == "░":
                                        b_direita_linha = True
                                else:
                                    b_direita_linha = True

                                if b_esquerda_linha and b_centro_linha and b_direita_linha:
                                    b_linha_vaga = True
                            else:
                                b_linha_vaga = True

                            if c_esquerda_vaga1 and c_centro_vaga1 and c_direita_vaga1 and c_linha_vaga and b_linha_vaga:
                                for preencher in range(embarcacoes_valor[contador]):
                                    matriz[posicao_linha + preencher][posicao_coluna] = "█"
                                    acertar = True
                    else:
                        if posicao_coluna + embarcacoes_valor[contador] > dimensao:
                            print("Coluna inválida!")
                        else:
                            vaga = 0
                            if posicao_linha - 1 >= 0:
                                for verificar_linha_cima in range(embarcacoes_valor[contador]):
                                    if matriz[posicao_linha - 1][posicao_coluna + verificar_linha_cima] == "░":
                                        vaga += 1
                                        if vaga == embarcacoes_valor[contador]:
                                            linha_vaga_cima2 = True
                            else:
                                linha_vaga_cima2 = True

                            vaga = 0
                            for verificar_linha_centro in range(embarcacoes_valor[contador]):
                                if matriz[posicao_linha][posicao_coluna + verificar_linha_centro] == "░":
                                    vaga += 1
                                    if vaga == embarcacoes_valor[contador]:
                                        linha_vaga_centro2 = True

                            vaga = 0
                            if posicao_linha + 1 < dimensao:
                                for verificar_linha_baixo in range(embarcacoes_valor[contador]):
                                    if matriz[posicao_linha + 1][posicao_coluna + verificar_linha_baixo] == "░":
                                        vaga += 1
                                        if vaga == embarcacoes_valor[contador]:
                                            linha_vaga_baixo2 = True
                            else:
                                linha_vaga_baixo2 = True

                            if posicao_coluna - 1 >= 0:
                                e_cima_coluna = False
                                e_centro_coluna = False
                                e_baixo_coluna = False
                                if posicao_linha - 1 >= 0:
                                    if matriz[posicao_linha - 1][posicao_coluna - 1] == "░":
                                        e_cima_coluna = True
                                else:
                                    e_cima_coluna = True

                                if matriz[posicao_linha][posicao_coluna - 1] == "░":
                                    e_centro_coluna = True
                                if posicao_linha + 1 < dimensao:
                                    if matriz[posicao_linha + 1][posicao_coluna - 1] == "░":
                                        e_baixo_coluna = True
                                else:
                                    e_baixo_coluna = True

                                if e_cima_coluna and e_centro_coluna and e_baixo_coluna:
                                    e_coluna_vaga2 = True
                            else:
                                e_coluna_vaga2 = True

                            if posicao_coluna + 1 + embarcacoes_valor[contador] < dimensao:
                                d_cima_coluna = False
                                d_centro_coluna = False
                                d_baixo_coluna = False
                                if posicao_linha - 1 >= 0:
                                    if matriz[posicao_linha - 1][posicao_coluna + 1 + embarcacoes_valor[contador]] == "░":
                                        d_cima_coluna = True
                                else:
                                    d_cima_coluna = True

                                if matriz[posicao_linha][posicao_coluna + 1 + embarcacoes_valor[contador]] == "░":
                                    d_centro_coluna = True
                                if posicao_linha + 1 < dimensao:
                                    if matriz[posicao_linha + 1][posicao_coluna + 1 + embarcacoes_valor[contador]] == "░":
                                        d_baixo_coluna = True
                                else:
                                    d_baixo_coluna = True

                                if d_cima_coluna and d_centro_coluna and d_baixo_coluna:
                                    d_coluna_vaga2 = True
                            else:
                                d_coluna_vaga2 = True

                            if linha_vaga_cima2 and linha_vaga_centro2 and linha_vaga_baixo2 and e_coluna_vaga2 and d_coluna_vaga2:
                                for preencher in range(embarcacoes_valor[contador]):
                                    matriz[posicao_linha][posicao_coluna + preencher] = "█"
                                    acertar = True
                                
    exibir_matriz(matriz)
exibir_matriz_cega(matriz_cega)

explodir_p = False
explodir_b = False
while not explodir_p and not explodir_b:
    derrota_p = 0
    derrota_b = 0
    p_bomba_linha = int(input("Qual a linha você quer atacar? "))
    p_bomba_coluna = int(input("Qual coluna? "))
    if bot_matriz[p_bomba_linha][p_bomba_coluna] == 0:
        matriz_cega[p_bomba_linha][p_bomba_coluna] = "~"
        exibir_matriz_cega(matriz_cega)
        print("AGUA")
    else:
        matriz_cega[p_bomba_linha][p_bomba_coluna] = "☼"
        exibir_matriz_cega(matriz_cega)
        print(f"Você acertou {embarcacoes_nome[bot_matriz[p_bomba_linha][p_bomba_coluna]]}")
    for verificar_vencedor_i in range(dimensao):
        for verificar_vencedor_j in range(dimensao):
            if matriz_cega[verificar_vencedor_i][verificar_vencedor_j] == "☼":
                derrota_p += 1
                if derrota_p == 3:
                    explodir_p = True
    if not explodir_p:
        b_bomba_linha = randint(0, dimensao -1)
        b_bomba_coluna = randint(0, dimensao -1)
        if matriz[b_bomba_linha][b_bomba_coluna] == "░":
            exibir_matriz(matriz)
            print("O seu inimigo errou!")
        else:
            matriz[b_bomba_linha][b_bomba_coluna] = "☼"
            exibir_matriz(matriz)
            print("O seu inimigo acertou sua navegação!")
        for verificar_vencedor_i_b in range(dimensao):
            for verificar_vencedor_j_b in range(dimensao):
                if matriz[verificar_vencedor_i_b][verificar_vencedor_j_b] == "☼":
                    derrota_b += 1
                    if derrota_b == 3:
                        explodir_b = True

exibir_bot_matriz(bot_matriz)