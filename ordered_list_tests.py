import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_add(self):
        o = OrderedList()
        o.add(1)
        self.assertEqual(o.size(), 1)
        self.assertEqual(o.python_list(), [1])
        o.add(2)
        self.assertEqual(o.size(), 2)
        self.assertEqual(o.python_list(), [1, 2])
        # repeat, should change nothing
        o.add(2)
        self.assertEqual(o.size(), 2)
        self.assertEqual(o.python_list(), [1, 2])
        # non repeat, should add rest
        o.add(3)
        self.assertEqual(o.size(), 3)
        self.assertEqual(o.python_list(), [1, 2, 3])
        o.add(4)
        self.assertEqual(o.size(), 4)
        self.assertEqual(o.python_list(), [1, 2, 3, 4])
        # in place, should add to end
        o.add(6)
        self.assertEqual(o.size(), 5)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 6])
        # out of place, should add to middle
        o.add(5)
        self.assertEqual(o.size(), 6)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 5, 6])
        # out of place, should add to beg
        o.add(0.5)
        self.assertEqual(o.size(), 7)
        self.assertEqual(o.python_list(), [0.5, 1, 2, 3, 4, 5, 6])
        # negative num
        o.add(-1)
        self.assertEqual(o.size(), 8)
        self.assertEqual(o.python_list(), [-1, 0.5, 1, 2, 3, 4, 5, 6])

    def test_remove(self):
        o = OrderedList()
        o.add(1)
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        o.add(6)
        self.assertEqual(o.size(), 6)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 5, 6])
        # remove last
        o.remove(6)
        self.assertEqual(o.size(), 5)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 5])
        # remove middle
        o.remove(3)
        self.assertEqual(o.size(), 4)
        self.assertEqual(o.python_list(), [1, 2, 4, 5])
        # remove first
        o.remove(1)
        self.assertEqual(o.size(), 3)
        self.assertEqual(o.python_list(), [2, 4, 5])
        # remove non-existent
        o.remove(1000)
        self.assertEqual(o.size(), 3)
        self.assertEqual(o.python_list(), [2, 4, 5])

    def test_index(self):
        o = OrderedList()
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        o.add(6)
        self.assertEqual(o.python_list(), [2, 3, 4, 5, 6])
        # first num
        self.assertEqual(o.index(2), 0)
        # middle num
        self.assertEqual(o.index(4), 2)
        # last num
        self.assertEqual(o.index(6), 4)
        # non existent
        self.assertEqual(o.index(1), None)

    def test_pop(self):
        o = OrderedList()
        o.add(1)
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 5])
        # beginning
        self.assertEqual(o.pop(0), 1)
        self.assertEqual(o.python_list(), [2, 3, 4, 5])
        # mid
        self.assertEqual(o.pop(2), 4)
        self.assertEqual(o.python_list(), [2, 3, 5])
        # end
        self.assertEqual(o.pop(2), 5)
        self.assertEqual(o.python_list(), [2, 3])
        # non existent
        try:
            o.pop(5)
        except IndexError:
            print("pass1")
        # negative
        try:
            o.pop(-1)
        except IndexError:
            print("pass2")

    def test_search(self):
        o = OrderedList()
        o.add(1)
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        o.add(6)
        o.add(7)
        o.add(8)
        o.add(9)
        o.add(10)
        # first
        self.assertTrue(o.search(1))
        # mid
        self.assertTrue(o.search(5))
        # end
        self.assertTrue(o.search(10))
        # non-existent
        self.assertFalse(o.search(11))

    def test_python_list(self):
        o = OrderedList()
        o.add(1)
        self.assertEqual(o.python_list(), [1])
        o.add(2)
        self.assertEqual(o.python_list(), [1, 2])
        o.add(3)
        self.assertEqual(o.python_list(), [1, 2, 3])
        o.add(4)
        self.assertEqual(o.python_list(), [1, 2, 3, 4])
        o.add(5)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 5])

    def test_python_list_reversed(self):
        o = OrderedList()
        o.add(1)
        o.add(2)
        o.add(3)
        o.add(4)
        o.add(5)
        # order
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 5])
        self.assertEqual(o.python_list_reversed(), [5, 4, 3, 2, 1])
        # out of order
        o.add(4.5)
        self.assertEqual(o.python_list(), [1, 2, 3, 4, 4.5, 5])
        self.assertEqual(o.python_list_reversed(), [5, 4.5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
