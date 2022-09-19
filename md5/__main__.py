import sys
from md5.md5 import digest


def main():
    print(digest(sys.stdin.buffer.read()).hex())
