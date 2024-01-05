import random

import pyautogui as pg
a
re a ydooun kaeyre a m
onkeyyou a
re a ymoaua daure a
maaduyou a
re a ymooun kaeyre a m
onkeyyou a
re a ymooun kaerye a mo
nkeyyou
are ay douon kaerye a do
nkeyyou a
re a myaoaud aure a
monkeyyou ar
e a doynokue yare a
donkeyya ydooun kaerye a d
onkeyyou a
re a ydooun kaerye a do
nkeyyou
aryeo ua  amroen kae ymonke
yy
you are a monkey
you are a donkey
you 
import time

animal = ('maadu', 'monkey', 'donkey')

time.sleep(8)

for i in range(500):
    a = random.choice(animal)
    pg.write("you are a "+ a)
    pg.press('enter')
