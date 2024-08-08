import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

mid = 683, 384
screen = 1315, 487
windowToScreen = 983, 24


driver.get('https://www.youtube.com/shorts/')
sleep(4)
pyautogui.moveTo(windowToScreen, duration=2)
pyautogui.click()
pyautogui.moveTo(mid , duration=1)
pyautogui.click()
def get_margin_left_percentage():
    try:
        element = driver.find_element(By.CLASS_NAME, 'PlayerControlsProgressBarHostProgressBarPlayheadWrapper')
        style = element.get_attribute('style')
        margin_left_value = style.split('margin-left: ')[1].split('%')[0]
        return float(margin_left_value)
    except Exception as e:
        print(f"Hata: {e}")
        return 0
    

while True:
    percentage = get_margin_left_percentage()
    if percentage >= 90:
        print(pyautogui.position())
        pyautogui.moveTo(screen, duration=2)
        pyautogui.click()
        pyautogui.moveTo(1366 / 2, 768 / 2)
        sleep(0.3)
    else:
        print(f"Yüzde: {percentage}")
        sleep(0.4)
