# Prompt user of the name of nba player for stats
#     Get authorization for NBA API
#     If data is already in our built database then fetch from there
#         else Fetch data pertaining to player from API
#     Add data to the database
#     Return important stats on the player
#     URL for API: https://pypi.org/project/nba-api/

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

loop = 1
player = {}
while(loop):
    nba_name = input("Enter an NBA Player's name: ")
    player = players.find_players_by_full_name(nba_name)
    if player == []:
        print("There was no player found matching the name you provided")
    else:
        loop = 0
print(player)


# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)
print(player_info)
