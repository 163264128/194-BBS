from ascii_magic import AsciiArt

# Load your image
my_art = AsciiArt.from_image('hoopa_fan_art.png')

# Convert to HTML (adjust columns for more/less detail)
my_art.to_html_file('index.html', columns=200, width_ratio=2)
print("Success! index.html has been created.")
