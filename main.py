def on_button_pressed_a():
    global xPos, hasCleared
    hasCleared = True
    xPos += -1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    hasCleared = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    global yPos
    yPos += 1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    global xPos, hasCleared
    hasCleared = True
    xPos += 1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    hasCleared = True
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global yPos, hasCleared
    hasCleared = True
    yPos += -1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    hasCleared = True
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

yPos = 0
xPos = 0
hasCleared = False

def on_forever():
    global xPos, yPos
    if xPos and yPos == 0 and True:
        pass
    if xPos > 4:
        xPos = 4
    if xPos < 0:
        xPos = 0
    if yPos > 4:
        yPos = 4
    if yPos < 0:
        yPos = 0
    led.plot(xPos, yPos)
basic.forever(on_forever)
