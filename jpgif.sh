# made by asking ChatGPT "show me a bash script where all jpegs in the current directory are converted to gifs using convert and a for loop"

#!/bin/bash

# Loop through all JPEG images in the current directory and convert them to GIF format
for file in *.jpg
do
    # Get the filename without the extension
    filename=$(basename "$file" .jpg)
    
    # Convert the file to GIF format
    convert "$file" "$filename.gif"
done

