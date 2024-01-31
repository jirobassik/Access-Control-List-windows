import os
import pathlib
import subprocess

import click


def create_folder(path, mode, sid):
    folder_path = str(pathlib.Path(f"./{path}").absolute())
    os.makedirs(folder_path)
    subprocess.run(['icacls', folder_path, '/inheritance:r'])
    subprocess.run(['icacls', folder_path, '/grant', f'*S-1-{sid}:{mode}'])


def delete_folder(path):
    pathlib.Path(f"./{path}").rmdir()


def view_folder_content(path):
    click.echo('Folder content:')
    for content in pathlib.Path(f"./{path}").iterdir():
        click.echo(content)


def folder_permission(path):
    result = subprocess.run(['icacls', f"./{path}", '/t'], capture_output=True, text=True, encoding='cp866')
    output = result.stdout
    click.echo(output)
