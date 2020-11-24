import unittest
import bitbucket_api
import os

# Set bitbucket credentials to test methods that require authenticated user
os.environ['BITBUCKET_USER'] = 'ENTER YOUR BITBUCKET USERNAME HERE'
os.environ['BITBUCKET_PW'] = 'ENTER YOUR BITBUCKET PASSWORD HERE'


class TestBitbucketAPI(unittest.TestCase):
    """ Class containing all the methods necessary for testing the bitbucket api """

    def test_ask_user_input(self):
        """Verify whether the ask_user_input function returns a tuple of the user's credentials"""

        self.assertEqual(bitbucket_api.ask_user_input(
            'test_user', 'test_pass'), ('test_user', 'test_pass'))
        self.assertEqual(bitbucket_api.ask_user_input(
            '', 'test_pass'), ('', 'test_pass'))
        self.assertEqual(bitbucket_api.ask_user_input(
            'test_user', ''), ('test_user', ''))
        self.assertEqual(bitbucket_api.ask_user_input(
            'x', 'x'), ('x', 'x'))

    def test_authenticate_user(self):
        """Test the authentication method for good and bad user credentials"""

        self.assertFalse(bitbucket_api.authenticate_user(
            'bad_username', 'bad_password').get_privileges()[0])
        self.assertFalse(bitbucket_api.authenticate_user(
            '', '').get_privileges()[0])
        self.assertTrue(bitbucket_api.authenticate_user(
            os.environ['BITBUCKET_USER'], os.environ['BITBUCKET_PW']).get_privileges()[0])

    def test_create_repo(self):
        """Test whether repository creation fails/succeeds for given repo names"""

        client = bitbucket_api.authenticate_user(
            os.environ['BITBUCKET_USER'], os.environ['BITBUCKET_PW'])  # Requires environment variables to be set
        self.assertTrue(bitbucket_api.create_repo(
            client, 'this-repo-does-not-exist'))  # Test creation of a repo that does not exist on bitbucket
        self.assertFalse(bitbucket_api.create_repo(
            client, ''))  # Test creation of a repo without a name
        self.assertFalse(bitbucket_api.create_repo(
            client, 'this-repo-does-exist'))  # Test creation of a repo that already exists on bitbucket


if __name__ == "__main__":
    unittest.main()
