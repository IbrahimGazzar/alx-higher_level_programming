#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
print(f"{argc} argument", end="")
if argc != 1:
    print("s", end="")
if argc == 0:
    print(".")
else:
    print(":")
for i in range(1, argc + 1):
    print(f"{i}: {argv[i]}")
