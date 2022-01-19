import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from time import sleep


def TextBoxes(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)

    a1 = curses.color_pair(1)
    a2 = curses.color_pair(2)

    win = curses.newwin(7, 25, 2, 2)
    box = Textbox(win)
    rectangle(stdscr, 1, 1, 9, 27)
    stdscr.refresh()

    box.edit()
    text1 = box.gather().replace("\n", "").strip()

    stdscr.addstr(11, 40, text1, curses.A_STANDOUT)

    stdscr.getch()


wrapper(TextBoxes)
