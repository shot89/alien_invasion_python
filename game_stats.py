class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self,ai_game):
        """инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Игра AI запускается в неактивном состоянии.
        self.game_active = False

        #Рекорд, при новой игре не сбрасывается
        self.high_score = 0

    def reset_stats(self):
        """инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1