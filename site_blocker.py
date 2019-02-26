#!/usr/bin/python

import os
import time

block_list = [
    "www.youtube.com",
    "www.reddit.com",
    "www.instagram.com",
    "www.twitter.com",
    "www.myspace.com"
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
    hosts.close()
    hosts = open("/private/etc/hosts", "a")

    if (time.localtime().tm_hour > 15 or time.localtime().tm_hour < 8) or time.localtime().tm_wday >= 5:
        for b in block_list:
            hosts.write("127.0.0.1\t" + b + "\n")
        os.system("dscacheutil -flushcache")

    hosts.close()

if __name__ == "__main__":
    main()
    pass