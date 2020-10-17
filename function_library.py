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
        "business": {
            "names":("business","bus","b"),
            "png":[dir+"screen/onenote/business.png"],
            "coords":(140,440,150,460)
        },
        "english": {
            "names":("english","eng","e"),
            "png":[dir+"screen/onenote/english.png"],
            "coords":(140,410,150,430)
        },
        "french": {
            "names":("french","fr","f"),
            "png":[dir+"screen/onenote/french.png",dir+"screen/onenote/french-new.png"],
            "coords":(140,370,150,390)
        },
        "maths": {
            "names":("maths", "math","m"),
            "png":[dir+"screen/onenote/maths.png",dir+"screen/onenote/maths-new.png"],
            "coords":(140,340,150,360)
        },
        "accounting": {
            "names":("accounting","acc","a"),
            "png":[dir+"screen/onenote/accounting.png"],
            "coords":(140,310,150,330)
        },
        "science": {
            "names":("science","sci","s"),
            "png":[dir+"screen/onenote/science.png",dir+"screen/onenote/science-new.png"],
            "coords":(140,260,150,280)
        },
        "school": {
            "names":("school","sch"),
            "png":[dir+"screen/onenote/school.png"],
            "coords":(90,230,100,250)
        },
        "conlang": {
            "names":("conlang","con"),
            "png":[dir+"screen/onenote/conlang.png"],
            "coords":(90,200,100,220)
        },
        "personal": {
            "names":("personal","per","p"),
            "png":[dir+"screen/onenote/personal.png"],
            "coords":(100,160,110,170)
        }
    }
}

mouse = Controller()
def onenote(nb=""):
    time.sleep(5)
    mouse.click(Button.left,2)
    # open notebooks dialogue
    if checkPics(notebooks["button"]["coords"],[notebooks["button"]["png"]]):
        mouse.position = notebooks["button"]["coords"][:2]
        mouse.click(Button.left)
        time.sleep(.5)
    #open all notebooks
    if not checkPics(notebooks["all"]["coords"],[notebooks["all"]["png"]]):
        mouse.position = notebooks["all"]["coords"][:2]
        mouse.click(Button.left)
        time.sleep(.5)
    if not nb:
        return
    for subj in notebooks["subjects"]:
        if nb in notebooks["subjects"][subj]["names"] and checkPics(notebooks["subjects"][subj]["coords"],notebooks["subjects"][subj]["png"]):
            mouse.position = notebooks["button"]["coords"][:2]
            mouse.click(Button.left)
            time.sleep(.5)
            break

def checkPics(bbox, paths):
    sc = ImageGrab.grab(bbox)
    for path in paths:
        if not ImageChops.difference(sc,Image.open(path)).getbbox():
            return True
    return False