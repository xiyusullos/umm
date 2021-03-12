#!/usr/bin/env python

import click
from click import echo

from . import C
from .commands import pip, npm, composer, brew

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
cli.add_command(composer.cli)
cli.add_command(brew.cli)


@cli.command('v', short_help='Show %s version.' % C.NAME)
def version():
    return echo(C.VERSION)


# @cli.command('selfupdate')
# def selfupdate():
#     '''Update umm'''
#     pass


if __name__ == '__main__':
    pass
    cli()
