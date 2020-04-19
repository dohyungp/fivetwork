from pathlib import Path
from flask_testing import TestCase
from dotenv import load_dotenv
from fivetwork.main import db
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('fivetwork.main.config.TestingConfig')
        root_dir = Path(__file__).absolute().parents[2]
        env_file = root_dir.joinpath('.flaskenv')
        load_dotenv(env_file)
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
