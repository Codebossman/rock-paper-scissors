class Food {
    x: number
    y: number
    constructor() {
        this.x = null
        this.y = null
    }
    
    public createFood() {
        this.x = randint(0, 4)
        this.y = randint(0, 4)
    }
    
    public drawFood() {
        if (this.x !== null && this.y !== null) {
            led.plot(this.x, this.y)
        }
        
    }
    
}

//  --- Game State ---
let xPos = 0
let yPos = 0
let movingHorizontal = false
let movingVertical = true
let food = new Food()
let foodPlotted = false
let updateRequired = true
//  Start with initial draw
//  --- Input Events ---
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    updateRequired = true
    movingHorizontal = false
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    updateRequired = true
    movingHorizontal = true
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    updateRequired = true
    movingVertical = false
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    updateRequired = true
})
//  --- Draw Only on Update ---
function draw() {
    basic.clearScreen()
    food.drawFood()
    led.plot(xPos, yPos)
}

//  --- Game Loop ---
basic.forever(function on_forever() {
    
    if (!foodPlotted) {
        food.createFood()
        foodPlotted = true
        updateRequired = true
    }
    
    if (xPos == food.x && yPos == food.y) {
        foodPlotted = false
        updateRequired = true
    }
    
    if (updateRequired) {
        draw()
        updateRequired = false
    }
    
    if (movingHorizontal) {
        xPos = Math.min(4, xPos + 1)
        basic.pause(100)
    } else {
        xPos = Math.min(4, xPos - 1)
        basic.pause(100)
    }
    
    if (movingVertical) {
        yPos = Math.min(4, xPos + 1)
        basic.pause(100)
    } else {
        xPos = Math.min(4, xPos - 1)
        basic.pause(100)
    }
    
})
