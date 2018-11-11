import unittest
import os

def analzyetext(filename):
    lines = 0
    chars = 0
    with open(filename,'r') as f:
        for line in f:
            lines +=1
            chars +=len(line)
        return lines, chars
class TextAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        with open(self.filename,'w') as f:
            f.write('dfadsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')

    def test_function_runs(self):
        analzyetext(self.filename)

    def testlinecount(self):
        self.assertEqual(analzyetext(self.filename)[0], 1)

    def testcharacetrocount(self):
        self.assertEqual(analzyetext(self.filename)[1], 70)

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

if __name__ == '__main__':
    unittest.main()

