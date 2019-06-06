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

    def test_EMDash(self):
        s = "It was the best\u2014and worst\u2014of times."
        result = AsciiNormalizer.to_ascii(s)
        self.assertEqual("It was the best--and worst--of times.", result)

    def test_DoubleQuotes(self):
        s = "He blinked. \u201cIt is nothing,\u201d he said."
        result = AsciiNormalizer.to_ascii(s)
        self.assertEqual('He blinked. "It is nothing," he said.', result)

if __name__ == '__main__':
    unittest.main()

