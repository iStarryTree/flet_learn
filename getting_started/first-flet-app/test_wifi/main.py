from pywifi import const, PyWiFi

def test_interface():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    if iface.status() in [const.IFACE_CONNECTED, const.IFACE_CONNECTING]:
        # return iface
        print(f"Connected to {iface.name()}.")
    else:
        print(f"Not connected to {iface.name()}.")
        # return None

if __name__=="__main__":
    test_interface()