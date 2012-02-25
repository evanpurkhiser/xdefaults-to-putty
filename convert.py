#!/usr/bin/python
import sys, re

# Read the passed Xdefaults file
colors = open(sys.argv[1], 'r').readlines()

# Iterate over the colors in the Xdefaults file
for line in colors:

	# Match the color value and name
	color = re.match(r"\*(color[0-9]+):.*#(.{6})", line)

	if not color:
		continue

	print color.group(1, 2)