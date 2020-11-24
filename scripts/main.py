import click

import bitbucket_api


@click.command()
@click.option('--name',  help='Name of the repo you want to create')
@click.option('--mode', default=0,  help='0 = Select Later, 1 = GitHub, 2 = BitBucket')
def start_process(name, mode):
    """Program that creates a repo on your favorite git version control system."""

    if name:
        name = name.lower()
        name = name.replace(' ', '-')
        if mode == 1:
            click.echo("Create repo: " + name + " on GitHub")
            # Code for github repo creation goes here
        elif mode == 2:
            click.echo("Create repo: " + name + " on BitBucket")
            bitbucket_api.run_process(name)
            # Code for bitbucker repo creation goes here
        else:
            click.echo(
                "Please enter a valid mode. 1 = GitHub, 2 = BitBucket. Refer to --help for more information.")

    else:
        click.echo(
            'Please use the --name parameter to enter a name for your repo. E.g --name="my-repo"')
        click.echo(
            'For additional help use the --help command.')


if __name__ == '__main__':
    start_process()
