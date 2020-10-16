import time
from PIL import ImageGrab, ImageChops, Image
from pynput.mouse import Controller, Button

dir = "C:/Users/seblf/Documents/Python/Sigma/"

notebooks = {
    "button": {
        "png":dir+"screen/nb-button.png",
        "coords":(10,120,20,130)
    },
    "all": {
        "png":dir+"screen/notebooks.png",
        "coords":(90,120,100,140)
    },
    "english": {
        "png":[dir+"screen/onenote/english.png", dir+"screen/onenote/english-new.png"],
        "coords":(140,400,150,440)
    }
}

mouse = Controller()
def onenote():
    time.sleep(5)
    if checkPic(notebooks["button"]["coords"],notebooks["button"]["png"]):
        mouse.position = (15,125)
        mouse.click(Button.left, 2)
def checkPic(bbox, path):
    sc = ImageGrab.grab(bbox)
    return False if ImageChops.difference(sc,Image.open(path)).getbbox() else True