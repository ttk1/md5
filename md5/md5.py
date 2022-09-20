from math import sin, floor


class MD5():
    def __init__(self):
        self._T = [floor((2 ** 32) * abs(sin(i))).to_bytes(4, byteorder='little')
                   for i in range(65)]
        self._A = b'\x01\x23\x45\x67'
        self._B = b'\x89\xab\xcd\xef'
        self._C = b'\xfe\xdc\xba\x98'
        self._D = b'\x76\x54\x32\x10'
        self._current = b''
        self._size = 0

    def _f1(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
        return word_add(b, word_rotate(
            word_add(a, word_add(
                F(b, c, d), word_add(self._X[k], self._T[i]))),
            s
        ))

    def _f2(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
        return word_add(b, word_rotate(
            word_add(a, word_add(
                G(b, c, d), word_add(self._X[k], self._T[i]))),
            s
        ))

    def _f3(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
        return word_add(b, word_rotate(
            word_add(a, word_add(
                H(b, c, d), word_add(self._X[k], self._T[i]))),
            s
        ))

    def _f4(self, a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
        return word_add(b, word_rotate(
            word_add(a, word_add(
                I(b, c, d), word_add(self._X[k], self._T[i]))),
            s
        ))

    def _update(self, data: bytes):
        self._X = [data[i:i+4] for i in range(0, 64, 4)]
        AA = self._A
        BB = self._B
        CC = self._C
        DD = self._D

        # Round 1.
        self._A = self._f1(self._A, self._B, self._C, self._D, 0, 7, 1)
        self._D = self._f1(self._D, self._A, self._B, self._C, 1, 12, 2)
        self._C = self._f1(self._C, self._D, self._A, self._B, 2, 17, 3)
        self._B = self._f1(self._B, self._C, self._D, self._A, 3, 22, 4)
        self._A = self._f1(self._A, self._B, self._C, self._D, 4, 7, 5)
        self._D = self._f1(self._D, self._A, self._B, self._C, 5, 12, 6)
        self._C = self._f1(self._C, self._D, self._A, self._B, 6, 17, 7)
        self._B = self._f1(self._B, self._C, self._D, self._A, 7, 22, 8)
        self._A = self._f1(self._A, self._B, self._C, self._D, 8, 7, 9)
        self._D = self._f1(self._D, self._A, self._B, self._C, 9, 12, 10)
        self._C = self._f1(self._C, self._D, self._A, self._B, 10, 17, 11)
        self._B = self._f1(self._B, self._C, self._D, self._A, 11, 22, 12)
        self._A = self._f1(self._A, self._B, self._C, self._D, 12, 7, 13)
        self._D = self._f1(self._D, self._A, self._B, self._C, 13, 12, 14)
        self._C = self._f1(self._C, self._D, self._A, self._B, 14, 17, 15)
        self._B = self._f1(self._B, self._C, self._D, self._A, 15, 22, 16)

        # Round 2.
        self._A = self._f2(self._A, self._B, self._C, self._D, 1, 5, 17)
        self._D = self._f2(self._D, self._A, self._B, self._C, 6, 9, 18)
        self._C = self._f2(self._C, self._D, self._A, self._B, 11, 14, 19)
        self._B = self._f2(self._B, self._C, self._D, self._A, 0, 20, 20)
        self._A = self._f2(self._A, self._B, self._C, self._D, 5, 5, 21)
        self._D = self._f2(self._D, self._A, self._B, self._C, 10, 9, 22)
        self._C = self._f2(self._C, self._D, self._A, self._B, 15, 14, 23)
        self._B = self._f2(self._B, self._C, self._D, self._A, 4, 20, 24)
        self._A = self._f2(self._A, self._B, self._C, self._D, 9, 5, 25)
        self._D = self._f2(self._D, self._A, self._B, self._C, 14, 9, 26)
        self._C = self._f2(self._C, self._D, self._A, self._B, 3, 14, 27)
        self._B = self._f2(self._B, self._C, self._D, self._A, 8, 20, 28)
        self._A = self._f2(self._A, self._B, self._C, self._D, 13, 5, 29)
        self._D = self._f2(self._D, self._A, self._B, self._C, 2, 9, 30)
        self._C = self._f2(self._C, self._D, self._A, self._B, 7, 14, 31)
        self._B = self._f2(self._B, self._C, self._D, self._A, 12, 20, 32)

        # Round 3.
        self._A = self._f3(self._A, self._B, self._C, self._D, 5, 4, 33)
        self._D = self._f3(self._D, self._A, self._B, self._C, 8, 11, 34)
        self._C = self._f3(self._C, self._D, self._A, self._B, 11, 16, 35)
        self._B = self._f3(self._B, self._C, self._D, self._A, 14, 23, 36)
        self._A = self._f3(self._A, self._B, self._C, self._D, 1, 4, 37)
        self._D = self._f3(self._D, self._A, self._B, self._C, 4, 11, 38)
        self._C = self._f3(self._C, self._D, self._A, self._B, 7, 16, 39)
        self._B = self._f3(self._B, self._C, self._D, self._A, 10, 23, 40)
        self._A = self._f3(self._A, self._B, self._C, self._D, 13, 4, 41)
        self._D = self._f3(self._D, self._A, self._B, self._C, 0, 11, 42)
        self._C = self._f3(self._C, self._D, self._A, self._B, 3, 16, 43)
        self._B = self._f3(self._B, self._C, self._D, self._A, 6, 23, 44)
        self._A = self._f3(self._A, self._B, self._C, self._D, 9, 4, 45)
        self._D = self._f3(self._D, self._A, self._B, self._C, 12, 11, 46)
        self._C = self._f3(self._C, self._D, self._A, self._B, 15, 16, 47)
        self._B = self._f3(self._B, self._C, self._D, self._A, 2, 23, 48)

        # Round 4.
        self._A = self._f4(self._A, self._B, self._C, self._D, 0, 6, 49)
        self._D = self._f4(self._D, self._A, self._B, self._C, 7, 10, 50)
        self._C = self._f4(self._C, self._D, self._A, self._B, 14, 15, 51)
        self._B = self._f4(self._B, self._C, self._D, self._A, 5, 21, 52)
        self._A = self._f4(self._A, self._B, self._C, self._D, 12, 6, 53)
        self._D = self._f4(self._D, self._A, self._B, self._C, 3, 10, 54)
        self._C = self._f4(self._C, self._D, self._A, self._B, 10, 15, 55)
        self._B = self._f4(self._B, self._C, self._D, self._A, 1, 21, 56)
        self._A = self._f4(self._A, self._B, self._C, self._D, 8, 6, 57)
        self._D = self._f4(self._D, self._A, self._B, self._C, 15, 10, 58)
        self._C = self._f4(self._C, self._D, self._A, self._B, 6, 15, 59)
        self._B = self._f4(self._B, self._C, self._D, self._A, 13, 21, 60)
        self._A = self._f4(self._A, self._B, self._C, self._D, 4, 6, 61)
        self._D = self._f4(self._D, self._A, self._B, self._C, 11, 10, 62)
        self._C = self._f4(self._C, self._D, self._A, self._B, 2, 15, 63)
        self._B = self._f4(self._B, self._C, self._D, self._A, 9, 21, 64)

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


def digest(message: bytes) -> bytes:
    '''
    メッセージの MD5 ダイジェストを計算する。

    Parameters
    ----------
    message: bytes
        メッセージ

    Returns
    -------
    message_digest: bytes
        計算された MD5 ダイジェスト
    '''

    m = (message +
         # Step 1. Append Padding Bits
         b'\x80' + b'\00' * ((56 - (len(message) + 1) % 64) % 64) +
         # Step 2. Append Length
         ((len(message) * 8) % (2 ** 64)).to_bytes(8, byteorder='little'))

    # Step 3. Initialize MD Buffer
    A = b'\x01\x23\x45\x67'
    B = b'\x89\xab\xcd\xef'
    C = b'\xfe\xdc\xba\x98'
    D = b'\x76\x54\x32\x10'

    # Step 4. Process Message in 16-Word Blocks
    M = [m[i:i+4] for i in range(0, len(m), 4)]
    T = [floor((2 ** 32) * abs(sin(i))).to_bytes(4, byteorder='little')
         for i in range(65)]
    for i in range(len(M) // 16):
        X = M[i*16:i*16+16]
        AA = A
        BB = B
        CC = C
        DD = D

        # Round 1.
        def f1(a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
            return word_add(b, word_rotate(
                word_add(a, word_add(F(b, c, d), word_add(X[k], T[i]))),
                s
            ))
        A = f1(A, B, C, D, 0, 7, 1)
        D = f1(D, A, B, C, 1, 12, 2)
        C = f1(C, D, A, B, 2, 17, 3)
        B = f1(B, C, D, A, 3, 22, 4)
        A = f1(A, B, C, D, 4, 7, 5)
        D = f1(D, A, B, C, 5, 12, 6)
        C = f1(C, D, A, B, 6, 17, 7)
        B = f1(B, C, D, A, 7, 22, 8)
        A = f1(A, B, C, D, 8, 7, 9)
        D = f1(D, A, B, C, 9, 12, 10)
        C = f1(C, D, A, B, 10, 17, 11)
        B = f1(B, C, D, A, 11, 22, 12)
        A = f1(A, B, C, D, 12, 7, 13)
        D = f1(D, A, B, C, 13, 12, 14)
        C = f1(C, D, A, B, 14, 17, 15)
        B = f1(B, C, D, A, 15, 22, 16)

        # Round 2.
        def f2(a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
            return word_add(b, word_rotate(
                word_add(a, word_add(G(b, c, d), word_add(X[k], T[i]))),
                s
            ))
        A = f2(A, B, C, D, 1, 5, 17)
        D = f2(D, A, B, C, 6, 9, 18)
        C = f2(C, D, A, B, 11, 14, 19)
        B = f2(B, C, D, A, 0, 20, 20)
        A = f2(A, B, C, D, 5, 5, 21)
        D = f2(D, A, B, C, 10, 9, 22)
        C = f2(C, D, A, B, 15, 14, 23)
        B = f2(B, C, D, A, 4, 20, 24)
        A = f2(A, B, C, D, 9, 5, 25)
        D = f2(D, A, B, C, 14, 9, 26)
        C = f2(C, D, A, B, 3, 14, 27)
        B = f2(B, C, D, A, 8, 20, 28)
        A = f2(A, B, C, D, 13, 5, 29)
        D = f2(D, A, B, C, 2, 9, 30)
        C = f2(C, D, A, B, 7, 14, 31)
        B = f2(B, C, D, A, 12, 20, 32)

        # Round 3.
        def f3(a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
            return word_add(b, word_rotate(
                word_add(a, word_add(H(b, c, d), word_add(X[k], T[i]))),
                s
            ))
        A = f3(A, B, C, D, 5, 4, 33)
        D = f3(D, A, B, C, 8, 11, 34)
        C = f3(C, D, A, B, 11, 16, 35)
        B = f3(B, C, D, A, 14, 23, 36)
        A = f3(A, B, C, D, 1, 4, 37)
        D = f3(D, A, B, C, 4, 11, 38)
        C = f3(C, D, A, B, 7, 16, 39)
        B = f3(B, C, D, A, 10, 23, 40)
        A = f3(A, B, C, D, 13, 4, 41)
        D = f3(D, A, B, C, 0, 11, 42)
        C = f3(C, D, A, B, 3, 16, 43)
        B = f3(B, C, D, A, 6, 23, 44)
        A = f3(A, B, C, D, 9, 4, 45)
        D = f3(D, A, B, C, 12, 11, 46)
        C = f3(C, D, A, B, 15, 16, 47)
        B = f3(B, C, D, A, 2, 23, 48)

        # Round 4.
        def f4(a: bytes, b: bytes, c: bytes, d: bytes, k: int, s: int, i: int):
            return word_add(b, word_rotate(
                word_add(a, word_add(I(b, c, d), word_add(X[k], T[i]))),
                s
            ))
        A = f4(A, B, C, D, 0, 6, 49)
        D = f4(D, A, B, C, 7, 10, 50)
        C = f4(C, D, A, B, 14, 15, 51)
        B = f4(B, C, D, A, 5, 21, 52)
        A = f4(A, B, C, D, 12, 6, 53)
        D = f4(D, A, B, C, 3, 10, 54)
        C = f4(C, D, A, B, 10, 15, 55)
        B = f4(B, C, D, A, 1, 21, 56)
        A = f4(A, B, C, D, 8, 6, 57)
        D = f4(D, A, B, C, 15, 10, 58)
        C = f4(C, D, A, B, 6, 15, 59)
        B = f4(B, C, D, A, 13, 21, 60)
        A = f4(A, B, C, D, 4, 6, 61)
        D = f4(D, A, B, C, 11, 10, 62)
        C = f4(C, D, A, B, 2, 15, 63)
        B = f4(B, C, D, A, 9, 21, 64)

        A = word_add(A, AA)
        B = word_add(B, BB)
        C = word_add(C, CC)
        D = word_add(D, DD)

    # Step 5. Output
    return A + B + C + D


def F(X: bytes, Y: bytes, Z: bytes):
    return word_or(word_and(X, Y), word_and(word_not(X), Z))


def G(X: bytes, Y: bytes, Z: bytes):
    return word_or(word_and(X, Z), word_and(Y, word_not(Z)))


def H(X: bytes, Y: bytes, Z: bytes):
    return word_xor(word_xor(X, Y), Z)


def I(X: bytes, Y: bytes, Z: bytes):
    return word_xor(Y, word_or(X, word_not(Z)))


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
