#!/usr/local/opt/python/bin/python3.7

import os
import time
import sys

block_list = [
    "www.youtube.com",
    "www.reddit.com",
    "www.instagram.com",
    "www.twitter.com",
    "www.tetrisfriends.com"
]


def main():
    os.chdir("/private/etc")
    hosts = open("/private/etc/hosts", "r")

    lines = []

    passed = False

    for line in hosts:
        lines.append(line)

    hosts.close()
    hosts = open("/private/etc/hosts", "w")


    for line in lines:
        if passed:
            break
        else:
            hosts.write(line)
            if line.replace("\n", "") == "##BLOCK##":
                passed = True

    if sys.argv.__len__() > 1:
        hosts.close()
        hosts = open("/private/etc/hosts", "a")
        for b in block_list:
            hosts.write("127.0.0.1\t" + b + "\n")
        os.system("dscacheutil -flushcache")

        hosts.close()
        print("Sites blocked!")
    else:
        print("Sites unblocked!")

if __name__ == "__main__":
    main()
    pass