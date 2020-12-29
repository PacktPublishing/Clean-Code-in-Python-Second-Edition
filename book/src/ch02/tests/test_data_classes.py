import unittest

from data_classes import RTrieNode


class TestRTrieNode(unittest.TestCase):
    def test_next_nodes_differ(self):
        node1 = RTrieNode(1)
        node2 = RTrieNode(1)

        self.assertIsNot(node1.next_, node2.next_)

        node1.next_[:2] = [2, 3]
        self.assertTrue(all(n is None for n in node2.next_))
        self.assertEqual(node1.next_, [2, 3, *(None for _ in range(RTrieNode.size - 2))])

    def test_invalid_next(self):
        with self.assertRaises(ValueError):
            RTrieNode(1, [1, 2, 3])

    def test_valid_next_provided(self):
        next_array = list(range(RTrieNode.size))
        node = RTrieNode(0, next_array)
        self.assertListEqual(node.next_, next_array)


if __name__ == "__main__":
    unittest.main()
