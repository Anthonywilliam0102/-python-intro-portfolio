import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    print("Jogo de Adivinhação: Tente acertar o número entre 1 e 10")

    while True:
        chute = int(input("Digite seu chute: "))
        tentativas += 1
        if chute == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif chute < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

jogo_adivinhacao()