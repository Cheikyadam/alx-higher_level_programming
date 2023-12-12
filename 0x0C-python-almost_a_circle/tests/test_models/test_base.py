#!/usr/bin/python3
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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


    def test_to_json_string_r(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)
        with captured_output() as (out, err):
            print(json_dictionary)
        output = out.getvalue()
        self.assertEqual(output, "[{\"x\": 2, \"y\": 8, \"id\": 1, \"height\": 7, \"width\": 10}]\n")
        
        json_dictionary = Base.to_json_string(None)
        self.assertTrue(type(json_dictionary) is str)
        self.assertTrue(json_dictionary == "[]")
    
        json_dictionary = Base.to_json_string([])
        self.assertTrue(type(json_dictionary) is str)
        self.assertTrue(json_dictionary == "[]")

    def test_to_json_string_s(self):
        r1 = Square(10, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary) is str)
        with captured_output() as (out, err):
            print(json_dictionary)
        output = out.getvalue()
        self.assertEqual(output, "[{\"x\": 2, \"y\": 8, \"id\": 1, \"size\": 10}]\n")

        json_dictionary = Base.to_json_string(None)
        self.assertTrue(type(json_dictionary) is str)
        self.assertTrue(json_dictionary == "[]")

        json_dictionary = Base.to_json_string([])
        self.assertTrue(type(json_dictionary) is str)
        self.assertTrue(json_dictionary == "[]")


from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

if __name__ == '__main__':
    unittest.main()
