# produced by chatgpt from a short conversation (and then adapted)
# on ubuntu it requires sudo apt-get install python3-tk

import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Load the background image
background = tk.PhotoImage(file="/home/tom/Desktop/poker/images/gif/background.gif")

# Load the smaller image
smaller_image = tk.PhotoImage(file="/home/tom/Desktop/poker/images/gif/As.gif")

# Create a Tkinter label for the background image
background_label = tk.Label(window, image=background)
background_label.pack()

# Set the position of the smaller image on top of the background image
position = (100, 100)  # Change the position as needed
smaller_image_label = tk.Label(window, image=smaller_image)
smaller_image_label.place(x=position[0], y=position[1])

# Run the Tkinter event loop
window.mainloop()
