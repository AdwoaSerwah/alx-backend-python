#!/usr/bin/env python3
"""
Test suite for the utils module, specifically testing the
access_nested_map function.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Ensure this import is correct


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test simple key-value access
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test nested dictionary
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Test deep nested dictionary
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        # Compare the exception message with the expected key directly
        self.assertEqual(cm.exception.args[0], path[-1])


if __name__ == "__main__":
    unittest.main()
