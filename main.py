from microbit import *

class Food:
    def __init__(self):
        self.x = None
        self.y = None

    def createFood(self):
        self.x = randint(0, 4)
        self.y = randint(0, 4)

    def drawFood(self):
        if self.x is not None and self.y is not None:
            led.plot(self.x, self.y)

# --- Game State ---
xPos = 0
yPos = 0
movingHorizontal = False
movingVertical = True
food = Food()
foodPlotted = False
updateRequired = True  # Start with initial draw

# --- Input Events ---
def on_button_pressed_a():
    global xPos, updateRequired, movingHorizontal
    
    updateRequired = True
    movingHorizontal = False

def on_button_pressed_b():
    global xPos, updateRequired, movingHorizontal
    
    updateRequired = True
    movingHorizontal = True

def on_pin_pressed_p2():
    global yPos, updateRequired, movingVertical
    
    updateRequired = True
    movingVertical = False

def on_logo_pressed():
    global yPos, updateRequired, movingVertical
    
    updateRequired = True

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# --- Draw Only on Update ---
def draw():
    basic.clear_screen()
    food.drawFood()
    led.plot(xPos, yPos)

# --- Game Loop ---
def on_forever():
    global xPos, yPos,foodPlotted, updateRequired, movingVertical, movingHorizontal

    if not foodPlotted:
        food.createFood()
        foodPlotted = True
        updateRequired = True

    if xPos == food.x and yPos == food.y:
        foodPlotted = False
        updateRequired = True

    if updateRequired:
        draw()
        updateRequired = False

    if movingHorizontal:
        xPos = min(4, xPos + 1)
        basic.pause(100)
    else:
        xPos = min(4, xPos - 1)
        basic.pause(100)
    if movingVertical:
        yPos = min(4, xPos + 1)
        basic.pause(100)
    else:
        xPos = min(4, xPos - 1)
        basic.pause(100)        
basic.forever(on_forever)
