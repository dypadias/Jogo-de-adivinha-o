# Jogo de advinhação

secreto = input('Digite uma palavra secreta:')
secreto = secreto.upper()
digitada = []
chances = 3
while True:

    if chances <= 0:
        print('Voce perdeu')
        break

    letra = input('Digite uma letra: ')
    letra = letra.upper()

    if len(letra) > 1 :
        print('Isso não vale, digite apenas uma letra')
        continue

    digitada.append(letra.upper())

    if letra in secreto:
        print(f'Letra {letra} existe na palavra secreta.')
    else:
        print(f'A letra {letra} NÃO existe na palvra secreta')
        digitada.pop()
        chances-= 1
        print(f'Voce tem ainda {chances} chances!')
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Voce ganhou!! A palavra secreta é {secreto}')
        break
    else:
        print(secreto_temporario)