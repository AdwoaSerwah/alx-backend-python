#!/usr/bin/env python3
"""
Test suite for the GithubOrgClient class.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
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
        mock_response = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, mock_response)

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_public_repos_url(self, org_name):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL
        based on the mocked org method.
        """
        mock_payload = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }

        # Patch the get_json method that org relies on
        with patch('client.get_json', return_value=mock_payload):
            client = GithubOrgClient(org_name)
            result = client._public_repos_url  # Access the property
            expected_url = mock_payload["repos_url"]
            self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()
