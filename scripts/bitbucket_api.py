from bitbucket.bitbucket import Bitbucket
import getpass


def ask_user_input(username='', password=''):
    """ Ask the user for their bitbucket credentials

    Keyword arguments:
    username -- defaulted to empty string for unit testing
    password -- defaulted to empty string for unit testing
    """

    if username == '' and password == '':
        username = input("Enter email address used on BitBucket: ")
        password = getpass.getpass("Enter password: ")
        return (username, password)
    else:
        return (username, password)


def authenticate_user(username, password):
    """ Authenticate the user with bitbucket api

    Keyword arguments:
    username -- username/email address used for authentication
    password -- password used for authentication
    """

    client = Bitbucket(username, password)
    return client


def create_repo(client, repo_name):
    """ Create a repository on bitbucket using the authenticated user

    Keyword arguments:
    client -- the authenticated user object obtained from authenticate_user()
    repo_name -- the name of the repo that the user wishes to create
    """

    success, result = client.repository.create(repo_name)
    return success


def run_process(repo_name):
    """ Runs the functions to ask the user for their credentials, authenticate the user to bitbucket api
    and create a repo.

    Keyword arguments:
    repo_name -- the name of the repo the user wishes to create
    """

    username, password = ask_user_input()
    client = authenticate_user(username, password)
    success = create_repo(client, repo_name)
    if (success):
        print("Repository {} created on Bitbucket".format(repo_name))
    else:
        print("Error while creating repository. Please try again.")
