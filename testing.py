import unittest
from glycan import get_glycan_sites 

class TestGlycanDetector(unittest.TestCase):

    def test_base_pattern(self):
        seq = "NGT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0])
        
    def test_one_gap_firstPos(self):
        seq = "N-GT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0])

    def test_one_gap_secondPos(self):
        seq = "NG-T"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0])

    def test_gaps_everywhere(self):
        seq = "-N-G-T-"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0])

    def test_null_string(self):
        seq = ""
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [])

    def test_only_gaps(self):
        seq = "------"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [])

    def test_double_middle_char(self):
        seq = "NGGT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [])

    def test_P_in_middle(self):
        seq = "NPT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [])

    def test_double_start_N(self):
        seq = "NNGT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [1])

    def test_double_ending_T(self):
        seq = "NGTT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0])

    def test_two_patterns(self):
        seq = "NGTTNGT"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0, 4])

    def test_gaps_and_double_T_and_two_patterns(self):
        seq = "N-G-T-T-N-G-T"
        sites = get_glycan_sites(seq)
        self.assertEqual(sites, [0, 4])


if __name__ == '__main__':
    unittest.main()
