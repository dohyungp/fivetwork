import os
import unittest
import click
from flask_migrate import Migrate, MigrateCommand
from fivetwork import blueprint
from fivetwork.main import create_app, db
from fivetwork.main.model import blacklist, user, department
from fivetwork.main.service.user_service import create_admin
from frontend import view
from home import home

app = create_app(os.getenv('PROD_ENV') or 'dev')
app.register_blueprint(home)
app.register_blueprint(blueprint)
app.register_blueprint(view)

app.app_context().push()
migrate = Migrate(app, db)


@app.cli.command('db')
def migrate_db():
    """DB Migration tool injection
    """
    MigrateCommand()


@app.cli.command("test")
def test():
    """Unit testing cli command

    :return: result code
    :rtype: int
    """
    tests = unittest.TestLoader().discover('fivetwork/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@app.cli.command('createsuperuser')
@click.option('--username', prompt='Username (leave blank to use "admin")', default='admin')
@click.option('--email', prompt='Email Address')
@click.option('--password', prompt='Password')
@click.option('--password_check', prompt='Password (again)')
def create_super_user(username, email, password, password_check):
    """Create service superuser

    :param username: service admin username
    :type username: string
    :param email: service admin email
    :type email: string
    :param password: service admin password
    :type password: string
    :param password_check: password double check
    :type password_check: string
    """
    assert password == password_check, 'Those passwords did\'nt match.'
    data = dict(username=username, email=email, password=password)
    result = create_admin(data)
    click.echo(result)


if __name__ == '__main__':
    app.run()
