#!/usr/bin/python

import subprocess
import sys

def clipboard_write(output):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

def alternating_case(t):
    replace = ""
    for i in range(0, len(t)):
        if i % 2 == 0:
            replace += t[i].upper()
        else:
            replace += t[i]
    return replace

def space_case(t, double_space = True):
    replace = ""
    for i in range(0, len(t)):
        if double_space or t[i] != " ":
            replace += t[i].upper() + " "
        else:
            replace += t[i].upper()
    return replace

if __name__ == "__main__":
    args = sys.argv
    text = ''.join(str(s + " ") for s in args[2:])
    if args[1] == "0":
        clipboard_write(alternating_case(text))
    elif args[1] == "1":
        clipboard_write(space_case(text))
    elif args[1] == "2":
        clipboard_write(space_case(text, False))
    pass