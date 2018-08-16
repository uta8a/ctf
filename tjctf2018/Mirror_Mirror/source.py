#!/usr/bin/python -u

from __future__ import print_function
from code import InteractiveConsole
import code
import sys

getattr = getattr
eval = eval
execfile = execfile
bad = ["__class__", "__base__", "__subclasses__", "_module", "open", "eval", "execfile", "exec", "type", "lambda", "getattr", "setattr", "__", "file", "reload", "compile", "builtins", "os", "sys", "system"]
banned = ["vars", "getattr", "setattr", "delattr", "input", "raw_input", "help", "open", "memoryview", "eval", "exec", "execfile", "super", "file", "reload", "repr", "staticmethod", "property", "intern", "coerce", "buffer", "apply"]
bad.extend(banned)

def get_flag(input):
    super_secret_string = "this_is_the_super_secret_string"
    for each in str(input):
        val = ord(each)
        if((val >= 48 and val <= 57) or (val >= 65 and val <= 90) or (val >= 97 and val <= 122) or val == 44 or val == 95):
            print(each + " is not a valid character")
            sys.stdout.flush()
            return
    if(eval(input) == super_secret_string):
        print(`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((~(~(~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((~(~(~(~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~(((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((~(~(~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((~((~((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~(~(((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((~(~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((((~(~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((((~(({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~(~(~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((~(((~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((~(~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((((~(({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(~((~(((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((~(~(~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((((~(~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((~(((~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((((~(({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((~(~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((~(~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((((~(({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(((((~(({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((~((~(~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(~(((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(((((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~((~((~(~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%((~(~((~((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(~((~(((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[])))+`'%\xcb'`[{}<[]::~(~({}<[])<<({}<[]))]%(~(~(~((((~({}<[])<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))<<({}<[]))))
    else:
        print("You didn't guess the value of my super_secret_string")
    sys.stdout.flush()

class PseudoFile(object):

    def __init__(self, sh):
        self.sh = sh

    def write(self, s):
        self.sh.write(s)

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def flush(self):
        pass

    def isatty(self):
        return True

class Shell(code.InteractiveConsole):
    "Wrapper around Python that can filter input/output to the shell"

    def __init__(self):
        code.InteractiveConsole.__init__(self)
        self.thread = None


    def push(self, line):
        for any in bad:
            if any in line:
                print("Sorry, that's not allowed.")
                sys.stdout.flush()
                return
        return code.InteractiveConsole.push(self, line)

    def raw_input(self, prompt=""):
        print(">>>", end=" ")
        sys.stdout.flush()
        a = ""
        try:
            a = sys.stdin.readline().strip()
        except EOFError:
            pass
        return a

    def runcode(self, _code):
        org_stdout = sys.stdout
        sys.stdout = PseudoFile(self)
        try:
            exec _code in self.locals
        except SystemExit:
            raise
        except:
            self.showtraceback()
        else:
            if code.softspace(sys.stdout, 0):
                print

        sys.stdout = org_stdout

    def interact(self, banner=None):
        try:
            sys.ps1
        except AttributeError:
            sys.ps1 = ">>> "
        try:
            sys.ps2
        except AttributeError:
            sys.ps2 = "... "
        cprt = 'Type "help", "copyright", "credits" or "license" for more information.'
        if banner is None:
            self.write("Python %s on %s\n%s\n(%s)\n" %
                       (sys.version, sys.platform, cprt,
                        self.__class__.__name__))
        else:
            self.write("%s\n" % str(banner))
        more = 0
        while 1:
            try:
                if more:
                    prompt = sys.ps2
                else:
                    prompt = sys.ps1
                try:
                    line = self.raw_input(prompt)
                    # Can be None if sys.stdin was redefined
                    encoding = getattr(sys.stdin, "encoding", None)
                    if encoding and not isinstance(line, unicode):
                        line = line.decode(encoding)
                except EOFError:
                    self.write("\n")
                    break
                else:
                    more = self.push(line)
            except KeyboardInterrupt:
                self.write("\nKeyboardInterrupt\n")
                self.resetbuffer()
                more = 0

def main():
    banner = ("Hi! Are you looking for the flag? Try get_flag() for free flags. Remember, wrap your input in double quotes. Good luck!")

    a = __builtins__
    for each in a.__dict__.keys():
        if("__" in each):
            del a.__dict__[each]
    del a.__dict__["getattr"]
    del a.__dict__["eval"]
    del a.__dict__["execfile"]


    shell = Shell()
    shell.locals['get_flag'] = get_flag
    shell.locals['__builtins__'] = a
    shell.interact(banner=banner)

if __name__=="__main__":
    main()

