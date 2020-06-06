import unittest


def corpFlightBookings(bookings: list, n: int) -> list:
    pass


class TestFlightBookings(unittest.TestCase):
    def test_5_flights(self):
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        output = [10, 55, 45, 25, 25]
        self.assertEqual(corpFlightBookings(bookings, 5), output)


if __name__ == "__main__":
    unittest.main();
