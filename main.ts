class Food {
    public createFood() {
        let x = randint(0, 4)
        let y = randint(0, 4)
        led.plot(x, y)
    }
    
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    xPos += -1
    clearScreen()
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    yPos += 1
    clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    xPos += 1
    clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    yPos += -1
    clearScreen()
})
let yPos = 0
let xPos = 0
let hasCleared = false
let food = new Food()
let foodPlotted = false
basic.forever(function on_forever() {
    
    buildBorder()
    if (xPos && yPos) {
        
    }
    
    led.plot(xPos, yPos)
    if (foodPlotted == false) {
        food.createFood()
        foodPlotted = true
    }
    
})
function buildBorder() {
    
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

function clearScreen() {
    
    basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    hasCleared = true
}

