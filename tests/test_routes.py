import time

import pytest

from app.models import User
from app.models import Favorite
from app.favorite_model import FavoriteLocationModel

@pytest.fixture
def Favlocation_model():
    """ comment here """
    return FavoriteLocationModel()

def test_already_favorite(caplog):
    """Test that adding already favorited location shoing error"""
    model = FavoriteLocationModel()
    model.add_favorite(1, "BU")
    
    with pytest.raises(ValueError) as exc_info:
        model.add_favorite(1, "BU")

    assert str(exc_info.value) == "BU is already favorited"
    
