#!/usr/bin/env python3
"""
Test suite for the utils module, specifically testing the
access_nested_map function.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
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

        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')  # Mock requests.get in the utils module
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected result.
        """
        # Set up the mock response
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function to test
        result = get_json(test_url)

        # Assert the mock get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert the result is the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize function.
    """

    def test_memoize(self):
        """
        Test that memoization works: a_method is only called once,
        even when a_property is called multiple times.
        """
        # Define the TestClass with memoize decorator
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_class = TestClass()

        # Patch the a_method function inside TestClass
        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_a_method:
            # Call a_property twice
            first_result = test_class.a_property
            second_result = test_class.a_property

            # Verify a_method was called only once
            mock_a_method.assert_called_once()

            # Check that both calls to a_property return the same result
            self.assertEqual(first_result, second_result)


if __name__ == "__main__":
    unittest.main()
