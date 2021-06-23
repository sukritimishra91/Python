import json
import zipfile
import csv


def saveUserSteps(file_name):
    if len(file_name) < 0:
        return
    userSteps = {}
    with zipfile.ZipFile(file_name,'r') as file:
        for finfo in file.infolist():
            ifile = file.open(finfo)
            line_list = ifile.readlines()
            if(len(line_list) > 0):
                jsonObj = json.loads(line_list[0])
                if jsonObj["user"] in userSteps.keys():
                    userSteps[jsonObj["user"]] += jsonObj["steps"]
                else:
                    userSteps[jsonObj["user"]] = jsonObj["steps"]
    sortedUserSteps = sorted(userSteps.items(), key=lambda x: x[1], reverse=True)
    rows = [['user', 'steps']]
    for value in sortedUserSteps:
        rows.append([value[0], value[1]])
    with open('leaderboard.csv','w') as writeFile:
        writer = csv.writer(writeFile)
        for row in rows:
            writer.writerow(row)
    writeFile.close()

saveUserSteps('input.zip')
