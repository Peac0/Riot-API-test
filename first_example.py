from importlib.metadata import metadata
from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-***' #put your key here
watcher = LolWatcher(api_key)
my_region = 'euw1'

me = watcher.summoner.by_name(my_region, 'mauvaise odeur')

my_matches = watcher.match.matchlist_by_puuid(my_region, me['puuid'])

# fetch last match detail
last_match = my_matches[0]
match_detail = watcher.match.by_id(my_region, last_match)['info']

participants = []
for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championName']
    participants_row['spell1'] = row['spell1Casts']
    participants_row['spell2'] = row['spell2Casts']
    participants_row['win'] = row['win']
    participants_row['kills'] = row['kills']
    participants_row['deaths'] = row['deaths']
    participants_row['assists'] = row['assists']
    participants_row['totalDamageDealt'] = row['totalDamageDealt']
    participants_row['goldEarned'] = row['goldEarned']
    participants_row['champLevel'] = row['champLevel']
    participants_row['totalMinionsKilled'] = row['totalMinionsKilled']
    participants_row['item0'] = row['item0']
    participants_row['item1'] = row['item1']
    participants.append(participants_row)
df = pd.DataFrame(participants)
#print data frame
print(df)
