from main.game_window import GamePanel, GameWindow


class Game:
    
    game_window: GameWindow
    
    def __init__(self) -> None:
        self.game_window = GameWindow()