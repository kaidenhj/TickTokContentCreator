
from config import Config
from migrate import Migrate
from sqlalchemy import SQLAlchemy
import os

app = os.name
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import main, models
