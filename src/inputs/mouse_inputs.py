import pygame

class MouseInputs():
    def mousePressed(self, mouse_input, pos):
        if mouse_input[0]:
            print(f"Left Click - {pos}")
        elif mouse_input[1]:
            print(f"Right Click - {pos}")