import sys
from contextlib import contextmanager


@contextmanager
def typing_disabled():
    """Hide and discard keystrokes while the agent is replying."""
    if not sys.stdin.isatty():
        yield
        return

    try:
        import termios
    except ImportError:  # Windows
        try:
            yield
        finally:
            import msvcrt

            while msvcrt.kbhit():
                msvcrt.getch()
        return

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ECHO  # index 3 = local flags; turn echo off
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        yield
    finally:
        termios.tcflush(fd, termios.TCIFLUSH)  # drop anything typed meanwhile
        termios.tcsetattr(fd, termios.TCSADRAIN, old)  # restore the terminal
