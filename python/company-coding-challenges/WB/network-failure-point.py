"""
Challenge 1b: Algorithm Test - Network Failure Point.

Time complexity: O(n). We iterate over all the connection pairs once for
counting connections, hence O(n). Later, we also iterate over all the counts,
but since this isn't nested, it doesn't add any additional big-O time
complexity.

"""
import unittest


def indentify_router(graph: list) -> int:
    """Identify router within network with most combined connetions."""
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for outgoing, incoming in graph:
        counts[outgoing] += 1
        counts[incoming] += 1

    nodes_with_most_connections = []
    most_connections = max(counts.values())
    for node in counts:
        if counts[node] == most_connections and most_connections != 0:
            nodes_with_most_connections.append(node)

    return nodes_with_most_connections


class TestMostConnections(unittest.TestCase):
    """Tests for the indentify_router() function."""

    def test_small(self):
        """Small input with a single result."""
        graph = [
            [1, 2],
            [2, 3],
            [3, 5],
            [5, 2],
            [2, 1]
        ]
        self.assertEqual(indentify_router(graph), [2])

    def test_large(self):
        """Larger input with single result."""
        graph = [
            [1, 3],
            [3, 5],
            [5, 6],
            [6, 4],
            [4, 5],
            [5, 2],
            [2, 6]
        ]
        self.assertEqual(indentify_router(graph), [5])

    def test_small_with_tie(self):
        """Small input with a tie."""
        graph = [
            [2, 4],
            [4, 6],
            [6, 2],
            [2, 5],
            [5, 6]
        ]
        self.assertEqual(indentify_router(graph), [2, 6])

    def test_single_input(self):
        """Single input test."""
        graph = [[1, 1]]
        self.assertEqual(indentify_router(graph), [1])

    def test_blank_input(self):
        """Blank input test."""
        graph = []
        self.assertEqual(indentify_router(graph), [])


if __name__ == "__main__":
    unittest.main()
