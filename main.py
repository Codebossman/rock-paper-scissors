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
food = Food()
foodPlotted = False
updateRequired = True  # Start with initial draw

# --- Input Events ---
def on_button_pressed_a():
    global xPos, updateRequired
    xPos = max(0, xPos - 1)
    updateRequired = True

def on_button_pressed_b():
    global xPos, updateRequired
    xPos = min(4, xPos + 1)
    updateRequired = True

def on_pin_pressed_p2():
    global yPos, updateRequired
    yPos = min(4, yPos + 1)
    updateRequired = True

def on_logo_pressed():
    global yPos, updateRequired
    yPos = max(0, yPos - 1)
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
    global foodPlotted, updateRequired

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

basic.forever(on_forever)
