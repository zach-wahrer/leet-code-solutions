import unittest


def can_finish(nums: list) -> bool:
    pass


class TestFinish(unittest.TestCase):

    def test_23114(self):
        self.assertTrue(can_finish([2, 3, 1, 1, 4]))

    def test_32104(self):
        self.assertFalse(can_finish([3, 2, 1, 0, 4]))

    def test_3101(self):
        self.assertTrue(can_finish([3, 1, 0, 1]))

    def test_2101(self):
        self.assertFalse(can_finish([2, 1, 0, 1]))

    def test_000(self):
        self.assertFalse(can_finish([0, 0, 0]))

    def test_111(self):
        self.assertTrue(can_finish([1, 1, 1]))

    def test_1(self):
        self.assertTrue(can_finish([1]))

    def test_0(self):
        self.assertTrue(can_finish([0]))


if __name__ == "__main__":
    unittest.main()
