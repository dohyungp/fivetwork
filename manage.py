import os
import unittest
import click
from flask_migrate import Migrate, MigrateCommand
from app import blueprint
from app.main import create_app, db
from app.main.model import blacklist, user
from app.main.service.user_service import create_admin

app = create_app(os.getenv('PROD_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()
migrate = Migrate(app, db)


@app.cli.command('db')
def migrate_db():
    """Run Database Migration"""
    MigrateCommand()


@app.cli.command("test")
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
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
    """Create super user in CLI"""
    assert password == password_check, 'Those passwords did\'nt match.'
    data = dict(username=username, email=email, password=password)
    result = create_admin(data)
    click.echo(result)


if __name__ == '__main__':
    app.run()
