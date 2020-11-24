from bitbucket.bitbucket import Bitbucket
import getpass


def ask_user_input(username='', password=''):
    if username == '' and password == '':
        username = input("Enter email address used on BitBucket: ")
        password = getpass.getpass("Enter password: ")
        return (username, password)
    else:
        return (username, password)


def authenticate_user(username, password):
    client = Bitbucket(username, password)
    print(client.get_privileges()[0])
    return client


def create_repo(client, repo_name):
    success, result = client.repository.create(repo_name)
    return success


def run_process(repo_name):
    username, password = ask_user_input()
    client = authenticate_user(username, password)
    success = create_repo(client, repo_name)
    if (success):
        print("Repository {} created on Bitbucket".format(repo_name))
    else:
        print("Error while creating repository. Please try again.")
