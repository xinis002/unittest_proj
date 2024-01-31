import unittest


from utils import arrs


class TestGet(unittest.TestCase):

    def test_get_valid_index(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)

    def test_get_index_out_of_bounds(self):
        self.assertEqual(arrs.get([1, 2, 3], 5, "test"), "test")

    def test_get_negative_index(self):
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")

    def test_get_empty_array(self):
        self.assertEqual(arrs.get([], 0, "empty"), "empty")


class TestMySlice(unittest.TestCase):

    def test_slice_normal(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])

    def test_slice_with_start_and_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, -1), [2, 3])

    def test_slice_with_start_only(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 2), [3, 4])

    def test_slice_negative_indices(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, -1), [2, 3])

    def test_slice_out_of_bounds_indices(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 5, 10), [])

    def test_slice_empty_array(self):
        self.assertEqual(arrs.my_slice([], 1, 3), [])

    def test_slice_negative_start(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2), [3, 4])

    def test_slice_negative_start_and_end(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, -1), [2, 3])





