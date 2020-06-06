import unittest

# O(n**2) time solution - exceeds time limit
def corp_flight_bookings_slow(bookings: list, n: int) -> list:
    flights = [0] * n

    for booking in bookings:
        for i in range(booking[0], booking[1] + 1):
            flights[i - 1] += booking[2]

    return flights


# O(n) time solution
def corp_flight_bookings(bookings: list, n: int) -> list:
    flights = [0] * (n + 1)

    for start_flight, end_flight, quantity in bookings:
        flights[start_flight - 1] += quantity
        flights[end_flight] -= quantity

    for i in range(1, n):
        flights[i] += flights[i - 1]

    return flights[:-1]


class TestFlightBookings(unittest.TestCase):
    def test_5_flights(self):
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        output = [10, 55, 45, 25, 25]
        self.assertEqual(corp_flight_bookings(bookings, 5), output)

    def test_1_flight(self):
        bookings = [[1, 1, 10]]
        output = [10]
        self.assertEqual(corp_flight_bookings(bookings, 1), output)

    def test_null_flights(self):
        bookings = [[1, 2, 0], [2, 3, 0]]
        output = [0, 0, 0]
        self.assertEqual(corp_flight_bookings(bookings, 3), output)


if __name__ == "__main__":
    unittest.main();
