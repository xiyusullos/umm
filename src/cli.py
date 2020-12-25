import click

from click import echo

from src import utils, C

CONTEXT_SETTINGS = {
    'ignore_unknown_options': True
}


@click.group(context_settings=CONTEXT_SETTINGS)
# @click.command()
# @click.argument('tool')
# @click.option('tool')
def cli():
    '''A toolkit to manager the fastest mirror of various tools, such as pip, npm, composer and etc.'''
    # echo('umm')
    pass


# cli.add_command(pip_.cli)


# @click.group()
# def pip():
#     '''Manage pip mirrors '''
#     pass
#
#
# @pip.command()
# def ls():
#     ''''''
#     pass


# import src.pip_.cli as pip
# cli = click.CommandCollection(sources=[pip])

from src.commands import pip
cli.add_command(pip.cli)

# @cli.command('version')
# def version():
#     '''Show umm's version.'''
#     echo(config.VERSION)
#
# @cli.command('selfupdate')
# def selfupdate():
#     '''Update umm'''
#     pass

if __name__ == '__main__':
    cli()
    print(utils.MACHINE)