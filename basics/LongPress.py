import time
from concurrent.futures import thread

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import pointer_input, interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "TejasEmulator",
    "automationName": "UiAutomator2",
    "app": "/Users/tejasd/Downloads/ApiDemos-debug.apk"
}

options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

time.sleep(2)
driver.find_element(By.XPATH,'//*[@text="Views"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@text="Expandable Lists"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@text="1. Custom Adapter"]').click()
time.sleep(2)

actions = ActionChains(driver)
pointer = PointerInput(interaction.POINTER_TOUCH, 'touch')
action_builder= ActionBuilder(driver, mouse=pointer)

longPress= driver.find_element(By.XPATH,'//*[@text="People Names"]')
action_builder.pointer_action.move_to(longPress).pause(3).pointer_down().pause(3).pointer_up()

actions.w3c_actions= action_builder
actions.perform()

time.sleep(6)
driver.quit()
