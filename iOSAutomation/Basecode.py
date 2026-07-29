import datetime
import time

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

tomorrow= datetime.datetime.now() + datetime.timedelta(days=1)
print(tomorrow.date())
print(tomorrow.strftime("%A" + "%d" + "%B"))
