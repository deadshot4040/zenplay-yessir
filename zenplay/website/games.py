import requests

def get_playstation_games(api_key):
    playstation_platform_ids = [9, 48, 49]  # IDs for PlayStation platforms
    all_playstation_games = []

    for platform_id in playstation_platform_ids:
        url = f'https://api.rawg.io/api/games?key={api_key}&platforms={platform_id}'
        response = requests.get(url)

        if response.status_code == 200:
            games_data = response.json().get('results', [])
            all_playstation_games.extend(games_data)
        else:
            print(f"Failed to fetch data for platform {platform_id}")

    return all_playstation_games

if __name__ == "__main__":
    api_key = '4300da9730d641faa00260d28aabff38'
    playstation_games = get_playstation_games(api_key)
    
    print(f"Total PlayStation games collected: {len(playstation_games)}")
