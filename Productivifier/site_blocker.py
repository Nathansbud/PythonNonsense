#!/usr/local/opt/python/bin/python3.7

import os
import time
import sys

strict_block = True

block_list = [
   # "www.youtube.com",
    "www.reddit.com",
   # "www.instagram.com",
   # "www.twitter.com",
   # "www.tetrisfriends.com"
]

strict_block_list = [
    "www.facebook.com",
    "www.messenger.com"
]


def block_sites():
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
    if strict_block:
        for b in block_list + strict_block_list:
            hosts.write("127.0.0.1\t" + b + "\n")
    else:
        for b in block_list:
            hosts.write("127.0.0.1\t" + b + "\n")
    os.system("dscacheutil -flushcache")

    hosts.close()
    print("Sites blocked!")


if __name__ == "__main__":
    block_sites()
    pass
