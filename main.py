import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            if palpite < numero_secreto:
                print("Maior!")
            elif palpite > numero_secreto:
                print("Menor!")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()