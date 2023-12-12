import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_task2(self):
        r1 = Rectangle(10, 2)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_task2_part2(self):
        r1 = Rectangle(7, 5, 2, 3, 89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 5)

    def test_task3(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle("a", 5, 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, "u", 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(6, 5, 'a', 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(9, 5, 4, "o", 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle([3, 4], 5, 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(5, [5, 4], 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(1, 5, [4, 2], 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 5, 4, ["a", "b"], 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle((2, 9), 5, 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, (5, 2), 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(4, 5, (5, 6), 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 5, 4, (5, 0), 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle({'id': 1}, 5, 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(2,{'5': "a"}, 4, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 5, {"a": 2}, 0, 8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(6, 5, 4, {}, 8)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3, 4, 5, 9)

        with self.assertRaises(ValueError):
            r = Rectangle(1, -8, 4, 5, 9)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 4, 5, 9)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 3, 4, 5, 9)

        with self.assertRaises(ValueError):
            r = Rectangle(8, 3, -3, 5, 9)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 3, 4, -5, 9)
    
    def test_area(self):
        r5 = Rectangle(9, 4)
        self.assertEqual(r5.area(), 36)

        r = Rectangle(2, 4, 6, 7, 90)
        self.assertEqual(r.area(), 8)

    def test_display(self):
        my_r = Rectangle(2, 1)
        with captured_output() as (out, err):
            my_r.display()
        output = out.getvalue().strip()
        self.assertEqual(output, '##')

    def test_display_next(self):
        my_r = Rectangle(3, 2)
        with captured_output() as (out, err):
            my_r.display()
        output = out.getvalue()
        self.assertEqual(output, '###\n###\n')

    def test_display2(self):
        my_r = Rectangle(3, 4, 2, 0)
        with captured_output() as (out, err):
            my_r.display()
        output = out.getvalue()
        self.assertEqual(output, "  ###\n  ###\n  ###\n  ###\n")

    def test_display3(self):
        my_r = Rectangle(3, 4, 2, 2)
        with captured_output() as (out, err):
            my_r.display()
        output = out.getvalue()
        self.assertEqual(output, "\n\n  ###\n  ###\n  ###\n  ###\n")

    def test_str(self):
        my_r = Rectangle(3, 4, 2, 2, 0)
        with captured_output() as (out, err):
            print(my_r)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (0) 2/2 - 3/4\n")

    def test_str2(self):
        my_r = Rectangle(3, 4)
        with captured_output() as (out, err):
            print(my_r)
        output = out.getvalue()
        self.assertEqual(output, "[Rectangle] (9) 0/0 - 3/4\n")

    def test_update(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(rec.id, 89)
        rec.update(89, 2)
        self.assertEqual(rec.width, 2)
        rec.update(89, 2, 5)
        self.assertEqual(rec.height, 5)
        rec.update(89, 2, 5, 19)
        self.assertEqual(rec.x, 19)
        rec.update(89, 2, 5, 19, 43)
        self.assertEqual(rec.y, 43)

    def test_update2(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height = 1)
        self.assertEqual(rec.height, 1)
        rec.update(width = 1, x = 2)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.x, 2)
        rec.update(y=1, width=2, x=3, id=89)
        self.assertEqual(rec.y, 1)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.id, 89)


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
