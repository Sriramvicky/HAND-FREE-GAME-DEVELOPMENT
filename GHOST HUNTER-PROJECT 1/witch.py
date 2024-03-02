import random
import image
from settings import *
from ghost import Ghost
class Witch(Ghost):
    def __init__(self):
        random_size_value = random.uniform(WITCH_SIZE_RANDOMIZE[0], WITCH_SIZE_RANDOMIZE[1])
        size = (int(WITCH_SIZES[0] * random_size_value), int(WITCH_SIZES[1] * random_size_value))
        moving_direction, start_pos = self.define_spawn_pos(size)
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0]//1.4, size[1]//1.4)
        self.images = [image.load(f"Assets/witch/{nb}.png", size=size, flip=moving_direction=="right") for nb in range(1, 7)] # load the images
        self.current_frame = 0
        self.animation_timer = 0
    def kill(self, ghosts): # remove the ghost from the list
        ghosts.remove(self)
        return -WITCH_PENALITY

import cv2
import mediapipe as mp
from settings import *

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
class HandTracking:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.hand_x = 0
        self.hand_y = 0
        self.results = None
        self.hand_closed = False
    def scan_hands(self, image):
        rows, cols, _ = image.shape
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        self.results = self.hand_tracking.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        self.hand_closed = False
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y
                self.hand_x = int(x * SCREEN_WIDTH)
                self.hand_y = int(y * SCREEN_HEIGHT)
                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y
                if y1 > y:
                    self.hand_closed = True
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        return image
    def get_hand_center(self):
        return (self.hand_x, self.hand_y)
    def display_hand(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)
    def is_hand_closed(self):
        pass
