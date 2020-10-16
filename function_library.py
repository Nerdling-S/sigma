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
    "subjects": {
        "english": {
            "names":("english","eng","e"),
            "png":[dir+"screen/onenote/english.png", dir+"screen/onenote/english-new.png"],
            "coords":(140,400,150,440)
        }
    }
}

mouse = Controller()
def onenote(nb=""):
    time.sleep(5)
    mouse.click(Button.left)
    # open notebooks dialogue
    if checkPics(notebooks["button"]["coords"],[notebooks["button"]["png"]]):
        mouse.position = notebooks["button"]["coords"][:2] + (5,5)
        mouse.click(Button.left)
        time.sleep(.5)
    #open all notebooks
    if not checkPics(notebooks["all"]["coords"],[notebooks["all"]["png"]]):
        mouse.position = notebooks["all"]["coords"][:2] + (5,5)
        mouse.click(Button.left)
        time.sleep(.5)
    if not nb:
        return
    for subj in notebooks["subjects"]:
        if nb in notebooks["subjects"][subj]["names"] and checkPics(notebooks["subjects"][subj]["coords"],notebooks["subjects"][subj]["png"]):
            mouse.position = notebooks["subjects"][subj]["coords"][:2]
            mouse.click(Button.left)
            break
def checkPics(bbox, paths):
    sc = ImageGrab.grab(bbox)
    for path in paths:
        if not ImageChops.difference(sc,Image.open(path)).getbbox():
            return True
    return False