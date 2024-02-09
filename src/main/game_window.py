from __future__ import annotations

import pygame
import sys


class GameWindow:
    
    game_panel: GamePanel
    
    def __init__(self) -> None:
        pygame.init()
        # Set Window Size - Width, Height
        size = (400, 400)
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption("Zephyr's Song")
        
        self.game_panel = GamePanel(screen)
        running = True
        
        # Window Loop - Keeps it running until closed
        while running:
            self.game_panel.paintComponent()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Exit Game Loop
                    running = False
                if event.type == pygame.VIDEORESIZE:
                    # Resize Window
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        pygame.quit()

class GamePanel:
    
    game_surface: pygame.Surface
    
    def __init__(self, game_surface: pygame.Surface) -> None:
        self.game_surface = game_surface
    
    def paintComponent(self) -> None:
        self.game_surface.fill((255,255,255))
        pygame.draw.rect(self.game_surface,(255,0,0),pygame.Rect(30, 30, 60, 60))
    
                
        