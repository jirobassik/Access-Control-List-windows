import os
import subprocess

import click


def create_file(path, content):
    with open(path, 'w') as file:
        file.write(content)
    click.echo(f"File '{path}' created successfully !")


def delete_file(path):
    try:
        os.remove(path)
        click.echo(f"File '{path}' deleted successfully!")
    except OSError as e:
        click.echo(f"There is some troubles with delete file '{path}': {str(e)}")


def set_permission(path, permissions):
    subprocess.run(['icacls', path, '/inheritance:d', '/grant', permissions])
    click.echo(f"Access rights for file '{path}' changed successfully for '{permissions}'!")