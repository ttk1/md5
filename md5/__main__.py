import sys
from md5 import MD5, MD4

READ_SIZE = 1024 * 1024 * 5


def main():
    md5 = MD5()
    while True:
        read_data = sys.stdin.buffer.read(READ_SIZE)
        md5.update(read_data)
        if (len(read_data) != READ_SIZE):
            break
    print(md5.digest().hex())


def main_md4():
    md4 = MD4()
    while True:
        read_data = sys.stdin.buffer.read(READ_SIZE)
        md4.update(read_data)
        if (len(read_data) != READ_SIZE):
            break
    print(md4.digest().hex())
