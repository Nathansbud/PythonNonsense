import os
import sys

accepted_args = ["-r", "-w"]
def validate(args):
    not_accepted = set()
    for a in args:
        if not a in accepted_args:
            not_accepted.add(a)
    return len(not_accepted) == 0, not_accepted


if len(sys.argv) > 1:
    passed, failed = validate(sys.argv[1:])
    if passed:
        print("Nothing wrong!")
    else:
        print(f'Unrecognized arguments: {", ".join(failed)}')



