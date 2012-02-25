#!/usr/bin/python
import sys, re, os

# Do some error checking
if len(sys.argv) < 2:
	print "Please enter the xdefaults file path"
	raise SystemExit

if len(sys.argv) < 3:
	print "Please enter atleast one Putty session name"
	raise SystemExit

if not os.path.exists(sys.argv[1]):
	print "The given xdefaults color file does not exist"
	raise SystemExit

# Read the passed Xdefaults file
colors = open(sys.argv[1], 'r').readlines()

# Store the putty color values in here
new_colors = ""

# Color map from xefault color code => Putty color code (possible multiple)
color_map = {
	'foreground': ['Colour0', 'Colour1'],
	'background': ['Colour2', 'Colour3'],
	'color0':     ['Colour6'],
	'color8':     ['Colour7'],
	'color1':     ['Colour8'],
	'color9':     ['Colour9'],
	'color2':     ['Colour10'],
	'color10':    ['Colour11'],
	'color3':     ['Colour12'],
	'color11':    ['Colour13'],
	'color4':     ['Colour14'],
	'color12':    ['Colour15'],
	'color5':     ['Colour16'],
	'color13':    ['Colour17'],
	'color6':     ['Colour18'],
	'color14':    ['Colour19'],
	'color7':     ['Colour20'],
	'color15':    ['Colour21']
}

# Iterate over the colors in the Xdefaults file
for line in colors:

	# Match the color value and name
	color = re.match(r"\*(.+):.*#(.{6})", line)

	# Make sure the color code exists in the color map
	if not color or not color.group(1) in color_map:
		continue

	# Get the RGB value of this color
	rgb = tuple(int(color.group(2)[i:i+2], 16) for i in range(0, 6, 2))

	# Add the new value to the new_colors dictionary
	for color_key in color_map[color.group(1)]:
		new_colors += '"{key}"="{color}"\n'.format(
			key   = color_key,
			color = ','.join(map(str, rgb))
		)

# Setup the registry file header
registry_string = "[HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\{session}]\n{values}"

# Output the registry header that windows needs
print "Windows Registry Editor Version 5.00\n"

# Output the registry script
for session in sys.argv[2:]:
	print registry_string.format(session = session, values = new_colors)