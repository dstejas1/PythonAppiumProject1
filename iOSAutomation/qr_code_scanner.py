import base64

from basics.UIScrollableUIselectorHorizantalScroll import driver


class QrCodeScanner:
    def __init__(self):
        self.qrcode = driver

    def take_screenshot(self):
        Screenshot_Base64 = self.qrcode.get_screenshot_as_base64()
        imgae_bytes = base64.b64encode(Screenshot_Base64)
        
