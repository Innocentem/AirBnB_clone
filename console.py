#!/usr/bin/python3
"""
AirBNB clone console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Implementation of an AirBNB CLI"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Command to exit the console on EOF signal (^D)"""
        return True

    def do_quit(self, line):
        """Quit command to exit the console"""
        return True

    def emptyline(self) -> bool:
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

