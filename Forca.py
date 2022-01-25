start = str(input("Escolha uma palavra: "))
mostrar_acertos = []
palavra = []
erros = 6
acertos = len(start)
fim = False
digitadas = []

for posicao, receber in enumerate(start):
    mostrar_acertos.append("_")
    palavra.append(receber)
print("=-=" * 10)
while fim == False:
    letra = str(input(f"Digite uma letra, você pode errar {erros} vezes: "))
    if letra in palavra:
        digitadas.append(letra)
        for p, l in enumerate(palavra):
            if letra == l:
                del mostrar_acertos[p]
                mostrar_acertos.insert(p,letra)
                print(mostrar_acertos)
                acertos -= 1
                if acertos == 0:
                    print("Parabéns, você ganhou!!!!")
                    fim = True
    else:
        digitadas.append(letra)
        erros -= 1
        if erros == 0:
            print("Você errou 6 vezes!")
            fim = True