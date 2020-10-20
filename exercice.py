#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import math
import sys
sys.path.insert(1, r"C:\Users\Max\Documents\GitHub\c04_ch6_exercices_MaxenceSigouin\exercice1.py")
from c04_ch6_exercices_MaxenceSigouin.exercice1 import frequence
from turtle import *

# TODO: Définissez vos fonction ici

def compute_volume_and_mass(a=2, b=4, c=2, p=10):
    volume = 4 / 3 * math.pi * a * b * c
    mass = p * volume

    return volume, mass


def dessin_arbre():
    setheading(90)
    color('green')
    draw_branch()
    done()

def draw_branch(branch_len=70, pen_size=7, angle=35):
    if branch_len > 0 and pen_size > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        left(angle * 2)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        back(branch_len)





if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(compute_volume_and_mass())
    (lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("ceci est une phrase")
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("ceci est une phrase"))
    dessin_arbre()
    pass
