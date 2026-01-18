import json
import numpy as np
import pandas as pd
from total_json_return import json_files,json_id 

all_matches = []

def teamscore_fun(match_data,inning):
    try:
        inning_overs = match_data['innings'][inning]['overs']
        s_total =0 #total val for a inning
    
        for over_data in inning_overs:
            over_number = over_data['over'] # Gets 0, 1, 2...
        
            for ball in over_data['deliveries']:
                s_total+=int(ball['runs']['total'])
        return s_total
    except:
        return 0

for jsonz, id in zip(json_files ,json_id):
    with open(jsonz) as f:
        match_data = json.load(f)

    total_first =teamscore_fun(match_data,0)
    total_second =teamscore_fun(match_data,1)

    teams = match_data['info']['teams']
    city = match_data['info']['city']
    try:
        winner = match_data['info']['outcome']['winner']
    except:
        winner = match_data['info']['outcome']['result']

    match_result = {
        "ID" : id,
        "City"  : city,
        "Team A": teams[0],
        "First Inning" : total_first,
        "Team B" : teams[1],
        "Second Inning" : total_second,
        "Winner" : winner
    }

    all_matches.append(match_result)



df = pd.DataFrame(all_matches)

def show_dataframe():
    print(df)