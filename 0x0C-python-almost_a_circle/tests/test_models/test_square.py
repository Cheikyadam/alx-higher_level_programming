import unittest
import sys
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle

class TestSquare(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_inheritance(self):
        s = Square(2, 3)
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_str(self):
        s = Square(2)
        with captured_output() as (out, err):
            print(s)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (13) 0/0 - 2\n")

        s = Square(2, 3, 4, 5)
        with captured_output() as (out, err):
            print(s)
        output = out.getvalue()
        self.assertEqual(output, "[Square] (5) 3/4 - 2\n")

    def test_init(self):
        s = Square(2, 7, 9, 8)
        self.assertEqual(s.id, 8)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 9)

        s = Square(10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_setter_getter(self):
        s = Square(9, 8, 3, 89)
        s.size = 10
        self.assertEqual(s.size, 10)

        with self.assertRaises(TypeError):
            s.size = [0, 9]

        with self.assertRaises(TypeError):
            s.size = {}

        with self.assertRaises(TypeError):
            s.size = "Bonjour"

        with self.assertRaises(TypeError):
            s.size = (2, 5)

        with self.assertRaises(ValueError):
            s.size = -5

        with self.assertRaises(ValueError):
            s.size = 0

        
    def test_update(self):
        rec = Square(10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(rec.id, 89)
        rec.update(89, 2)
        self.assertEqual(rec.size, 2)
        rec.update(89, 2, 5)
        self.assertEqual(rec.x, 5)
        rec.update(89, 2, 5, 19)
        self.assertEqual(rec.y, 19)

    def test_update2(self):
        rec = Square(10, 10, 10, 10)
        rec.update(size = 1)
        self.assertEqual(rec.size, 1)
        rec.update(size = 1, x = 2)
        self.assertEqual(rec.size, 1)
        self.assertEqual(rec.x, 2)
        rec.update(y=1, size=2, x=3, id=89)
        self.assertEqual(rec.y, 1)
        self.assertEqual(rec.size, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.id, 89)

    def test_to_dic(self):
        rec = Square(10, 1, 9, 0)
        rec_d = rec.to_dictionary()
        self.assertTrue(type(rec_d is dict))
        with captured_output() as (out, err):
            print(rec_d)
        output = out.getvalue()
        self.assertEqual(output, "{'x': 1, 'y': 9, 'id': 0, 'size': 10}\n")


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
