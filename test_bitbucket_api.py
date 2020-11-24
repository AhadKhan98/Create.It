import unittest
import bitbucket_api
import os

# Set bitbucket credentials to test methods that require authenticated user
os.environ['BITBUCKET_USER'] = 'ENTER YOUR BITBUCKET USERNAME HERE'
os.environ['BITBUCKET_PW'] = 'ENTER YOUR BITBUCKET PASSWORD HERE'


class TestBitbucketAPI(unittest.TestCase):

    def test_ask_user_input(self):
        self.assertEqual(bitbucket_api.ask_user_input(
            'test_user', 'test_pass'), ('test_user', 'test_pass'))
        self.assertEqual(bitbucket_api.ask_user_input(
            '', 'test_pass'), ('', 'test_pass'))
        self.assertEqual(bitbucket_api.ask_user_input(
            'test_user', ''), ('test_user', ''))
        self.assertEqual(bitbucket_api.ask_user_input(
            'x', 'x'), ('x', 'x'))

    def test_authenticate_user(self):
        self.assertFalse(bitbucket_api.authenticate_user(
            'bad_username', 'bad_password').get_privileges()[0])
        self.assertFalse(bitbucket_api.authenticate_user(
            '', '').get_privileges()[0])
        self.assertTrue(bitbucket_api.authenticate_user(
            os.environ['BITBUCKET_USER'], os.environ['BITBUCKET_PW']).get_privileges()[0])

    def test_create_repo(self):
        # Valid & Authenticated User
        client = bitbucket_api.authenticate_user(
            os.environ['BITBUCKET_USER'], os.environ['BITBUCKET_PW'])
        self.assertTrue(bitbucket_api.create_repo(
            client, 'this-repo-does-not-exist'))
        self.assertFalse(bitbucket_api.create_repo(
            client, ''))
        self.assertFalse(bitbucket_api.create_repo(
            client, 'this-repo-does-exist'))


if __name__ == "__main__":
    unittest.main()
