import time
import pyautogui as pag
import keyboard

# Variables
path_to_ss = "C:/Users/Mladen/Documents/Python/Screenshot app/img/"


def screenshotter(w, h):
    print()
    print('Starting program...\nPress "q" for screenshot or "k" to exit program.')
    print()
    num = -1
    while True:
        if keyboard.is_pressed("q"):
            num += 1
            x, y = pag.position()
            pag.screenshot(path_to_ss + "img_" + str(num) + ".png", (x, y, w, h))
            print(f"Click! Screenshot saved to defined path!")
        elif keyboard.is_pressed("k"):
            print("Exiting program...")
            break
        else:
            time.sleep(0.01)


if __name__ == "__main__":
    w = int(input("Enter width[px]: "))
    h = int(input("Enter height[px]: "))
    screenshotter(w, h)
