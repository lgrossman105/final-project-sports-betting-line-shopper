from app.odds_shopper import get_in_season_sports, get_odds, process_odds
import pandas as pd
def test_api_working():
    assert isinstance(get_in_season_sports(), list)

def lines_data_test():
    assert isinstance(get_odds, pd.DataFrame )

def test_process_odds_picks_best_totals():
    test_data = {
        'bookmakers': [[
            {
                'title': 'DraftKings',
                'markets': [{'outcomes': [
                    {'name': 'Over', 'price': -110, 'point': 45.5},
                    {'name': 'Under', 'price': -110, 'point': 45.5}
                ]}]
            },
            {
                'title': 'FanDuel',
                'markets': [{'outcomes': [
                    {'name': 'Over', 'price': -105, 'point': 44.5}, 
                    {'name': 'Under', 'price': -115, 'point': 46.5}  
                ]}]
            }
        ]],
        'commence_time': ['2025-01-01T00:00:00Z']
    }
    df = pd.DataFrame(test_data)
    
    result = process_odds(df, type="totals")
    
    # Assert FanDuel was picked for the better Over line (44.5 < 45.5)
    assert result.at[0, 'one_sportsbook'] == 'FanDuel'
    assert result.at[0, 'one_line'] == 44.5