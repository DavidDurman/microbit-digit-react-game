def on_button_pressed_a():
    global Attempts, Paused
    Attempts = 0
    Paused = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Attempts, Paused
    Attempts = Attempts + 1
    if Number2 == 4:
        Paused = 1
        basic.show_string("" + str((Attempts)))
        music.play_melody("C5 G B A F A C5 B ", 120)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

Number2 = 0
Attempts = 0
Paused = 0
Paused = 1

def on_forever():
    global Number2
    if Paused == 0:
        Number2 = randint(0, 9)
        basic.show_string("" + str((Number2)))
        basic.pause(100)
basic.forever(on_forever)
