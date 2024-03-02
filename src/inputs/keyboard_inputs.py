import pygame

class KeyboardInputs():
    def keyPressed(self, key):
        if key[pygame.K_w]:
            print("w")
        elif key[pygame.K_a]:
            print("a")
        elif key[pygame.K_s]:
            print("s")
        elif key[pygame.K_d]:
            print("d")
            