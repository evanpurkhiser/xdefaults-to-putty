#!/usr/bin/python
import sys, re

# Color map from xefault color code => Putty color code
color_map = {
	'foreground': ('color0', 'color1'),
	'background': ('color2', 'color3'),
	'color0':     'color6',
	'color8':     'color7',
	'color1':     'color8',
	'color9':     'color9',
	'color2':     'color10',
	'color10':    'color11',
	'color3':     'color12',
	'color11':    'color13',
	'color4':     'color14',
	'color12':    'color15',
	'color5':     'color16',
	'color13':    'color17',
	'color6':     'color18',
	'color14':    'color19',
	'color7':     'color20',
	'color15':    'color21'
}

# Setup the registry file header
registry_string = "[HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\{session}]\n{values}"

# Store the putty color values in here
new_colors = ""

# Read the passed Xdefaults file
colors = open(sys.argv[1], 'r').readlines()

# Iterate over the colors in the Xdefaults file
for line in colors:

	# Match the color value and name
	color = re.match(r"\*(.+):.*#(.{6})", line)

	# Make sure the color code exists in the color map
	if not color or not color.group(1) in color_map:
		continue

	# Add the new value to the new_colors dictionary
	new_colors += '"{key}"="{color}"\n'.format(
		key   = color_map[color.group(1)],
		color = tuple(int(color.group(2)[i:i+2], 16) for i in range(0, 6, 2))
	)

# Output the registry header that windows needs
print "Windows Registry Editor Version 5.00\n"

# Output the registry script
for session in sys.argv[2:]:
	print registry_string.format(session = session, values = new_colors)