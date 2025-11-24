"""
--------------------------------------------------------------------------------------------------------------------
File: Fireflies_Marcus.py
By: Ella Marcus
Date: 11/17/2025
Description: Fireflies fly in a circle at different speeds and angles
--------------------------------------------------------------------------------------------------------------------

Pseudocode for Fireflies:
import simplegui, math, and random
set Width and Height to 600, 400
set CX and CY to W/2 and H/2 for canvas center
set R to list [30, 40, 60, 80, 100, 140, 150, 160, 180]
set ball_size to list [4, 7, 10, 8, 15, 3, 6, 2, 11]
set isRunning to False
set isFlickering to False
set playSound to False
set fast_count to 0
set slow_count to 0
set speed to list[
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05)
]
set angle to list [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
set colors to list [
    "Aquamarine", "Crimson", "LightPink", "LightSkyBlue", "YellowGreen", "Moccasin", 
    "MediumPurple", "GoldenRod", "LightSteelBlue"
]
set ball_color to list [
    random.choice(colors),random.choice(colors),random.choice(colors),
    random.choice(colors),random.choice(colors),random.choice(colors),
    random.choice(colors),random.choice(colors),random.choice(colors),
]
set flicker to dictionary {
    "Aquamarine": "MediumTurquoise",
    "MediumTurquoise":"Aquamarine",
    "Crimson":"LightCoral",
    "LightCoral":"Crimson",
    "LightPink":"HotPink",
    "HotPink":"LightPink",
    "LightSkyBlue":"DeepSkyBlue",
    "DeepSkyBlue":"LightSkyBlue",
    "YellowGreen":"Chartreuse",
    "Chartreuse":"YellowGreen",
    "Moccasin":"Orange",
    "Orange":"Moccasin",
    "MediumPurple":"Plum",
    "Plum":"MediumPurple",
    "GoldenRod":"Khaki",
    "Khaki":"GoldenRod",
    "LightSteelBlue":"CornflowerBlue",
    "CornflowerBlue":"LightSteelBlue"
}

Define draw(c):
    c.draw_text("Fireflies Start/Stop Faster Slower", (10, 24), 16, "White")
    c.draw_text(f"Count:11, Speed: x {(fast_count - slow_count) * 1.25}", (10, 45), 16, "White")
    for i, a in enumerate(angle):
        x = CX + R[i] * math.cos(a)
        y = CY + R[i] * math.sin(a)
        c.draw_circle((x, y), ball_size[i], 4, ball_color[i], ball_color[i]) 
    
    
Define tick(0):
    if isRunning:
        global speed
        for i, a in enumerate(angle):
            add speed[i] to angle[i]
    if isFlickering:
        for i, a in enumerate(angle):
            ball_color[i] = flicker[ball_color[i]]
            
            
Define start_stop():
    global speed
    global isRunning
    
    if isRunning == True:
        isRunning = False
        timer_label.set_text("Timer: OFF")
    else:
        isRunning = True
        timer_label.set_text("Timer: ON")
        
        
Define faster():
    global fast_count
    global speed
    for i, a in enumerate(angle):
        speed[i] multiplied by 1.25
    fast_count add 1
    return fast_count
    
    
Define slower():
    global slow_count
    global speed
    for i, a in enumerate(angle):
        speed[i] divided by 1.25
    slow_count add 1
    return slow_count
    
    
Define flickerStart():
    global isFlickering
    if isFlickering == True:
        isFlickering = False
        flicker_label.set_text("Flicker: OFF")
    else:
        isFlickering = True
        flicker_label.set_text("Flicker: ON")
        
        
Define soundButton():
    global playSound
    if playSound == True:
        sound.pause()
        playSound = False
        sound_label.set_text("Sound: OFF")
    else:
        sound.play()
        playSound = True
        sound_label.set_text("Sound: ON")
        
        
frame = simplegui.create_frame("Fireflies", W, H)
frame.set_draw_handler(draw)
frame.set_canvas_background("#203040")
frame.add_button("Start/ Stop", start_stop)
timer_label = frame.add_label("Timer: OFF")
frame.add_button("Faster x 1.25", faster)
frame.add_button("Slower / 1.25", slower)
frame.add_button("Flicker: ON/OFF", flickerStart)
flicker_label = frame.add_label("Flicker: OFF")
frame.add_button("Sound: ON/OFF", soundButton)
sound_label = frame.add_label("Sound: OFF")
t0 = simplegui.create_timer(20, tick0) 
t0.start()

sound = simplegui.load_sound("https://raw.githubusercontent.com/emarcus9/module7_Ella_Marcus/main/fireflies-in-the-night-forest.mp3")


frame.start()

"""

