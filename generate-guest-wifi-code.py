import segno

wifi_code = helpers.make_wifi(ssid='Partridge Guest', password='WiFiPassword22', security='WPA')
wifi_code.designator
'3-M'
wifi_code.save('partridge-guest-wifi.png', scale=10)
