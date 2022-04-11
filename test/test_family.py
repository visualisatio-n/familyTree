import unittest

from model.family import family_tree
from model.female import Female
from model.male import Male


class TestFamilyTree(unittest.TestCase):
    def test_King_Shan_in_family_tree(self):
        self.assertEqual(True, 'King Shan' in family_tree)
        self.assertEqual(True, isinstance(family_tree['King Shan'], Male))

    def test_Queen_Anga_in_family_tree(self):
        self.assertEqual(True, 'Queen Anga' in family_tree)
        self.assertEqual(True, isinstance(family_tree['Queen Anga'], Female))


if __name__ == '__main__':
    unittest.main()
