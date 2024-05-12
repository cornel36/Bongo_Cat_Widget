import os
import tkinter as tk
from PIL import Image, ImageTk
import keyboard

# Variables to track mouse movement
mouse_x, mouse_y = 0, 0

def on_drag(event):
    global mouse_x, mouse_y
    x, y = event.x_root, event.y_root
    root.geometry(f"+{root.winfo_x() + x - mouse_x}+{root.winfo_y() + y - mouse_y}")
    mouse_x, mouse_y = x, y

def on_drag_start(event):
    global mouse_x, mouse_y
    mouse_x, mouse_y = event.x_root, event.y_root

def on_drag_stop(event):
    pass

root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", '#fc0000')  
root.config(bg='#fc0000')  # background color
root.geometry("100x63")  # window size

# load images from main dir
image_files = sorted([f for f in os.listdir() if f.endswith(".gif")])
num_states = len(image_files)
images = [ImageTk.PhotoImage(Image.open(f)) for f in image_files]

label = tk.Label(root, image=images[0])
label.config(bg='#fc0000')  # Set background color to black for transparency effect
label.pack()

display_state = 0  

def on_press(event):
    global display_state
    display_state = (display_state + 1) % num_states  # change state by 1

    # update image
    label.configure(image=images[display_state])
    label.pack()
    root.update()

# listen for keys
keyboard.on_press(on_press)

# mouse for dragging window
root.bind("<B1-Motion>", on_drag)
root.bind("<ButtonPress-1>", on_drag_start)
root.bind("<ButtonRelease-1>", on_drag_stop)

root.mainloop()
