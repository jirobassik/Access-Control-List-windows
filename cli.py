import click
from utils.group import operation_group
from utils.user import add_user, delete_user, user_operation_group, give_admin_user
from utils.folder import create_folder, delete_folder, view_folder_content, folder_permission
from utils.file import create_file, delete_file, set_permission


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
@click.option('--mode', default='RWD', help='''R - read, W - write, D - delete''')
@click.option('--sid', default='1-0', help='''1-0 - all users, 3-0 - owner, 5-11 - all users(exclude owner), 
               5-32-544 - only admin group, 5-32-545 - only user group''')
@click.argument('path')
def create_folder_command(path, mode, sid):
    create_folder(path, mode, sid)


@click.command(name='delete_folder')
@click.argument('path')
def delete_folder_command(path):
    delete_folder(path)


@click.command(name='folder_content')
@click.argument('path')
def view_folder_content_command(path):
    view_folder_content(path)


@click.command(name='check_perm')
@click.argument('path')
def check_permission_command(path):
    folder_permission(path)


@click.command(name='file', help='File operations')
@click.option('--operation', type=click.Choice(['create', 'delete', 'set-permission'], case_sensitive=False),
              required=True)
@click.argument('path')
@click.option('--content', help='File content (only for "create" operation')
@click.option('--permissions', help='Access rights (only for "set-permission" operation')
def file_command(operation, path, content=None, permissions=None):
    if operation == 'create':
        create_file(path, content)
    elif operation == 'delete':
        delete_file(path)
    elif operation == 'set-permission':
        set_permission(path, permissions)


cli.add_command(file_command)
cli.add_command(group_command)
cli.add_command(add_user_command)
cli.add_command(delete_user_command)
cli.add_command(user_operation_group_command)
cli.add_command(admin_user_operation_command)
cli.add_command(create_folder_command)
cli.add_command(delete_folder_command)
cli.add_command(view_folder_content_command)
cli.add_command(check_permission_command)

if __name__ == '__main__':
    cli()
