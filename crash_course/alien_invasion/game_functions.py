import sys
import pygame
from bullet import Bullet



def check_keydown_events(event, ai_settings, screen, ship, bullets):
	""" Responds to key presses """
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		
def check_keyup_events(event, ship):
	""" Response to key releases """
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	""" respond to keypresses and mouse events """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
	# If spacebar is pressed, make a new bullet and add to group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)


def update_bullets(bullets):
	# Clean up bullets that are off the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, bullets):
	screen.fill(ai_settings.bg_color)
	
	# Redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()

		
	# Redraw the ship	
	ship.blitme()
		
	# Make the most recently drawn screen visible
	pygame.display.flip()
