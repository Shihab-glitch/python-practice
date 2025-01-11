import pygame
from pygame.locals import *
import sys

pygame.init()

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
print ("Framebuffer size: %d x %d" % (size[0], size[1]))
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
sysfont = pygame.font.SysFont('Times New Roman', 150)

hello = sysfont.render("Game of Alphabet", False, (0,0,0))

def screen_opening():
    screen.fill((144, 238, 144))
    screen.blit(hello, (size[0]/5 , size[1]/3))
    pygame.display.update()

def display_word(word):
    print(word)
    display_word = sysfont.render(word, False, (0,0,0))

    screen.fill((173, 216, 230))
    screen.blit(display_word, (size[0]/4 , size[1]/3))
    pygame.display.update()

if __name__ == '__main__':
    screen_opening()

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_a:
                    display_word('A for Apple & Art')
                if event.key == K_b:
                    display_word('B for Ball & Boy')

                if event.key == K_c:
                    display_word('C for Cat & Car')

                if event.key == K_d:
                    display_word('D for Dog & Dim')

                if event.key == K_e:
                    display_word('E for Earth & Eye')

                if event.key == K_f:
                    display_word('F for Fish & Fan')

                if event.key == K_g:
                    display_word('G for Game & Gem')

                if event.key == K_h:
                    display_word('H for Hat & Hop')

                if event.key == K_i:
                    display_word('I for Ice & Ink')

                if event.key == K_j:
                    display_word('J for Jar & Jam')

                if event.key == K_k:
                    display_word('K for Kite & Kin')

                if event.key == K_l:
                    display_word('L for Lion & Life')

                if event.key == K_m:
                    display_word('M for Man & Mass')

                if event.key == K_n:
                    display_word('N for Nuts & Nap')

                if event.key == K_o:
                    display_word('O for One & Oats')

                if event.key == K_p:
                    display_word('P for Pet & Pie')

                if event.key == K_q:
                    display_word('Q for Queen & Quill')

                if event.key == K_r:
                    display_word('R for Race & Real')

                if event.key == K_s:
                    display_word('S for Star & Step')

                if event.key == K_t:
                    display_word('T for Top & True')

                if event.key == K_u:
                    display_word('U for Up & Us')

                if event.key == K_v:
                    display_word('V for Van & Villa')

                if event.key == K_w:
                    display_word('W for Watch & Will')

                if event.key == K_x:
                    display_word('X for Xmas & Xerox')

                if event.key == K_y:
                    display_word('Y for Year & Yell')

                if event.key == K_z:
                    display_word('Z for Zoo & Zeal')

                if event.key == K_ESCAPE:
                    sys.exit()