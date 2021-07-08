# Prompt user of the name of nba player for stats
#     Get authorization for NBA API
#     If data is already in our built database then fetch from there
#         else Fetch data pertaining to player from API
#     Add data to the database
#     Return important stats on the player
#     URL for API: https://pypi.org/project/nba-api/

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
import requests

loop = 1
player = {}
while(loop):
    nba_name = input("Enter an NBA Player's name: ")
    player = players.find_players_by_full_name(nba_name)
    if player == []:
        print("There was no player found matching the name you provided")
    else:
        loop = 0
print(player[0])
user_id = player[0].get("id")
print(user_id)


# Basic Request
custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
player_info = commonplayerinfo.CommonPlayerInfo(player_id=user_id, headers=custom_headers, timeout=100)
print(player_info.available_seasons.get_dict())