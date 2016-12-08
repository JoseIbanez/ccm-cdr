import unittest
import cdr

class TestCdrMethods(unittest.TestCase):

    @unittest.skip("demo version")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_time_to_string(self):
        self.assertEqual(cdr.time_to_string("1447409455"), '2015-11-13 10:10:55')

    def test_int_to_ip(self):
        self.assertEqual(cdr.int_to_ip("51388076"), '172.30.16.3')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper(),"oooh :(")
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
