import tkinter as tk
from tkinter import ttk
import time
import pyautogui
import keyboard

# Variables to keep track of the number of times the mouse has moved and countdown seconds
moves_count = 0
is_running = False

def move_mouse():
    # Move the mouse cursor 20 pixels to the right
    pyautogui.move(20, 0, duration=0.25)

def reset_mouse():
    # Get the center coordinates of the screen
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    # Move the mouse cursor to the center of the screen
    pyautogui.moveTo(center_x, center_y, duration=0.25)

def start_stop_mouse():
    global is_running
    if is_running:
        # Stop the mouse movement
        is_running = False
        start_stop_button.config(text="Start")
    else:
        # Start the mouse movement
        is_running = True
        start_stop_button.config(text="Stop")
        move_mouse_loop()

def move_mouse_loop():
    global moves_count
    if is_running:
        # Call the function to move the mouse
        move_mouse()
        # Increment the moves_count
        moves_count += 1
        # If the mouse has moved 4 times, reset its position
        if moves_count == 4:
            reset_mouse()
            moves_count = 0  # Reset moves_count back to 0
    # Schedule the move_mouse_loop function to run again after 30 seconds
    root.after(10000, move_mouse_loop)

def stop_mouse():
    global is_running
    is_running = False
    start_stop_button.config(text="Start")

def toggle_start_stop(event=None):
    if is_running:
        stop_mouse()
    else:
        start_stop_mouse()

# Create the main Tkinter window
root = tk.Tk()
root.title("AFK Mouse Mover")

# Configure style
style = ttk.Style()
style.configure('Primary.TButton', background='dark grey', foreground='white')
style.configure('Secondary.TButton', background='blue', foreground='white')

# Create a label for the title
title_label = ttk.Label(root, text="AFK Mouse Mover", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create a button to start and stop the mouse movement
start_stop_button = ttk.Button(root, text="Start", style='Primary.TButton', command=start_stop_mouse)
start_stop_button.pack(pady=5)

# Create a button to stop the mouse movement
stop_button = ttk.Button(root, text="Stop", style='Secondary.TButton', command=stop_mouse)
stop_button.pack(pady=5)

# Bind the toggle_start_stop function to Ctrl+Alt+X key combination
keyboard.add_hotkey("ctrl+alt+x", toggle_start_stop)

# Start the Tkinter event loop
root.mainloop()
