import hashlib
import hmac
import math
import struct


DEFAULT_ROUNDS = 10


class FFX(object):
    def __init__(self, key, rounds=DEFAULT_ROUNDS, digestmod=hashlib.sha1):
        self.key = key
        self.rounds = rounds
        self.digestmod = digestmod
        self.digest_size = self.digestmod().digest_size

    def add(self, radix, a, b):
        return [(a_i + b_i) % radix for a_i, b_i in zip(a, b)]

    def sub(self, radix, a, b):
        return [(a_i - b_i) % radix for a_i, b_i in zip(a, b)]

    def round(self, radix, i, s):
        key = struct.pack('I%sI' % len(s), i, *s)
        chars_per_hash = int(self.digest_size * math.log(256, radix))
        i = 0
        while True:
            h = hmac.new(self.key, key + struct.pack('I', i), self.digestmod)
            d = int(h.hexdigest(), 16)
            for _ in range(chars_per_hash):
                d, r = divmod(d, radix)
                yield r
            key = h.digest()
            i += 1

    def split(self, v):
        s = int(len(v) / 2)
        return v[:s], v[s:]

    def encrypt(self, radix, v):
        a, b = self.split(v)
        for i in range(self.rounds):
            c = self.add(radix, a, self.round(radix, i, b))
            a, b = b, c
        return a + b

    def decrypt(self, radix, v):
        a, b = self.split(v)
        for i in range(self.rounds - 1, -1, -1):
            b, c = a, b
            a = self.sub(radix, c, self.round(radix, i, b))
        return a + b
