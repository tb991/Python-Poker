# produced by chatgpt from a short conversation (and then adapted)
# on ubuntu it requires sudo apt-get install python3-tk

import tkinter as tk
import threading
import time

# Create a Tkinter window
window = tk.Tk()

# Load the background image
background = tk.PhotoImage(file="/home/tom/Desktop/poker/images/gif/background.gif")

# Load the smaller image
first_image = tk.PhotoImage(file="/home/tom/Desktop/poker/images/gif/Jd.gif")
new_image = tk.PhotoImage(file="/home/tom/Desktop/poker/images/gif/2s.gif")

# Create a Tkinter label for the background image
background_label = tk.Label(window, image=background)
background_label.pack()

# Set the position of the smaller image on top of the background image
position = (100, 100)  # Change the position as needed
image_label = tk.Label(window, image=first_image)
image_label.place(x=position[0], y=position[1])

# define a function that will be executed in the thread
def thread_function():
    print("Thread started")
    # do some work here...
    time.sleep(5)
    image_label.configure(image=new_image)
    print("Thread finished")

# create a new thread and start it
thread = threading.Thread(target=thread_function)

thread.start()

# Run the Tkinter event loop
window.mainloop()
