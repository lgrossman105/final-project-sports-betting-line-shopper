from app.odds_shopper import get_in_season_sports

def test_api_working():
    assert get_in_season_sports() is not None