import simplegui, math, random

# -------------------------
# Canvas / geometry constants
# -------------------------
W, H = 600, 400  # canvas width/height
CX, CY = W / 2, H / 2  # canvas center
R = [30, 40, 60, 80, 100, 140, 150, 160, 180]  # radii for the nine orbits (inner -> outer)

ball_size = [4, 7, 10, 8, 15, 3, 6, 2, 11]  # list of possible ball sizes
isRunning = False  # use this for toggle to turn on and off orbit
isFlickering = False  # use this for toggle to turn on and off flicker
playSound = False  # use this for toggle to turn on and off sound
fast_count = 0  # Keep track of how many times faster is clicked
slow_count = 0  # Keep track of how many times slower is clicked
speed = [  # list of different speeds for balls selected at random as extra credit
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05),random.uniform(0.01, 0.05),
    random.uniform(0.01, 0.05)
]
# -------------------------
# Mutable game state
# -------------------------
# Angles (in radians) for each orbiting dot. Timer will *update* these values.
angle = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
colors = [  # Optional colors for balls
    "Aquamarine", "Crimson", "LightPink", "LightSkyBlue", "YellowGreen", "Moccasin", 
    "MediumPurple", "GoldenRod", "LightSteelBlue"
]
ball_color = [  # List of colors picked at random for balls
    random.choice(colors),random.choice(colors),random.choice(colors),
    random.choice(colors),random.choice(colors),random.choice(colors),
    random.choice(colors),random.choice(colors),random.choice(colors),
]
flicker = {  # Colors for balls to flicker between
    "Aquamarine": "MediumTurquoise",
    "MediumTurquoise":"Aquamarine",
    "Crimson":"LightCoral",
    "LightCoral":"Crimson",
    "LightPink":"HotPink",
    "HotPink":"LightPink",
    "LightSkyBlue":"DeepSkyBlue",
    "DeepSkyBlue":"LightSkyBlue",
    "YellowGreen":"Chartreuse",
    "Chartreuse":"YellowGreen",
    "Moccasin":"Orange",
    "Orange":"Moccasin",
    "MediumPurple":"Plum",
    "Plum":"MediumPurple",
    "GoldenRod":"Khaki",
    "Khaki":"GoldenRod",
    "LightSteelBlue":"CornflowerBlue",
    "CornflowerBlue":"LightSteelBlue"
}

# -------------------------
# Draw handler
# -------------------------
def draw(c):
    """
    The frame calls draw(c) to draw orbiting balls ~60 times per second.
    
    c.draw_text to write title on the canvas, and the fireflies count and speed.
    Use for loop to draw each circle according to its orbit from the center.
    Draw each circle with random ball size and random color
    """
    # Title text
    c.draw_text("Fireflies Start/Stop Faster Slower", (10, 24), 16, "White")  # Title on canvas
    c.draw_text(f"Count:9, Speed: x {(fast_count - slow_count) * 1.25}", (10, 45), 16, "White")  # Title on canvas
    # For each angle, compute the (x, y) along its circular path and draw it.
    for i, a in enumerate(angle):
        # Convert polar (radius R[i], angle a) to Cartesian (x, y)
        x = CX + R[i] * math.cos(a)
        y = CY + R[i] * math.sin(a)
        

        # The orbiter itself: a small circle. We draw the same outline color and filled interior color, with random ball size.
        c.draw_circle((x, y), ball_size[i], 4, ball_color[i], ball_color[i]) 


