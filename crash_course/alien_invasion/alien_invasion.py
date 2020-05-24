#!/usr/bin/python

import pygame
from pygame.sprite import Group
from Settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object
	pygame.display.init()
	pygame.mixer.quit()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion!")
	bg_color = ai_settings.bg_color
	
	ship = Ship(ai_settings, screen)
	# Group for bullets
	bullets = Group()
	
	while True:		
		# Watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, ship, bullets)	
		ship.update()	
		bullets.update()		
		gf.update_bullets(bullets)		
		gf.update_screen(ai_settings, screen, ship, bullets)
		
		
		
		
run_game()
