import pygame
WINDOW_NAME = "GADS DEVELOPERS"
GAME_TITLE1 = "GHOST HUNTER"
GAME_TITLE2 = "-GADS DEVELOPERS-"
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
FPS = 90
DRAW_FPS = True
BUTTONS_SIZES = (240, 90)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
GHOSTS_SIZES = (100, 60)
GHOST_SIZE_RANDOMIZE = (1,2) # for each new GHOST, it will multiply the size with an random value beteewn X and Y
WITCH_SIZES = (100,100)
WITCH_SIZE_RANDOMIZE = (1.2, 1.5)
DRAW_HITBOX = False # will draw all the hitbox
ANIMATION_SPEED = 0.08 # the frame of the insects will change every X sec
GAME_DURATION = 60 # the game will last X sec
GHOSTS_SPAWN_TIME = 1
GHOSTS_MOVE_SPEED = {"min": 1, "max": 5}
WITCH_PENALITY = 1 # will remove X of the score of the player (if he kills a WITCH)
COLORS = {"title": (38, 61, 39), "score": (38, 61, 39), "timer": (38, 61, 39),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)}} # second is the color when the mouse is on the button
MUSIC_VOLUME = 0.5 # value between 0 and 1
SOUNDS_VOLUME = 1
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 50)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 120)
