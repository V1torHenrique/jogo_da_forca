"""
Projeto - GitHub

    Uma brincadeira chamada de A forca, onde consiste em
advinhar a palavra escolhida tentando acertar as letras
até chegar na palavra. 

"""
from time import sleep

palavra_secreta = 'prosopopéia'
letras_digitadas = []
chances = 5

print('\n--- A Forca ---')

while True:
    jogar = str(input('\nVamos jogar o jogo da Forca <s/n>? ')).strip().lower()[0]   # Verificar se o usuário quer jogar.
    if jogar not in 'sn':
        print('\n[Error] Digite uma resposta válida.')
        jogar = ('\nVamos jogar o jogo da Forca <s/n>?').strip().lower()[0]
    else:
        if jogar == 's':
            print()
            print('='*21)
            print('Então vamos começar..')
            print('='*21)
            sleep(1.5)

            while True:
                letra = str(input('\nDigite uma letra: '))  # Tratar a resposta.
                if not letra.isalpha():
                   print('\n[Error] Digite um caractere válido.')
                else:
                    if len(letra) > 1:
                        print('\n[Error] Só é aceito apenas uma letra por vez.')
                        continue

                    letras_digitadas.append(letra) 
                    
                    if letra in palavra_secreta:     # Verificar se a letra digitada está na palavra.
                        print(f'\nIhuuul, a letra {letra} está presente na palavra.')
                    else:
                        print(f'\nPoxa, {letra} não está presente na palavra.')
                        letras_digitadas.pop()
                    
                    secreta_temporaria = ''  # Adicionar a letra digitada correta na palavra, e se estiver errada, deixa como '_'.
                    for letra_secreta in palavra_secreta:
                        if letra_secreta in letras_digitadas:
                            secreta_temporaria += letra_secreta
                        else:
                            secreta_temporaria += '_'

                    if secreta_temporaria ==  palavra_secreta: # Mostrar se a palavra está correta ou não.
                        print(f'\nParabénsss, você ganhou! A palabra era: "{palavra_secreta}".')
                        break
                    else:
                        print(f'A palavra secreta é: "{secreta_temporaria}".')

                    if letra not in palavra_secreta: # Indicar quantas chances o usuário possue.
                        chances -= 1
                        print(f'Você errou, lhe restam apenas {chances} chances.')

                        if chances == 0:
                            print(f'\nAcabaram sua chances, a palavra era: "{palavra_secreta}".')
                            print('\nMais sorte na próxima!')
                            break
        else:
            print('\nEncerrando..')
            sleep(2)
            print('\nObrigado por jogar, volte sempre! ;)')
            break
