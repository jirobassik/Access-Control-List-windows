import click
from utils.group import operation_group
from utils.user import add_user, delete_user, user_operation_group, give_admin_user
from utils.folder import create_folder, folder_permission
from utils.validators import validate_mode_file


@click.group()
def cli():
    pass


@click.command(name='group', help='Group operations')
@click.option('--operation', type=click.Choice(['add', 'delete'], case_sensitive=True), required=True)
@click.argument('name')
def group_command(name, operation):
    operation_group(name, operation)


@click.command(name='delete_user', help='Delete user')
@click.argument('name')
@click.confirmation_option(prompt='Are you sure you want to delete user?')
def delete_user_command(name):
    delete_user(name)


@click.command(name='add_user', help='Add user')
@click.argument('name')
def add_user_command(name):
    password = click.prompt('Please enter the password', hide_input=True)
    add_user(name, password)


@click.command(name='user_oper_group', help='User group operations')
@click.option('--operation', type=click.Choice(['add', 'delete'], case_sensitive=True), required=True)
@click.argument('group_name')
@click.argument('user_name')
def user_operation_group_command(group_name, user_name, operation):
    user_operation_group(group_name, user_name, operation)


@click.command(name='admin_oper', help='Give or remove administrator rights')
@click.option('--operation', type=click.Choice(['add', 'delete'], case_sensitive=True), required=True)
@click.argument('name')
@click.confirmation_option(prompt='Are you sure you want to give or remove rights for user?')
def admin_user_operation_command(name, operation):
    give_admin_user(name, operation)


@click.command(name='create_folder')
@click.argument('path')
@click.argument('mode', callback=validate_mode_file)
def create_folder_command(path, mode):
    create_folder(path, mode)


@click.command(name='check_perm')
@click.argument('path')
def check_permission_command(path):
    folder_permission(path)


cli.add_command(group_command)
cli.add_command(add_user_command)
cli.add_command(delete_user_command)
cli.add_command(user_operation_group_command)
cli.add_command(admin_user_operation_command)
cli.add_command(create_folder_command)
cli.add_command(check_permission_command)

if __name__ == '__main__':
    cli()