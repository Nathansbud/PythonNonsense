#!/Users/zackamiton/Code/PythonNonsense/venv/bin/python
import sys

sys.argv = [l.lower() for l in sys.argv]
if len(sys.argv) > 1:
    if sys.argv[1] == "you": print("No, fuck you!")
    elif sys.argv[1] == "me": print("I wouldn't dream of it!")
else:
    print("Yep.")