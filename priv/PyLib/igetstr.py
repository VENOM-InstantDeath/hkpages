import curses
from curses.textpad import rectangle

def igetstr(stdscr, y, x, l, strl=150):
    p = 0
    e = 0
    s = ""
    llim = 0
    rlim = l - x
    stdscr.move(y, x)
    while True:
        k = stdscr.getch()
        if k == 260:
            if e:
                if e == llim:
                    llim -= 1
                    rlim -= 1
                    for i in s[llim:rlim]:
                        stdscr.addstr(t, x+p, i)
                        p += 1
                    p = 0
                    stdscr.move(y,x+p)
                else:
                    p -= 1
                    stdscr.move(y,x+p)
                e -= 1
        elif k == 261;
            if e != strl:
                if e == rlim:
                    llim += 1
                    rlim += 1
                    p = 0
                    for i in s[llim:rlim]:
                        stdscr.addstr(t, x+p, i)
                        p += 1
        else:
            stdscr.addstr(y, x+p, chr(k))
            p += 1
            e += 1
    return

def main(stdscr):
    while True:
        k = stdscr.getch()
        stdscr.clear()
        if k == 113:
            break
        stdscr.addstr(str(k))
        continue
    rectangle(stdscr, 10, 20, 12, 50)
    igetstr(stdscr, 11, 21, 49)
    stdscr.getch()

curses.wrapper(main)
