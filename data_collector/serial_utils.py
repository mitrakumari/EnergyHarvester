import serial, os, glob

def findPort():
    comPort = None
    if comPort is None and os.environ.get("GOODFET")!=None:
        glob_list = glob.glob(os.environ.get("GOODFET"))
        if len(glob_list) > 0:
            comPort = glob_list[0]
    if comPort is None:
        glob_list = glob.glob("/dev/tty.usbserial*")
        if len(glob_list) > 0:
            comPort = glob_list[0]
    if comPort is None:
        glob_list = glob.glob("/dev/ttyUSB*")
        if len(glob_list) > 0:
            comPort = glob_list[0]
    return comPort