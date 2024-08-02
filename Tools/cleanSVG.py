# https://github.com/median-dispersion/Software-Development-Icons

# A script for cleaning SVG files, that contain only one path, to the bare minimum

import sys
import os
import re

# Check if a path was provided as an argument
if len(sys.argv) == 1:

    # If not, ask for a path
    rootPath = input("Please provide a path: ").strip('\'"')

else:
    
    # Else use provided path
    rootPath = sys.argv[1]

# Loop through all subdirectories and files 
for root, dirs, files in os.walk(rootPath):

    # For all files
    for file in files:

        # Check if the file is a ".svg"
        if os.path.splitext(file)[1].lower() == ".svg":

            # Get the full file path
            filePath = os.path.join(root, file)

            # Read the content of the SVG file
            with open(filePath, "r") as svg: svgContent = svg.read()

            # Write that content to a ".backup" file with the same name as the original
            with open(f"{filePath}.backup", "w") as backup: backup.write(svgContent)
            
            # Get the coordinates / points from the SVG file
            svgPoints = re.findall(r'd="(.*?)"', svgContent)[0]

            # Put the extracted points into an SVG template
            svgOutput = f'<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" fill="#fff"><path d="{svgPoints}"/></svg>'

            # Write the output to the original SVG file
            with open(filePath, "w") as svg: svg.write(svgOutput)