import unittest

from pyffx import String, Integer


class StringTests(unittest.TestCase):
    def test_encrypt(self):
        s = String(b"foo", "abc", length=3)
        self.assertRaises(ValueError, s.encrypt, "abx")
        self.assertEqual(s.encrypt("cba"), "abb")
        self.assertEqual(s.decrypt(s.encrypt("ccc")), "ccc")


class IntegerTests(unittest.TestCase):
    def test_encrypt(self):
        d = Integer(b"foo", length=2)
        for i in range(100):
            self.assertEqual(d.decrypt(d.encrypt(i)), i)
        hist = set()
        for i in range(100):
            hist.add(d.encrypt(i))
        self.assertEqual(hist, set(range(100)))

    def test_encrypt_big_number(self):
        d = Integer(b"foo", length=20)
        self.assertEqual(d.decrypt(d.encrypt(1)), 1)

    def test_cypher_text_with_leading_zero(self):
        d = Integer(b"foo", 2)
        n = 11
        encrypted = d.encrypt(n)
        self.assertTrue(len(str(encrypted)), 1)
        self.assertTrue(d.decrypt(encrypted), n)
