#!/usr/bin/python

import os
import time

max_rows, max_columns = os.popen('stty size', 'r').read().split()
max_rows = int(max_rows)
max_columns = int(max_columns)


def main():
	clear_reset()

	files = os.popen('ls -l --color=auto /', 'r').read().split("\n")

	if max_rows<len(files):
		rows = max_rows
	else:
		rows = len(files)
	for i in range(1, rows):
		#row = i % int(rows)
		#print_coord(row, row, "omgggggg")
		#time.sleep(0.05)
		#print_coord(row, row, "        ")
		print_coord(i, 1, files[i])
		x = 5
	

def print_coord(row, column, string):
	print "\033[" + str(row) + ";" + str(column) + "H" + string

def clear_console():
	print "\033[2J\033[1;1H"

def clear_reset():
	rows, columns = os.popen('stty size', 'r').read().split()
	for i in range(1, int(rows)):
		print_coord(i, 1, ' '*int(columns))
	print "\033[1;1H"

main()
