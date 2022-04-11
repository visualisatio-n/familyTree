import unittest

from service.family_addition import add_child, add_husband, add_wife


class TestFamilyAddition(unittest.TestCase):
    def test_add_child_to_existing_female(self):
        res = add_child(person_name='Queen Anga', child_name='Chit', gender='Male')
        self.assertEqual(res, 'CHILD_ADDITION_SUCCEEDED')

    def test_add_child_to_existing_male(self):
        res = add_child(person_name='King Shan', child_name='Chit', gender='Male')
        self.assertEqual(res, 'CHILD_ADDITION_FAILED')

    def test_add_child_to_non_existing_person(self):
        res = add_child(person_name='Kexitin', child_name='Chit', gender='Male')
        self.assertEqual(res, 'PERSON_NOT_FOUND')

    def test_add_husband_to_existing_female(self):
        res = add_husband(person_name='Queen Anga', husband_name='Chit')
        self.assertEqual(res, 'HUSBAND_ADDITION_SUCCEEDED')

    def test_add_husband_to_existing_male(self):
        res = add_husband(person_name='King Shan', husband_name='Chit')
        self.assertEqual(res, 'HUSBAND_ADDITION_FAILED')

    def test_add_husband_to_non_existing_person(self):
        res = add_husband(person_name='Kexitin', husband_name='Chit')
        self.assertEqual(res, 'PERSON_NOT_FOUND')

    def test_add_wife_to_existing_female(self):
        res = add_wife(person_name='Queen Anga', wife_name='Chit')
        self.assertEqual(res, 'WIFE_ADDITION_FAILED')

    def test_add_wife_to_existing_male(self):
        res = add_wife(person_name='King Shan', wife_name='Chit')
        self.assertEqual(res, 'WIFE_ADDITION_SUCCEEDED')

    def test_add_wife_to_non_existing_person(self):
        res = add_wife(person_name='Kexitin', wife_name='Chit')
        self.assertEqual(res, 'PERSON_NOT_FOUND')


if __name__ == '__main__':
    unittest.main()
