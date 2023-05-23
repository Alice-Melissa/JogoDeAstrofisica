import sys
import pygame
from config import Settings
from imagem import Ship
import funcoes as gf
from pygame.sprite import Group
from alienigena import Alien
from estatisticas import GameStats
from botao import Button
from pontuacao import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'Play')
    sb = Scoreboard(ai_settings, screen, stats)
    clock = pygame.time.Clock()

    while True:
        clock.tick(90)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
