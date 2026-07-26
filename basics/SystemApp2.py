import time
from concurrent.futures import thread

from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "TejasEmulator",
    "automationName": "UiAutomator2",
    "appPackage": "com.vivo.calculator",
    "appActivity": ".Calculator"
}
options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
driver.press_keycode(8)
driver.press_keycode(9)
time.sleep(5)
driver.quit()
