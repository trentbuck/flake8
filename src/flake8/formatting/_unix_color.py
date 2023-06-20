import curses

try:
    curses.initscr()
    terminal_supports_color = curses.has_colors()
    curses.endwin()
except curses.error:
    # "I can't tell if color is supported" should logically be None.
    # Use True for consistency with _windows_color.
    terminal_supports_color = True
