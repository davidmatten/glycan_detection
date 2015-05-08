import unittest
from glycan import get_glycan_sites 

class TestGlycanDetector(unittest.TestCase):

    def test_pattern(self):
        seq = "NGT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0])

if __name__ == '__main__':
    unittest.main()
