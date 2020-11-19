import click


@click.command()
@click.option('--name',  help='Name of the repo you want to create:')
def start_process(name):
    """Program that creates a repo on your favorite git version control system."""

    if name:
        name = name.lower()
        name = name.replace(' ', '-')
        click.echo("You chose to create a repo named: " + name)
    else:
        click.echo(
            'Please use the --name parameter to enter a name for your repo. E.g --name="my-repo"')
        click.echo(
            'For additional help use the --help command.')


if __name__ == '__main__':
    start_process()
