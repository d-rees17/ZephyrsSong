from __future__ import annotations

import pygame
import sys
import time

from typing import List

from inputs.keyboard_inputs import KeyboardInputs
from inputs.mouse_inputs import MouseInputs


class GameWindow:
    
    game_panel: GamePanel
    
    def __init__(self) -> None:
        pygame.init()
        # Set Window Size - Width, Height
        size = (400, 400)
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.game_panel = GamePanel(screen)
        pygame.display.set_caption("Zephyr's Song")

        # Initialise game clock and delta
        clock = pygame.time.Clock()
        last_delta = time.time_ns()
        
        # Grab keyboard Focus
        pygame.event.set_keyboard_grab(True)
        
        # Window Loop - Keeps it running until closed
        running = True
        while running:
            # FPS check
            clock.tick(60)
            print(f"FPS: {clock.get_fps()}")
            
            # Delta time for lagg handling
            delta_check = time.time_ns()
            delta = (delta_check - last_delta) / 1_000_000_000
            last_delta = delta_check
            
            # Set Background Colour
            bg_colour = "blue"
            screen.fill(bg_colour)
            
            # Check inputs
            self.game_panel.check_key_inputs()
            self.game_panel.check_mouse_inputs()
            
            # Render components
            self.game_panel.render()
            
            # Update the game display
            self.game_panel.update(delta)
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
    keyboard_listener: KeyboardInputs
    mouse_listener: MouseInputs
    objects: List[Player]
    
    def __init__(self, game_surface: pygame.Surface) -> None:
        self.game_surface = game_surface
        self.keyboard_listener = KeyboardInputs()
        self.mouse_listener = MouseInputs()
        self.objects = [Player()]
    
    def render(self) -> None:
        for obj in self.objects:
            obj.draw(self.game_surface)
        
    def update(self, delta: float) -> None:
        for obj in self.objects:
            obj.move(100, 100, delta)
    
    def check_key_inputs(self) -> None:
        keyboard_inputs = pygame.key.get_pressed()
        self.keyboard_listener.keyPressed(keyboard_inputs)
        
    def check_mouse_inputs(self) -> None:
        mouse_inputs = pygame.mouse.get_pressed()
        mouse_position = pygame.mouse.get_pos()
        self.mouse_listener.mousePressed(mouse_inputs, mouse_position)
        
class Player():
    player: pygame.Rect
    
    def __init__(self) -> None:
        self.player = pygame.rect.Rect((30, 30, 60, 60))
    
    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, "green", self.player)
    
    def move(self, x: int, y: int, delta: float) -> None:
        x = x * delta
        y = y * delta
        self.player = self.player.move(x,y)
        
    
                
        