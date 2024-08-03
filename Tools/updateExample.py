# https://github.com/median-dispersion/Software-Development-Icons

# A script for generating HTML / JavaScript that is being used to update the example page

import os
import re

# Generate HTML for an icon section on the example page
def generateHTML(path, name):

    # HTML template for an icon section
    html = f"""
    <div class="main-section-item">

        <div class="main-section-item-icon" style="background-image: url('{path}');"></div>
        <div class="main-section-item-text">{name}</div>

    </div>
    """

    # Return the HTML string without any line breaks or indentations
    return re.sub(r"[\s]+", " ", html).strip()

# Style of icon, it's path, and a string that will contain the HTML content for the example page
icons = {

    "filled": {

        "path": "../Icons/Filled",
        "html": ""

    },

    "outlined": {

        "path": "../Icons/Outlined",
        "html": ""

    }

}

# For each style of icon
for style in icons:

    # Loop through all subdirectories and files 
    for root, dirs, files in os.walk(icons[style]["path"]):

        # Sort files in alphabetical order
        files.sort()

        # For all files
        for file in files:

            # Check if the file is a ".svg"
            if os.path.splitext(file)[1].lower() == ".svg":

                # Generate the HTML and add it to the HTML string for that style of icon
                icons[style]["html"] += (generateHTML(os.path.join(root, file), file))

# JavaScript template that dynamically injects the generated HTML into the example page
javascript = f"""
// https://github.com/median-dispersion/Software-Development-Icons

// This file was created by {os.path.basename(__file__)}

// Icon HTML strings
const filled = `{icons["filled"]["html"]}`;
const outlined = `{icons["outlined"]["html"]}`;

// Once the page has finished loading
document.addEventListener("DOMContentLoaded", () => {{

    // Inject the HTML at the end of the appropriate section
    document.getElementById("filled").insertAdjacentHTML("beforeend", filled);
    document.getElementById("outlined").insertAdjacentHTML("beforeend", outlined);

}});
"""

# Write the JavaScript to a file
with open("../Example/icons.js", "w") as out: out.write(javascript.strip())