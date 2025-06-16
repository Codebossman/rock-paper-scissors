let xPos = 0
let yPos = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    xPos += -1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    yPos += 1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    xPos += 1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    yPos += -1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
basic.forever(function on_forever() {
    
    if (xPos == 6) {
        xPos = 5
    }
    
    led.plot(xPos, yPos)
})
