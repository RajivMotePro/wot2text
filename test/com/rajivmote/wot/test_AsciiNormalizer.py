import unittest
from com.rajivmote.wot.AsciiNormalizer import AsciiNormalizer

class TestAsciiNormalizer(unittest.TestCase):
    def setUp(self):
        self.func = AsciiNormalizer()

    def test_SingleQuote(self):
        s = 'Tel\u2019aran\u2019rhiod'
        result = AsciiNormalizer.to_ascii(s)
        self.assertEqual("Tel'aran'rhiod", result)

    def test_Elipses(self):
        s = 'Something.\xa0.\xa0.\xa0 Strange'
        result = AsciiNormalizer.to_ascii(s)
        self.assertEqual("Something... Strange", result)

if __name__ == '__main__':
    unittest.main()

