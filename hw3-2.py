import urllib.request
import json

def filterWeatherData(year, month):
    if year < 2013 or year > 2019:
        return
    if month < 1 or month > 12:
        return
    i=1
    filteredData = []
    while i <= 31:
        response = urllib.request.urlopen(f'https://www.metaweather.com/api/location/2487956/{year}/{month}/{i}/')
        data = response.read()
        data_str = data.decode("utf-8")
        for weatherData in json.loads(data_str):
            createdDate = weatherData["created"].split('T')[0]
            applicableDate = weatherData["applicable_date"]
            if(createdDate == applicableDate):
                filteredData.append(weatherData)
        i += 1
    return filteredData

def computeAverageEachDay(filteredData):
    if filteredData is None or len(filteredData) < 1:
        return
    averageData = {}
    for data in filteredData:
        if(data['applicable_date'] in averageData.keys()):
            averageData[data['applicable_date']] = (averageData[data['applicable_date']] + data['the_temp']) / 2
        else:
            averageData[data['applicable_date']] = data['the_temp']
    return averageData

def writeAverageDataInFile(averageData):
    if averageData is None or len(averageData) < 1:
        return
    with open('aver_temp.json', 'w') as fp:
        json.dump(averageData, fp, sort_keys=True)


filteredData = filterWeatherData(2019, 8)
averageData = computeAverageEachDay(filteredData)
writeAverageDataInFile(averageData)