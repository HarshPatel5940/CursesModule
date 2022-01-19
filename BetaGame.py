import curses
from curses import wrapper

def main(stdscr):
    stdscr.nodelay(True)
    x, y = 0, 0
    # coord = 0
    while True:
        try:
            KEY = stdscr.getkey()
        except:
            KEY = None
        if KEY == "KEY_LEFT":
            x -= 1
        if KEY == "KEY_RIGHT":
            x += 1
        if KEY == "KEY_DOWN":
            y += 1
        if KEY == "KEY_UP":
            y -= 1
        stdscr.clear()
        # coord += 1
        # stdscr.addstr(0, coord // 50, "===> Hello World! ===>")
        stdscr.addstr(y, x, "#")
        stdscr.refresh()

wrapper(main)
