#!/usr/bin/python3
"""
AirBNB clone console
"""
import cmd


class AirbnbShell(cmd.Cmd):
    """Implementation of an AirBNB CLI"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Command Exit console on EOF signal (^D)"""
        return True

    def do_quit(self, line):
        """Exit console on normal quit"""
        return True


if __name__ == '__main__':
    AirbnbShell().cmdloop()
