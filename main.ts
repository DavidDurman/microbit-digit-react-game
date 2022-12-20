input.onButtonPressed(Button.A, function () {
    Attempts = 0
    Paused = 0
})
input.onButtonPressed(Button.B, function () {
    Attempts = Attempts + 1
    if (Number2 == 4) {
        Paused = 1
        basic.showString("" + Attempts)
        music.playMelody("C5 G B A F A C5 B ", 120)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
let Number2 = 0
let Attempts = 0
let Paused = 0
Paused = 1
basic.forever(function () {
    if (Paused == 0) {
        Number2 = randint(0, 9)
        basic.showString("" + Number2)
        basic.pause(100)
    }
})
