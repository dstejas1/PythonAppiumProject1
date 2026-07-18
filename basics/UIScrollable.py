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
    "app": "/Users/tejasd/Documents/Android/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
    "appActivity": "com.swaglabsmobileapp.MainActivity"
}

options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
window_size = driver.get_window_size()
start_x = window_size["width"]/2
start_y = window_size["height"] *2
end_y = window_size["height"] * 0.2

actions = ActionChains(driver)
pointer = PointerInput(interaction.POINTER_TOUCH, 'finger')
action_builder= ActionBuilder(driver, mouse=pointer)

action_builder.pointer_action.move_to_location(x=start_x, y=start_y)
action_builder.pointer_action.pointer_down()
action_builder.pointer_action.move_to_location(x=start_x, y=end_y)
action_builder.pointer_action.pointer_up()

actions.w3c_actions= action_builder
actions.perform()



time.sleep(5)
driver.quit()
