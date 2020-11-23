from bitbucket.bitbucket import Bitbucket
import getpass


def authenticate_user():
    username = input("Enter email address used on BitBucket: ")
    password = getpass.getpass("Enter password: ")
    client = Bitbucket(username, password)
    return client


def create_repo(client, repo_name):
    success, result = client.repository.create(repo_name)
    return success


def run_process(repo_name):
    client = authenticate_user()
    success = create_repo(client, repo_name)
    if (success):
        print("Repository {} created on Bitbucket".format(repo_name))
    else:
        print("Error while creating repository. Please try again.")
