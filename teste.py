# coding=UTF-8

from pybot import *

# desenha o tabuleiro
mundo = Mundo(altura=8, largura=8, espera=True)
Robot(4, 1)

dizer(u"Juca vai à feira")

while True:
    andar(acima)