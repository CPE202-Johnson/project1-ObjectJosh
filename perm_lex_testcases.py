import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        # test: two characters
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

        # test: empty string
        self.assertEqual(perm_lex.perm_gen_lex(''),[])

        # test: normal case (three characters)
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

        # test: one character
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])

        # test: normal case (four characters -> numbers)
        self.assertEqual(perm_lex.perm_gen_lex('1234'),['1234', '1243', '1324', '1342', '1423', '1432', '2134', '2143', '2314', '2341', '2413', '2431', '3124', '3142', '3214', '3241', '3412', '3421', '4123', '4132', '4213', '4231', '4312', '4321'])

if __name__ == "__main__":
    unittest.main()
