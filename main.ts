input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    hasCleared = true
    xPos += -1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    hasCleared = true
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
    
    hasCleared = true
    xPos += 1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    hasCleared = true
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    hasCleared = true
    yPos += -1
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    hasCleared = true
})
let yPos = 0
let xPos = 0
let hasCleared = false
basic.forever(function on_forever() {
    
    buildBorder()
    if (xPos && yPos) {
        
    }
    
    led.plot(xPos, yPos)
})
function buildBorder() {
    let xPos: number;
    let yPos: number;
    if (xPos > 4) {
        xPos = 4
    }
    
    if (xPos < 0) {
        xPos = 0
    }
    
    if (yPos > 4) {
        yPos = 4
    }
    
    if (yPos < 0) {
        yPos = 0
    }
    
}

class Food {
    public static instanceFood() {
        let x = randint(0, 4)
        let y = randint(0, 4)
        if (hasCleared == true) {
            led.plot(x, y)
        }
        
    }
    
}

