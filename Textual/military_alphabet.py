#!/usr/local/bin/python3.7
import sys
import subprocess

letters = [
    "Alfa",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo",
    "Foxtrot",
    "Golf",
    "Hotel",
    "India",
    "Juliett",
    "Kilo",
    "Lima",
    "Mike",
    "November",
    "Oscar",
    "Papa",
    "Quebec",
    "Romeo",
    "Sierra",
    "Tango",
    "Uniform",
    "Victor",
    "Whiskey",
    "X-ray",
    "Yankee",
    "Zulu"
]

def convert_to_nato(tc, copy_to=True):
    res = ""

    for char in tc:
        if char.isalpha() and ord(char) < 123:
            res += letters[ord(char.upper()) - 65] + " "

    if copy_to: copy_to_clipboard(res)
    else: return res

def copy_to_clipboard(output): #Thank you https://gist.github.com/luqmaan/d8bc61e746207bb12f11
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode())

if __name__ == "__main__":
    if sys.argv.__len__() == 1:
        convert_to_nato("OWO, What's this?".strip())
    elif sys.argv.__len__() == 2:
        convert_to_nato(sys.argv[1].strip())
    elif sys.argv.__len__() >= 3:
        result = ""
        if sys.argv[1].lower() == "-f":
            for arg in sys.argv[2:]:
                result += convert_to_nato(arg, False)
            print(result.strip())
        else:
            result = ""
            for arg in sys.argv[1:]:
                result += convert_to_nato(arg, False)
            copy_to_clipboard(result.strip())
