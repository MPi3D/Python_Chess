import pygame
from pygame.locals import *
import time
import random
pygame.init()
son = pygame.mixer.Sound("Sons/Bruits/gagné.wav")
son1 = pygame.mixer.Sound("Sons/Bruits/etindre.wav")
son2 = pygame.mixer.Sound("Sons/Voix/Mots/Démarage_en_cour.wav")
son.play()
print('############################################################')
print('##                                                        ##')
print('##     #####   ##    ##   ########    ######     ######   ##')
print('##   ###       ##    ##   ##         ##         ##        ##')
print('##  ##         ##    ##   ##         ##         ##        ##')
print('##  ##         ########   ########    ######     ######   ##')
print('##  ##         ##    ##   ##               ##         ##  ##')
print('##   ###       ##    ##   ##               ##         ##  ##')
print('##     #####   ##    ##   ########    ######     ######   ##')
print('##                                                        ##')
print('############################################################')
print('                           MPi3D                            ')
print('                      Version : 3.5                         ')
time.sleep(4)
print('\n\nDémarrage...\n\n')
son2.play()
time.sleep(2)
time.sleep(random.randint(1, 6))
from threading import Thread

def échec():
    import main
def musique():
    while True :
        nb = random.randint(1, 5)
        if nb == 1:
            pygame.mixer.music.load("Sons/Musiques/Olivaw-Airwaves.wav")
            pygame.mixer.music.play()
            time.sleep(183)
        elif nb == 2:
            pygame.mixer.music.load("Sons/Musiques/KaiEngel-TheRun-02Run.wav")
            pygame.mixer.music.play()
            time.sleep(241)
        elif nb == 3:
            pygame.mixer.music.load("Sons/Musiques/Jens_East_-_Daybreak_feat_Henk.wav")
            pygame.mixer.music.play()
            time.sleep(282)
        elif nb == 4:
            pygame.mixer.music.load("Sons/Musiques/Jaunter-Reset.wav")
            pygame.mixer.music.play()
            time.sleep(191)
        elif nb == 5:
            pygame.mixer.music.load("Sons/Musiques/04_binaerpilot_-_cornered_promo.wav")
            pygame.mixer.music.play()
            time.sleep(171)

        
t1=Thread(target=musique,args=())      
t2=Thread(target=échec,args=())

t1.start()
t2.start()

t2.join()
pygame.mixer.music.fadeout(1000)
son1.play()
quit(0)
