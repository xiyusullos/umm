import click
from click import echo

from src import C
from src.commands import pip, npm

CONTEXT_SETTINGS = {
    'ignore_unknown_options': True
}


@click.group(context_settings=CONTEXT_SETTINGS, help=C.DESCRIPTION)
# @click.command()
# @click.argument('tool')
# @click.option('-v', '--version')
def cli():
    pass


cli.add_command(pip.cli)
cli.add_command(npm.cli)


@cli.command('v', short_help='Show %s version.' % C.NAME)
def version():
    return echo(C.VERSION)


# @cli.command('selfupdate')
# def selfupdate():
#     '''Update umm'''
#     pass

def test_mirrors_yaml():
    for k in C.MIRRORS:
        print(k)


if __name__ == '__main__':
    pass
    cli()
    # test_mirrors_yaml()
