class MD4():
    def __init__(self):
        self._A = b'\x01\x23\x45\x67'
        self._B = b'\x89\xab\xcd\xef'
        self._C = b'\xfe\xdc\xba\x98'
        self._D = b'\x76\x54\x32\x10'
        self._current = b''
        self._size = 0

    def _f1(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int):
        return word_rotate(word_add(a, word_add(
            F(b, c, d), self._X[k])),
            s
        )

    def _f2(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int):
        return word_rotate(word_add(a, word_add(
            G(b, c, d), word_add(self._X[k], b'\x99\x79\x82\x5a'))),
            s
        )

    def _f3(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int):
        return word_rotate(word_add(a, word_add(
            H(b, c, d), word_add(self._X[k], b'\xa1\xeb\xd9\x6e'))),
            s
        )

    def _update(self, data: bytes):
        self._X = [data[i:i+4] for i in range(0, 64, 4)]
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

        self._A = word_add(self._A, AA)
        self._B = word_add(self._B, BB)
        self._C = word_add(self._C, CC)
        self._D = word_add(self._D, DD)

    def update(self, data: bytes):
        self._current += data
        self._size += len(data)
        while len(self._current) >= 64:
            self._update(self._current[0:64])
            self._current = self._current[64:]

    def digest(self):
        self._current += (b'\x80' +
                          b'\00' * ((56 - (len(self._current) + 1)) % 64) +
                          ((self._size * 8) % (2 ** 64)).to_bytes(8, byteorder='little'))
        self._update(self._current[0:64])
        if len(self._current) > 64:
            self._update(self._current[64:128])
        return self._A + self._B + self._C + self._D


def F(X: bytes, Y: bytes, Z: bytes):
    return word_or(word_and(X, Y), word_and(word_not(X), Z))


def G(X: bytes, Y: bytes, Z: bytes):
    return word_or(word_or(word_and(X, Y), word_and(X, Z)), word_and(Y, Z))


def H(X: bytes, Y: bytes, Z: bytes):
    return word_xor(word_xor(X, Y), Z)


def word_add(a: bytes, b: bytes):
    return ((int.from_bytes(a, byteorder='little') +
             int.from_bytes(b, byteorder='little')) %
            (2 ** 32)).to_bytes(4, byteorder='little')


def word_and(a: bytes, b: bytes):
    return bytes((a[i] & b[i]) for i in range(4))


def word_or(a: bytes, b: bytes):
    return bytes((a[i] | b[i]) for i in range(4))


def word_xor(a: bytes, b: bytes):
    return bytes((a[i] ^ b[i]) for i in range(4))


def word_not(a: bytes):
    return bytes(~a[i] & 0xff for i in range(4))


def word_rotate(a: bytes, s: int):
    return bytes((a[(i - s // 8) % 4] << s % 8 |
                 a[(i - s // 8 - 1) % 4] >> (8 - s % 8)) & 0xff
                 for i in range(4))
