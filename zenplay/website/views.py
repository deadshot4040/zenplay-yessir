from django.shortcuts import render
import requests

def index(request):
    # Define your RAWG API key
    api_key = '4300da9730d641faa00260d28aabff38'
    
    # Initialize an empty list to store all PlayStation games
    all_playstation_games = []
    
    # Define the API endpoint URL with your API key and set up pagination
    page = 1
    per_page = 40  # Adjust this number to control the number of games per page
    url = f'https://api.rawg.io/api/games?key={api_key}&platforms=18&page={page}&page_size={per_page}'  # Platform ID 18 is for PlayStation

    while True:
        # Make a GET request to fetch game data
        response = requests.get(url)

        if response.status_code == 200:
            game_data = response.json()
            # Extract relevant data from the API response
            games = game_data['results']
            all_playstation_games.extend(games)  # Add fetched games to the list

            # Check if there are more pages to fetch
            if game_data['next']:
                page += 1
                url = f'https://api.rawg.io/api/games?key={api_key}&platforms=18&page={page}&page_size={per_page}'
            else:
                break
        else:
            # Handle API request error gracefully
            break

    return render(request, 'index.html', {'games': all_playstation_games})

def meetings(request):
    return render(request, 'meetings.html', {})

def meetingdetails(request):
    return render(request, 'meetingdetails.html')
