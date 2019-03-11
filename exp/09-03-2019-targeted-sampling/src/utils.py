import sys

def parseBoolean(s):
    if s in ["true", "True", "TRUE", "on", "On", "ON", "1"]:
        return True
    elif s in ["false", "False", "FALSE", "off", "Off", "OFF", "0"]:
        return False
    else:
        sys.exit("Error while reading the expected boolean parameter "+s)
