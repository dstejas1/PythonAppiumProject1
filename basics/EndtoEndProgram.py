import time
from concurrent.futures import thread

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
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

def ScrollDown(driver : WebDriver):
    window_size = driver.get_window_size()
    start_x = window_size["width"] / 2
    start_y = window_size["height"] * 2
    end_y = window_size["height"] * 0.2

    actions = ActionChains(driver)
    pointer = PointerInput(interaction.POINTER_TOUCH, 'finger')
    action_builder = ActionBuilder(driver, mouse=pointer)

    action_builder.pointer_action.move_to_location(x=start_x, y=start_y)
    action_builder.pointer_action.pointer_down()
    action_builder.pointer_action.move_to_location(x=start_x, y=end_y)
    action_builder.pointer_action.pointer_up()

    actions.w3c_actions = action_builder
    actions.perform()


options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
#Login
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Username').send_keys('standard_user')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Password').send_keys('secret_sauce')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Login').click()
#Add to cart
driver.find_element(By.XPATH,'(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Cart').click()
#checkout
time.sleep(2)
driver.find_element(By.XPATH,'//android.widget.TextView[@text="CHECKOUT"]').click()
#Fill the form
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-First Name').send_keys('user')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Last Name').send_keys('sauce')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Zip/Postal Code').send_keys('560065')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-CONTINUE').click()

#PlaceOrder
ScrollDown(driver)
driver.find_element(By.ACCESSIBILITY_ID,'test-FINISH').click()

time.sleep(5)
driver.quit()
