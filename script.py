import pyautogui
import time
import os
import functools
def click_accept_button():
    accept_button_location = None
    accept_images = os.listdir("./images")
    print(accept_images)
    print("Finding button...")
    while accept_button_location is None:
        for image in accept_images:
            accept_button_location = pyautogui.locateOnScreen(f"./images/{image}", confidence=0.7)
        time.sleep(1)
    print("Button found")
    accept_button_center = pyautogui.center(accept_button_location)
    pyautogui.click(accept_button_center)
    print("Match accepted! Exiting...")
    time.sleep(2)

click_accept_button()