def tick0():
    """
    Called by a timer at a fixed interval to draw the circles and flicker the colors.
    
    If isRunning is true globalize speed and use a for loop to add speed to angle to make the ball rotate.
    if IsFlickering is true use a for loop to switch between flcker color and ball color.
    """
    if isRunning:
        global speed
        for i, a in enumerate(angle):  # add speed to angle to make it appear as though it's going in a circle
            angle[i] += speed[i]
    if isFlickering:
        for i, a in enumerate(angle):
            ball_color[i] = flicker[ball_color[i]]  # Switch off between two colors to appear as though it's flickering
       

    
def start_stop():
    """
    Called by a button used as a toggle to turn on and off orbit.
    
    Globalize speed and isRunning for usage.
    If isRunning is true, make it false for the toggle and set label to off.
    If isRunning is false, make it true for the toggle and set label to on.
    """
    global speed
    global isRunning
    
    if isRunning == True:
        isRunning = False  # Set to false so it will work as a toggle
        timer_label.set_text("Timer: OFF")
    else:
        isRunning = True  # Set to true so it will work as a toggle
        timer_label.set_text("Timer: ON")
        
        
def faster():
    """
    Called by a button to make orbit of balls faster.
    
    Globalize fast_count and speed for usage.
    Use for loop to multiply speed by 1.25
    Add 1 to fast_count and return it for usage.
    """
    global fast_count
    global speed
    for i, a in enumerate(angle):  # multiply speed to make it go faster
        speed[i] *= 1.25
    fast_count += 1  # Use fast_count to keep track of number of clicks
    return fast_count
        
    
def slower():
    """
    Called by a button to make orbit of balls slower.
    
    Globalize slow_count and speed for usage.
    Use for loop to divide speed by 1.25
    Add 1 to slow_count and return it for usage.
    """
    global slow_count
    global speed
    for i, a in enumerate(angle):  # divide speed to make it go slower
        speed[i] /= 1.25
    slow_count += 1  # Use slow_count to keep track of number of clicks
    return slow_count


# Extra credit flicker
def flickerStart():
    """
    Called by a button used as a toggle to turn on and off flicker.
    
    Globalize isFlickering for usage.
    If isFlickering is true, make it false for the toggle and set label to off.
    If isFlickering is false, make it true for the toggle and set label to on.
    """
    global isFlickering
    if isFlickering == True:
        isFlickering = False  # Set to false so it will work as a toggle
        flicker_label.set_text("Flicker: OFF")
    else:
        isFlickering = True  # Set to true so it will work as a toggle
        flicker_label.set_text("Flicker: ON")
        

# Extra credit sound button, works on chrome
def soundButton():
    """
    Called by a button used as a toggle to turn on and off sound.
    
    Globalize playSound for usage.
    If playSound is true, make it false for the toggle, pause sound, and set label to off.
    If playSound is false, make it true for the toggle, play sound, and set label to on.
    """
    global playSound
    if playSound == True:
        sound.pause()  # Stop playing sound
        playSound = False  # Set to false so it will work as a toggle
        sound_label.set_text("Sound: OFF")
    else:
        sound.play()  # Start playing sound
        playSound = True  # Set to true so it will work as a toggle
        sound_label.set_text("Sound: ON")
    
    

# -------------------------
# Frame / timer, sound, and button setup.
# -------------------------
frame = simplegui.create_frame("Fireflies", W, H)

# The draw handler is the renderer—no state changes beyond drawing.
frame.set_draw_handler(draw)

# A dark background so colors pop.
frame.set_canvas_background("#203040")

# Add button to start and stop orbit.
frame.add_button("Start/ Stop", start_stop)
# Add label for timer
timer_label = frame.add_label("Timer: OFF")
# Add faster and slower button.
frame.add_button("Faster x 1.25", faster)
frame.add_button("Slower / 1.25", slower)

# Add button to start and stop flicker.
frame.add_button("Flicker: ON/OFF", flickerStart)
flicker_label = frame.add_label("Flicker: OFF")

# Add button to start and stop sound.
frame.add_button("Sound: ON/OFF", soundButton)
sound_label = frame.add_label("Sound: OFF")

# Create a timer.
t0 = simplegui.create_timer(20, tick0) 
t0.start()

# Load sound to play.
sound = simplegui.load_sound("https://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg")

# Start the frame loop (this begins the ~60 FPS draw cycle).
frame.start()
