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

# Read the passed Xdefaults file
colors = open(sys.argv[1], 'r').readlines()

# Iterate over the colors in the Xdefaults file
for line in colors:

	# Match the color value and name
	color = re.match(r"\*(color[0-9]+):.*#(.{6})", line)

	if not color:
		continue

	print color.group(1, 2)