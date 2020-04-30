"""
Challenge 1a: Algorithm Test - String Compression.

For this problem, I used a simple algorithm that loops through the string,
counting the number of times a char is repeated in sequence. If it is > 1, we
append the character and the count to a compressed string. If a char only
occurs once, simply pass the unmodified character through.

Time complexity: O(n). We iterate over every character in the input string,
hence O(n). _compress_char() is O(1) each time it is called, and therefore
adds no additional big-O time complexity.

"""
import unittest


def compress_string(input_string: str) -> str:
    """Compresses strings."""
    def _compress_char(char: str, amount: int) -> str:
        return char + str(amount) if amount > 1 else char

    if not input_string:
        return ""

    char_to_compress, compression_factor = input_string[0], 1
    compressed_string = ""

    for input_char in input_string[1:]:
        if input_char == char_to_compress:
            compression_factor += 1
        else:
            compressed_string += _compress_char(char_to_compress,
                                                compression_factor)
            char_to_compress = input_char
            compression_factor = 1

    compressed_string += _compress_char(char_to_compress,
                                        compression_factor)

    return compressed_string


class TestStringCompression(unittest.TestCase):
    """Tests for the compress_string() function."""

    def test_compress_bbcceeee(self):
        """Test common compression."""
        input = "bbcceeee"
        output = "b2c2e4"
        self.assertEqual(compress_string(input), output)

    def test_compress_aaabbbcccaaa(self):
        """Test common compression."""
        input = "aaabbbcccaaa"
        output = "a3b3c3a3"
        self.assertEqual(compress_string(input), output)

    def test_compress_single_char(self):
        """Test no compression pass through."""
        input = "a"
        output = "a"
        self.assertEqual(compress_string(input), output)

    def test_no_compression_possible(self):
        """Test no compression pass through with multi-char input."""
        input = "abcd"
        output = "abcd"
        self.assertEqual(compress_string(input), output)

    def test_blank_input(self):
        """Test blank input."""
        input = ""
        output = ""
        self.assertEqual(compress_string(input), output)


if __name__ == "__main__":
    unittest.main()
