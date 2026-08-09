import time
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "TejasEmulator",
    "automationName": "UiAutomator2",
    "app": "/Users/tejasd/Downloads/callsandroid.apk"
}

appium_server = AppiumService()
appium_server.start()
print(appium_server.is_running)
print(appium_server.is_listening)

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Accept').click()
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Activate SynQ').click()
time.sleep(2)
driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
time.sleep(2)

# ---- FACE LIVENESS BYPASS (replaces the "Biometric and Liveliness Check" screen) ----
def bypass_face_liveness(image_path):
    url = "https://facelivenessbackend.trustgrid.com/api/check_liveness"

    with open(image_path, "rb") as img_file:
        files = {"file": (image_path.split("/")[-1], img_file, "image/jpeg")}
        response = requests.post(url, files=files)

    print(f"Liveness bypass status: {response.status_code}")
    print(response.text)
    return response.status_code == 200

# Path to a real face photo you'll supply manually
image_path = "/Users/tejasd/Desktop/NRI.jpeg"

bypass_success = bypass_face_liveness(image_path)

if not bypass_success:
    raise Exception("Liveness bypass failed — check API response above")

time.sleep(2)
# ---- END BYPASS ----

driver.find_element(By.XPATH, '//*[@text="Start your SynQ"]')
time.sleep(5)

driver.quit()
appium_server.stop()