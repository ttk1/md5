class MD4():
    def __init__(self):
        self._A = 0x67452301
        self._B = 0xefcdab89
        self._C = 0x98badcfe
        self._D = 0x10325476
        self._data = b''
        self._size = 0

    def _f1(self, a: int, b: int, c: int, d: int, k: int, s: int):
        return rotate((a + F(b, c, d) + self._X[k]) & 0xffffffff, s)

    def _f2(self, a: int, b: int, c: int, d: int, k: int, s: int):
        return rotate((a + G(b, c, d) + self._X[k] + 0x5a827999) & 0xffffffff, s)

    def _f3(self, a: int, b: int, c: int, d: int, k: int, s: int):
        return rotate((a + H(b, c, d) + self._X[k] + 0x6ed9eba1) & 0xffffffff, s)

    def _update(self, data: bytes):
        self._X = [int.from_bytes(data[i:i+4], byteorder='little')
                   for i in range(0, 64, 4)]
        AA = self._A
        BB = self._B
        CC = self._C
        DD = self._D

        # Round 1.
        self._A = self._f1(self._A, self._B, self._C, self._D, 0, 3)
        self._D = self._f1(self._D, self._A, self._B, self._C, 1, 7)
        self._C = self._f1(self._C, self._D, self._A, self._B, 2, 11)
        self._B = self._f1(self._B, self._C, self._D, self._A, 3, 19)
        self._A = self._f1(self._A, self._B, self._C, self._D, 4, 3)
        self._D = self._f1(self._D, self._A, self._B, self._C, 5, 7)
        self._C = self._f1(self._C, self._D, self._A, self._B, 6, 11)
        self._B = self._f1(self._B, self._C, self._D, self._A, 7, 19)
        self._A = self._f1(self._A, self._B, self._C, self._D, 8, 3)
        self._D = self._f1(self._D, self._A, self._B, self._C, 9, 7)
        self._C = self._f1(self._C, self._D, self._A, self._B, 10, 11)
        self._B = self._f1(self._B, self._C, self._D, self._A, 11, 19)
        self._A = self._f1(self._A, self._B, self._C, self._D, 12, 3)
        self._D = self._f1(self._D, self._A, self._B, self._C, 13, 7)
        self._C = self._f1(self._C, self._D, self._A, self._B, 14, 11)
        self._B = self._f1(self._B, self._C, self._D, self._A, 15, 19)

        # Round 2.
        self._A = self._f2(self._A, self._B, self._C, self._D, 0, 3)
        self._D = self._f2(self._D, self._A, self._B, self._C, 4, 5)
        self._C = self._f2(self._C, self._D, self._A, self._B, 8, 9)
        self._B = self._f2(self._B, self._C, self._D, self._A, 12, 13)
        self._A = self._f2(self._A, self._B, self._C, self._D, 1, 3)
        self._D = self._f2(self._D, self._A, self._B, self._C, 5, 5)
        self._C = self._f2(self._C, self._D, self._A, self._B, 9, 9)
        self._B = self._f2(self._B, self._C, self._D, self._A, 13, 13)
        self._A = self._f2(self._A, self._B, self._C, self._D, 2, 3)
        self._D = self._f2(self._D, self._A, self._B, self._C, 6, 5)
        self._C = self._f2(self._C, self._D, self._A, self._B, 10, 9)
        self._B = self._f2(self._B, self._C, self._D, self._A, 14, 13)
        self._A = self._f2(self._A, self._B, self._C, self._D, 3, 3)
        self._D = self._f2(self._D, self._A, self._B, self._C, 7, 5)
        self._C = self._f2(self._C, self._D, self._A, self._B, 11, 9)
        self._B = self._f2(self._B, self._C, self._D, self._A, 15, 13)

        # Round 3.
        self._A = self._f3(self._A, self._B, self._C, self._D, 0, 3)
        self._D = self._f3(self._D, self._A, self._B, self._C, 8, 9)
        self._C = self._f3(self._C, self._D, self._A, self._B, 4, 11)
        self._B = self._f3(self._B, self._C, self._D, self._A, 12, 15)
        self._A = self._f3(self._A, self._B, self._C, self._D, 2, 3)
        self._D = self._f3(self._D, self._A, self._B, self._C, 10, 9)
        self._C = self._f3(self._C, self._D, self._A, self._B, 6, 11)
        self._B = self._f3(self._B, self._C, self._D, self._A, 14, 15)
        self._A = self._f3(self._A, self._B, self._C, self._D, 1, 3)
        self._D = self._f3(self._D, self._A, self._B, self._C, 9, 9)
        self._C = self._f3(self._C, self._D, self._A, self._B, 5, 11)
        self._B = self._f3(self._B, self._C, self._D, self._A, 13, 15)
        self._A = self._f3(self._A, self._B, self._C, self._D, 3, 3)
        self._D = self._f3(self._D, self._A, self._B, self._C, 11, 9)
        self._C = self._f3(self._C, self._D, self._A, self._B, 7, 11)
        self._B = self._f3(self._B, self._C, self._D, self._A, 15, 15)

        self._A = (self._A + AA) & 0xffffffff
        self._B = (self._B + BB) & 0xffffffff
        self._C = (self._C + CC) & 0xffffffff
        self._D = (self._D + DD) & 0xffffffff

    def update(self, data: bytes):
        self._data += data
        self._size += len(data)
        while len(self._data) >= 64:
            self._update(self._data[0:64])
            self._data = self._data[64:]

    def digest(self):
        self._data += (b'\x80' +
                       b'\00' * ((56 - (len(self._data) + 1)) % 64) +
                       ((self._size * 8) % (2 ** 64)).to_bytes(8, byteorder='little'))
        self._update(self._data[0:64])
        if len(self._data) > 64:
            self._update(self._data[64:128])
        return (
            self._A.to_bytes(4, byteorder='little') +
            self._B.to_bytes(4, byteorder='little') +
            self._C.to_bytes(4, byteorder='little') +
            self._D.to_bytes(4, byteorder='little')
        )


def F(X: int, Y: int, Z: int):
    return X & Y | ~X & 0xffffffff & Z


def G(X: int, Y: int, Z: int):
    return X & Y | X & Z | Y & Z


def H(X: int, Y: int, Z: int):
    return X ^ Y ^ Z


def rotate(a: int, s: int):
    return (a << s | a >> (32 - s)) & 0xffffffff
