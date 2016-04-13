#!/usr/bin/python

import sys,tty,termios
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

def read_single_keypress():
    """Waits for a single keypress on stdin.

    This is a silly function to call if you need to do it a lot because it has
    to store stdin's current setup, setup stdin for reading single keystrokes
    then read the single keystroke then revert stdin back after reading the
    keystroke.

    Returns the character of the key that was pressed (zero on
    KeyboardInterrupt which can happen when a signal gets handled)

    """
    import termios, fcntl, sys, os
    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save) # copy the stored version to update
    # iflag
    attrs[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK 
                  | termios.ISTRIP | termios.INLCR | termios. IGNCR 
                  | termios.ICRNL | termios.IXON )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios. PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(termios.ECHONL | termios.ECHO | termios.ICANON
                  | termios.ISIG | termios.IEXTEN)
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)
    # read a single keystroke
    try:
        ret = sys.stdin.read(1) # returns a single character
    except KeyboardInterrupt: 
        ret = 0
    finally:
        # restore old state
        termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)
    return ret

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

def main():
	stack = []
	while True:
		key = get()
		#print key
		if key == 3:
			break;
		stack.append(key)
		if len(stack) > 0:
			if stack[0] == 27:
				if len(stack) > 1: 
					if stack[1] == 91:
						if len(stack) > 2:
							arrow = stack.pop()
							stack.pop()
							stack.pop()
							print arrow_key_str(arrow) + " arrow key"


def arrow_key_str(arrow):
	if arrow == 65:	return "up"
	if arrow == 66:	return "down"
	if arrow == 67:	return "right"
	if arrow == 68:	return "left"

if __name__=='__main__':
  main()
