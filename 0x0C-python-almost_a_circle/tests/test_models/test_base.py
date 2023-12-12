#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)
        
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

        b4 =Base()
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()
