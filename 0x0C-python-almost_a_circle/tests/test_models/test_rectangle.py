import unittest
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

if __name__ == '__main__':
    unittest.main()
