import curses
from time import sleep
from curses import wrapper  # ! It's Used to initialize a function


def simple(stdscr):
    stdscr.clear()
    # sleep(10)
    stdscr.addstr("Hello World!")
    stdscr.refresh()
    stdscr.getch()


def arranging(stdscr):
    stdscr.clear()
    # sleep(10)
    stdscr.addstr(15, 50, "Hello World!")
    stdscr.refresh()
    stdscr.getch()


def styling(stdscr):
    stdscr.clear()
    # sleep(10)
    stdscr.addstr(15, 50, "Normal Text")
    stdscr.addstr(16, 50, "Bold Text", curses.A_BOLD)
    stdscr.addstr(17, 50, "Blink/highlight Text", curses.A_BLINK)
    stdscr.addstr(18, 50, "Reverse Forground and BackGround", curses.A_REVERSE)
    stdscr.addstr(19, 50, "Underlined Text", curses.A_UNDERLINE)
    stdscr.addstr(20, 50, "Italic Text", curses.A_ITALIC)
    stdscr.addstr(21, 50, "DIM Text", curses.A_DIM)
    stdscr.addstr(22, 50, "STANDOUT Text", curses.A_STANDOUT)

    stdscr.refresh()
    stdscr.getch()


def coloring(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_WHITE)

    GREEN_AND_RED = curses.color_pair(1)
    MAGENTA_AND_CYAN = curses.color_pair(2)
    YELLOW_AND_WHITE = curses.color_pair(3)

    stdscr.clear()
    # sleep(10)
    stdscr.addstr(15, 50, "Hello World!", GREEN_AND_RED)
    stdscr.addstr(17, 50, "Harsh Patel Op", MAGENTA_AND_CYAN)
    stdscr.addstr(19, 50, "We Love India!", MAGENTA_AND_CYAN)

    stdscr.refresh()
    stdscr.getch()


def StyleAndColor(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    GREEN_AND_BLUE = curses.color_pair(1)
    stdscr.clear()

    stdscr.addstr(15, 50, "Hello World!", GREEN_AND_BLUE | curses.A_REVERSE)

    stdscr.refresh()
    stdscr.getch()


def SimpleLooping(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)

    a1 = curses.color_pair(1)
    a2 = curses.color_pair(2)

    for i in range(100):
        # stdscr.clear()

        COLOR = a1
        if i % 2 != 0:
            COLOR = a2

        stdscr.addstr(f"Counter = {i}", COLOR)
        stdscr.refresh()
        sleep(0.1)

    stdscr.getch()


def Windows(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)

    a1 = curses.color_pair(1)
    a2 = curses.color_pair(2)

    counter_win = curses.newwin(1, 20, 15, 50)
    stdscr.addstr("Hello World!")

    for i in range(100):
        counter_win.clear()

        COLOR = a1
        if i % 2 != 0:
            COLOR = a2

        counter_win.addstr(f"Counter = {i}", COLOR)
        counter_win.refresh()
        sleep(0.1)

    stdscr.getch()


def Pad(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)

    a1 = curses.color_pair(1)
    a2 = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            COLOR = a1
            if j % 2 != 0:
                COLOR = a2

            char = chr(67 + j)
            pad.addstr(char, COLOR)

    for i in range(50):  # ! scrolling pad
        pad.refresh(0, i, 5, 5, 10, 55)
        sleep(0.2)
    stdscr.getch()

    for i in range(50):  # ! rolling and moving pad
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, 0, 5, i, 10, 25 + i)
        sleep(0.2)
    stdscr.getch()


wrapper(Pad)
