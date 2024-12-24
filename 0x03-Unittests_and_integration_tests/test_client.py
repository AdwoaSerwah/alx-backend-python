#!/usr/bin/env python3
"""
Test suite for the GithubOrgClient class.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """

        # Mock response for the org method
        mock_response = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }

        # Set the mock response for the get_json function
        mock_get_json.return_value = mock_response

        # Create the client instance
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Check that the get_json method was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        # Assert that the result matches the mock response
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
