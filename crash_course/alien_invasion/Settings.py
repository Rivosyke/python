class Settings():
	""" A class to store all settings in Alien Invasion """
	
	def __init__(self):
		""" Init the game's settings """
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		# Ship Settings
		self.ship_speed_factor = 2
		
		# Bullet Settings
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 8
		self.bullet_color = 60,60,60
		self.bullets_allowed = 4
		
		
