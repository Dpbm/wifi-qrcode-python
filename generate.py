import qrcode
import getpass

ssid     = input("[SSID] : ")
password = getpass.getpass("[PASSWORD] : ") 

auth_type = "WPA"
hidden = False

wifi_qrcode_string = f"WIFI:T:{auth_type};S:{ssid};P:{password};H:{hidden};;"

image = qrcode.make(wifi_qrcode_string)
image.save(f'qr-code-wifi-{ssid}.png')
