import pyautogui
import cv2
import numpy as np
import keyboard 
import time  

pyautogui.FAILSAFE = False

def get_screenshot():
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def is_within_excluded_area(x, y, excluded_areas):
    for area in excluded_areas:
        ex, ey, ew, eh = area
        if ex <= x <= ex + ew and ey <= y <= ey + eh:
            return True
    return False

def find_enemy_by_color(image, lower_color, upper_color, excluded_areas):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        center_x, center_y = int(x + w / 2), int(y + h / 2)
        if not is_within_excluded_area(center_x, center_y, excluded_areas):
            return center_x, center_y
    return None

def move_mouse_to_enemy(enemy_position):
    x, y = enemy_position
    pyautogui.moveTo(x, y, duration=0.1)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([100, 150, 70])
upper_blue = np.array([140, 255, 255])

current_color = "red"

excluded_areas = [
    (3218, 33, 100, 100),
    (3806, 301, 100, 100),
    (0, 0, 100, 100),
    (521, 262, 100, 100)
]

while True:
    if keyboard.is_pressed("1"):
        current_color = "red"
        print("Red color selected")
        time.sleep(0.2)
    elif keyboard.is_pressed("2"):
        current_color = "blue"
        print("Blue color selected")
        time.sleep(0.2)
    screenshot = get_screenshot()
    if current_color == "red":
        enemy_position = find_enemy_by_color(screenshot, lower_red, upper_red, excluded_areas)
    elif current_color == "blue":
        enemy_position = find_enemy_by_color(screenshot, lower_blue, upper_blue, excluded_areas)
    if enemy_position:
        move_mouse_to_enemy(enemy_position)
    time.sleep(0.05)
