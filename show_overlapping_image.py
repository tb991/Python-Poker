from PIL import Image

# Open the background image file
background = Image.open("/home/tom/Desktop/poker/images/background.jpg")

# Open the smaller image file
smaller_image = Image.open("/home/tom/Desktop/poker/images/As.jpg")

# Create a copy of the background image
background_copy = background.copy()

# Paste the smaller image onto the background copy
position = (100, 100)  # Change the position as needed
background_copy.paste(smaller_image, position)

# Display the combined image
background_copy.show()
