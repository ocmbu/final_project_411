import time

import pytest

from app.models import User
from app.models import Favorite
from app.favorite_model import FavoriteLocationModel


@pytest.fixture
def sample_boxer1(session):
    boxer = Boxers(name="Muhammad Ali", weight=210, height=191, reach=78, age=32)
    session.add(boxer)
    session.commit()
    return boxer