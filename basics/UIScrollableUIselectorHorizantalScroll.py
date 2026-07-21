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
    "app": "/Users/tejasd/Downloads/ApiDemos-debug.apk",
    "appActivity": "io.appium.android.apis.ApiDemos"
}

options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Views').click()
time.sleep(2)

ui_scrollable = (
    'new UiScrollable(new UiSelector().scrollable(true))'
    '.scrollIntoView(new UiSelector().text("Tabs"))'
)

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    ui_scrollable
)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Tabs').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'5. Scrollable').click()
time.sleep(2)

ui_scrollable1 = (
    'new UiScrollable(new UiSelector().scrollable(true))'
    '.setAsHorizontalList()'
    '.scrollIntoView(new UiSelector().text("TAB 14"))'
)

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,ui_scrollable1)
time.sleep(5)
driver.quit()
