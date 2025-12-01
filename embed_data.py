import json

# Read plot data
with open('plot_data.json', 'r') as f:
    plot_data = f.read()

# Read HTML file
with open('servo apres.html', 'r') as f:
    html_content = f.read()

# Prepare the injection string
injection = f"const PLOT_DATA = {plot_data};\n"

# Find the insertion point
target = "const sections ="
if target in html_content:
    new_html_content = html_content.replace(target, injection + target)
    
    # Write back to file
    with open('servo apres.html', 'w') as f:
        f.write(new_html_content)
    print("Successfully embedded plot data.")
else:
    print("Error: Could not find insertion point 'const sections ='")
