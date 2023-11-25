import cv2
import keyboard
import pyautogui
import numpy as np

fps = 30
tamanho_da_tela = tuple(pyautogui.size())

codec = cv2.VideoWriter_fourcc(*"mp4h")
video = cv2.VideoWriter("capturePy.mp4", codec, fps, tamanho_da_tela)

while True:
    frame = pyautogui.screenshot()
    frame = np.array(frame)

    video.write(frame)

    if keyboard.is_pressed("esc"):
        break

video.release()
cv2.destroyAllWindows()