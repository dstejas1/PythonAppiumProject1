import time

import appium
import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService


def setup_function():
    global appium_server
    appium_server = AppiumService()
    appium_server.start()
    desired_caps = {
        "platformName": "iOS",
        "platformVersion": "26.5",
        "deviceName": "iPhone 16 Pro",
        "udid": "B57D299A-6602-4DC6-8C41-473AF8B46923",
        "automationName": "XCUITest",
        "app": "/Users/tejasd/Library/Developer/Xcode/DerivedData/UIKitCatalog-cykpnfbggdpjqcgegnfvdehfvyys/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
    }

    global driver

    options = XCUITestOptions().load_capabilities(desired_caps)

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    time.sleep(3)


def teardown_function():
    driver.quit()
    appium_server.stop()


def test_applaunch():
    print("app is launched")

