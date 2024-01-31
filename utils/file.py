import os
import pathlib
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


def set_permission(path, mode, sid):
    folder_path = str(pathlib.Path(f"./{path}").absolute())
    subprocess.run(['icacls', folder_path, '/inheritance:r'])
    subprocess.run(['icacls', folder_path, '/grant', f'*S-1-{sid}:{mode}'])


def check_file_permissions(path):
    result = subprocess.run('[icacls]', path)
    output = result.stdout
    click.echo(output)
