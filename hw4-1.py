import glob
import json
from collections import Counter

json_files = glob.glob("input/*.json")
# tally = dict()
tally = Counter()

for json_file in json_files:
    with open(json_file, "r") as jf:
        json_dict = json.load(jf)
        print(json_dict)
    # tally[json_dict['user']] = tally.get(json_dict['user'], 0) + json_dict['steps']
    tally.update({json_dict['user'] : json_dict['steps']})

# leaderboard = sorted(tally.items(), key=lambda x: x[1], reverse=True)
# for item in leaderboard:
#     print(item)

print(tally.most_common())

with open ("leaderboard-4.csv", "w") as f:
    # for id, steps in leaderboard:
    for id, steps in tally.most_common():
        f.write(f"{id},{steps}\n")