#!/usr/bin/python

import sys,tty,termios
import os

COLOR_END    = "\033[0m"
COLOR_BLACK  = "\033[7;30m"
COLOR_BLUE   = "\033[0;34m"
COLOR_GREEN  = "\033[0;32m"
COLOR_CYAN   = "\033[0;36m"
COLOR_RED    = "\033[0;31m"
COLOR_PURPLE = "\033[0;35m"
COLOR_BROWN  = "\033[0;33m"
COLOR_LGRAY  = "\033[0;37m"
COLOR_WHITE  = "\033[7;97m"

screen = [[' ']*200 for i in range(200)]

def main2():
	print COLOR_WHITE + " OOOOOMG" + COLOR_END + "my"


def main():
	init_screen()

	cursor_pos = [1, 1]
	prev_pos = [1, 1]
	
	display_list = os.popen('ls -l --color=auto /').read().split("\n")
	
	i=0
	#for item in display_list:
	#	if i == 1:
	#		print COLOR_RED + item + COLOR_END
	#	else:
	#		print item
	#	i = i+1

	while True:
		key = get_key()
		if key == 3:
			break
		elif key>=65 and key<=68:
			prev_pos = list(cursor_pos)
			if key == 65: cursor_pos[1] = cursor_pos[1] - 1
			elif key == 66: cursor_pos[1] = cursor_pos[1] + 1
			elif key == 67: cursor_pos[0] = cursor_pos[0] + 1
			elif key == 68: cursor_pos[0] = cursor_pos[0] - 1
			#draw_cursor(prev_pos, cursor_pos)		
			#draw_coord(cursor_pos)
			#draw_screen()
			if cursor_pos[1] >= len(display_list):
				cursor_pos[1] = len(display_list)-1
			if cursor_pos[1] < 1:
				cursor_pos[1] = 1
			print cursor_pos[1]
			draw_list(display_list, cursor_pos[1])
		else:
			#print "\033[" + str(cursor_pos[1]) + ";" + str(cursor_pos[1]) + "H"
			print ""


def init_screen():
	rows, columns = os.popen('stty size', 'r').read().split()
	rows = int(rows)
	columns = int(columns)

	screen = [[' ']*columns for i in range(rows)]

	draw_screen()

def draw_screen():
	max_rows, max_columns = os.popen('stty size', 'r').read().split()
	max_rows = int(max_rows)
	max_columns = int(max_columns)
	
	for i in range(0, max_rows):
		row = "".join(screen[i])
		print_coord(i+1, 1, row)
		print "\033[1;1H"

def draw_list(l, selected):
	max_rows, max_columns = os.popen('stty size', 'r').read().split()
	max_rows = int(max_rows)
	max_columns = int(max_columns)
	if len(l) > max_rows:
		size = max_rows
	else:
		size = len(l)
	
	for i in range(size):
		if i == selected:
			print COLOR_WHITE
		print_coord(i, 1, l[i-1])
		print COLOR_END

def draw_cursor(prev_pos, cursor_pos):
	screen[prev_pos[1]-1][prev_pos[0]-1] = '+'
	print prev_pos
	screen[cursor_pos[1]-1][cursor_pos[0]-1] = 'B'
	#print screen
	#draw_screen()

def draw_coord(cursor_pos):
	screen[60][40] = 'A'#str(cursor_pos[0])
	screen[60][40] = 'B'#str(cursor_pos[1])
	#print screen
	#draw_screen()





def print_coord(row, column, string):
   print "\033[" + str(row) + ";" + str(column) + "H" + string

def arrow_key_action(key):
	return 0

def arrow_key_str(arrow):
	if arrow == 65:	return "up"
	if arrow == 66:	return "down"
	if arrow == 67:	return "right"
	if arrow == 68:	return "left"

class _Getch:
	def __call__(self):
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch


def get():
	inkey = _Getch()
	while(1):
		k=inkey()
		return ord(k)
		if k!='': break

        #if k=='\x1b[A':
        #        print "up"
        #elif k=='\x1b[B':
        #        print "down"
        #elif k=='\x1b[C':
        #        print "right"
        #elif k=='\x1b[D':
        #        print "left"
        #else:
        #        print "not an arrow key!"

def get_key():
	stack = []
	while True:
		key = get()
		#print key
		stack.append(key)
		if len(stack) > 0:
			if stack[0] == 27:
				if len(stack) > 1: 
					if stack[1] == 91:
						if len(stack) > 2:
							arrow = stack.pop()
							stack.pop()
							stack.pop()
							return arrow
			else:
				return key




if __name__=='__main__':
	main()




