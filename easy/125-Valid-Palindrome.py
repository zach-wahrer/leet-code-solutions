import unittest


# O(n) Brute
def valid_palindrome_brute(s: str) -> bool:
    # Process String: Remove spaces, punctuation, and to_lower it
    # Reverse string
    # Compare
    processed_string = ""
    for i in s:
        if i.isalnum():
            processed_string += i.lower()
    return processed_string == processed_string[::-1]


# O(n) Two pointer
def valid_palindrome(s: str) -> bool:
    # Start from either end, comparing string
    # To lower each char
    # Skip non-alpha chars and spaces
    if s == "" or len(s) == 1:
        return True
    lp = 0
    rp = len(s) - 1
    while True:
        while not s[lp].isalnum():
            lp += 1
            if lp >= rp:
                return True
        while not s[rp].isalnum():
            rp -= 1
            if lp >= rp:
                return True
        if s[lp].lower() != s[rp].lower():
            return False
        lp += 1
        rp -= 1
        if lp >= rp:
            return True


class TestPalindrome(unittest.TestCase):
    def test_a_man(self):
        input = valid_palindrome("A man, a plan, a canal: Panama")
        self.assertTrue(input)

    def test_radar(self):
        input = valid_palindrome("radar")
        self.assertTrue(input)

    def test_racecar(self):
        input = valid_palindrome("race car")
        self.assertTrue(input)

    def test_race(self):
        input = valid_palindrome("race a car")
        self.assertFalse(input)

    def test_heart(self):
        input = valid_palindrome("I heart sea food")
        self.assertFalse(input)

    def test_0p(self):
        input = valid_palindrome("0P")
        self.assertFalse(input)

    def test_a(self):
        input = valid_palindrome("a")
        self.assertTrue(input)

    def test_empty(self):
        input = valid_palindrome("")
        self.assertTrue(input)

    def test_blank(self):
        input = valid_palindrome(" ")
        self.assertTrue(input)

    def test_period(self):
        input = valid_palindrome(".")
        self.assertTrue(input)

    def test_period_comma(self):
        input = valid_palindrome(".,")
        self.assertTrue(input)


if __name__ == '__main__':
    unittest.main()
