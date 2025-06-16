xPos = 0
yPos = 0

def on_button_pressed_a():
    global xPos
    xPos += -1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
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
    global xPos
    xPos += 1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global yPos
    yPos += -1
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    global xPos
    if xPos == 6:
        xPos = 5
    led.plot(xPos, yPos)
basic.forever(on_forever)
