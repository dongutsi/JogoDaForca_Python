__author__ = 'dongutsi'
import string
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def printaLetras(palavra):
    for a in palavra:
        print a,
    #print palavra

jogar = 1
print 'Jogo da forca'

while jogar == 1:
    palavra = raw_input('Digite a palavra a ser advinhada\n')
    palavra = list(palavra)
    obscuro = []
    for a in palavra:
        obscuro.append('_')

    printaLetras(obscuro)
    tentativas = len(palavra)
    acertos = 0
    while tentativas != 0:
        letra = raw_input('\nDigite uma letra...\n')
        if(letra in palavra):
            for pos,a in enumerate(palavra):
                if letra == a:
                    obscuro[pos] = letra
                    acertos += 1
            print 'Acertou!'

        else:
            tentativas -= 1
            print ('Errou! Vc ainda tem %d chances de acertar' %tentativas)

        printaLetras(obscuro)
        if acertos == len(obscuro):
            print '\nVoce conseguiu adivinhar a palavra ',string.join(palavra)
            break
    if tentativas == 0:
        print '\nNao foi dessa vez, tente de novo...'

    jogar = input('Jogar de novo?\n1 - Sim\n0 - Nao\n')

print 'Obrigado por jogar!'