dir = "C:\\Users\\seblf\\Documents\\Python\\Sigma\\"

notebooks = {
    "button": {
        "jpg":dir+"screen\\nb-button.jpg",
        "coords":(10,120,20,130)
    },
    "all": {
        "jpg":dir+"screen\\notebooks.jpg",
        "coords":(90,120,100,140)
    },
    "english": {
        "jpg":dir+"screen\\onenote\\english.jpg",
        "coords":(140,400,150,440)
    }
}

def onenote():
    pass
    #Wait
    #if checkPic(notebooks[button][coords],notebooks[button][path]):
        #Click

def checkPic(bbox, path):
    pass
    #sc = ImageGrab.grab(bbox)
    #return True if ImageChops.difference(sc,open(path)).getbbox() else False