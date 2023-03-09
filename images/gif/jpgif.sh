#!/bin/bash

# Loop through all JPEG images in the current directory and convert them to GIF format
for file in *.jpg
do
    # Get the filename without the extension
    filename=$(basename "$file" .jpg)
    
    # Convert the file to GIF format
    convert "$file" "$filename.gif"
done

