from tkinter import *
from PIL import ImageTk, Image
#http://www.krivers.net/15112-f18/notes/notes-animations-part2.html
####################################
# customize these functions
####################################
#Idea:

def init(data):
# data comes preset with width and height, from the run function
    data.circleSize = min(data.width,data.height) / 10
    data.circleX = data.width/2
    data.circleY = data.height/2
    data.charText = ""
    data.keysymText = ""
    data.Toggle = ImageTk.PhotoImage(Image.open("Toggle.png"))
    data.On = ImageTk.PhotoImage(Image.open("NewOn.png"))

    data.Off = ImageTk.PhotoImage(Image.open("NewOff.png"))
    data.isClass = False
    data.togX = 27
    data.togY = 25
    data.needChange = False
def mousePressed(event, data):

    data.circleX = event.x
    data.circleY = event.y

    #is the mouse hovering over the button?
    if (not(data.needChange)):
        if(event.x >= 27 and event.x <= 86 and event.y >= 25 and event.y <=61):
            if (data.isClass):
                data.isClass = False
                data.needChange = True
            else:
                data.isClass = True

                data.needChange = True
def keyPressed(event, data):
    data.charText = event.char
    data.keysymText = event.keysym
def timerFired(data):
    pass

def redrawAll(canvas, data):

    '''
    if(data.circleX >= 27 and data.circleX <= 409 and data.circleY >= 27 and data.circleY <=109):
        data.On = Image.resize(168 + data.rsa, 36 + data.rsa)
    '''
    if (data.isClass):
        canvas.create_image(27, 25, anchor=NW, image=data.On)
    else:
        canvas.create_image(27, 25, anchor=NW, image=data.Off)

    if (data.needChange):
        if (data.togX == 47):
            data.togX = 50
            data.needChange = False
        if (data.togX == 42):
            data.togX = 47
        if (data.togX == 27):
            data.togX = 42

        if (data.needChange):
            if (data.togX == 30):
                data.togX = 27
                data.needChange = False
            if (data.togX == 35):
                data.togX = 30
            if (data.togX == 50):
                data.togX = 35
        '''
    if (data.needChange):
        if (data.togX == 41):
            data.togX = 50
            data.needChange = False
        if (data.togX == 27):
            data.togX = 41

        if (data.needChange):
            if (data.togX == 36):
                data.togX = 27
                data.needChange = False
            if (data.togX == 50):
                data.togX = 36
        '''
    canvas.create_image(data.togX, data.togY, anchor=NW, image=data.Toggle)

    """
    if data.charText != "":
        canvas.create_text(data.width/10, data.height/3,
                           text="char: " + data.charText)
    if data.keysymText != "":
        canvas.create_text(data.width/10, data.height*2/3,
                           text="keysym: " + data.keysymText)
    """
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(683, 384)
