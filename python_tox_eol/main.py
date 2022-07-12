from functools import partial
from io import TextIOWrapper

import click
import yaml

arg_file = partial(click.option, '--file', type=click.STRING, required=True)

some_dict = {
    'let': 'me',
    'check': 'this'
}


@click.group()
def cli():
    """The CLI"""


@cli.command()
@arg_file()
def unforced(file: str):
    """unforced"""

    with open(file, 'w') as f:
        yaml.dump(some_dict, f)


@cli.command()
@arg_file()
def forced(file: str):
    """forced"""

    with open(file, 'w', newline='\n') as f:
        yaml.dump(some_dict, f, line_break='\n')


@cli.command()
@arg_file()
def forcedbinary(file: str):
    """forced"""

    with open(file, 'wb', newline='\n') as f:
        yaml.dump(some_dict, f, line_break='\n')


@cli.command()
@arg_file()
def extraforced(file: str):
    """extraforced"""

    with CRRemoverTIW(open(file, 'w', newline='\n')) as f:
        yaml.dump(some_dict, f, line_break='\n')


class CRRemoverTIW(TextIOWrapper):
    def write(self, __s: str) -> int:
        return super().write(__s=__s.replace('\r', ''))
