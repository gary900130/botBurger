import netifaces as ni
def getIP:
    ni.ifaddresses('lo')
    ip = ni.ifaddresses('lo')[ni.AF_INET][0]['addr']
    return ip
