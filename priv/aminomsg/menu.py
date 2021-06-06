import curses

def scroll(stdscr, y, x, d, limit):
    curses.use_default_colors()
    curses.init_pair(15, 0, 15)
    it = list(d.keys())
    p = 0
    e = 0
    mp = 0
    minpag = 0
    maxpag = limit-1
    for i in it[0:limit]:
        stdscr.addstr(y+p, x, i)
        p += 1
    p = 0
    stdscr.addstr(y+p,x, it[e], curses.color_pair(15))
    while True:
        k = stdscr.getch()
        if k == 259:
            if e:
                if e == minpag:
                    maxpag -= 1
                    minpag -= 1
                    stdscr.move(y,x);stdscr.clrtobot()
                    mp = 0
                    for i in it[minpag:maxpag]:
                        stdscr.addstr(y+mp, x, i)
                        mp += 1
                else:
                    stdscr.addstr(y+p, x, it[e])
                    p -= 1
                e -= 1
                stdscr.addstr(y+p, x, it[e], curses.color_pair(15))
        if k == 258:
            if e != len(it)-1:
                if e == maxpag:
                    maxpag += 1
                    minpag += 1
                    stdscr.move(y,x);stdscr.clrtobot()
                    mp = 0
                    for i in it[minpag:maxpag]:
                        stdscr.addstr(y+mp, x, i)
                        mp += 1
                else:
                    stdscr.addstr(y+p, x, it[e])
                    p += 1
                e += 1
                stdscr.addstr(y+p, x, it[e], curses.color_pair(15))
        if k == 10:
            res=d[it[e]]()
            if res:
                return res
            return


def menu(stdscr, y, x, d):
    curses.use_default_colors()
    curses.init_pair(15, 0, 15)
    it = list(d.keys())
    p = 0
    for i in d:
        stdscr.addstr(y+p, x, i)
        p += 1
    p = 0
    stdscr.addstr(y+p,x, it[p], curses.color_pair(15))
    while True:
        k = stdscr.getch()
        if k == 259:
            if p:
                stdscr.addstr(y+p, x, it[p])
                p -= 1
                stdscr.addstr(y+p, x, it[p], curses.color_pair(15))
        if k == 258:
            if p != len(it)-1:
                stdscr.addstr(y+p, x, it[p])
                p += 1
                stdscr.addstr(y+p, x, it[p], curses.color_pair(15))
        if k == 10:
            res=d[it[p]]()
            if res:
                return res
            return

if __name__ == "__main__":
    def main(stdscr):
        curses.use_default_colors()
        curses.init_pair(15, 0, 15)
        menu(stdscr, 10, 20, {"exit": exit, "print": lambda: stdscr.addstr(1,0,"hello")})
    curses.wrapper(main)
