import abc
import string
import six

from pyffx.ffx import FFX


@six.add_metaclass(abc.ABCMeta)
class Codec(object):
    def __init__(self, ffx, radix):
        self.ffx = ffx if hasattr(ffx, 'encrypt') else FFX(ffx)
        self.radix = radix

    def encrypt(self, v):
        return self.unpack(self.ffx.encrypt(self.radix, self.pack(v)), type(v))

    def decrypt(self, v):
        return self.unpack(self.ffx.decrypt(self.radix, self.pack(v)), type(v))

    @abc.abstractmethod
    def pack(self, v):
        raise NotImplementedError()

    @abc.abstractmethod
    def unpack(self, v, t):
        raise NotImplementedError()


class Sequence(Codec):
    def __init__(self, ffx, alphabet, length=None, **kwargs):
        self.alphabet = alphabet
        self.pack_map = {c: i for i, c in enumerate(alphabet)}
        self.length = length
        super(Sequence, self).__init__(ffx, radix=len(alphabet), **kwargs)

    def pack(self, v):
        padlen = self.length - len(v) if self.length else 0
        if padlen < 0:
            raise ValueError('too long')
        try:
            return [0] * padlen + [self.pack_map[c] for c in v]
        except KeyError as e:
            raise ValueError('non-alphabet character: %s' % e)

    def unpack(self, v, t):
        return t(self.alphabet[i] for i in v)


class String(Sequence):
    def unpack(self, v, t):
        return ''.join(super(String, self).unpack(v, list))


class Integer(String):
    def __init__(self, ffx, **kwargs):
        super(Integer, self).__init__(ffx, string.digits, **kwargs)

    def pack(self, v):
        return super(Integer, self).pack(str(v))

    def unpack(self, v, t):
        return int(super(Integer, self).unpack(v, t))
