from matplotlib import lines
from requests import get
from json import dumps
import datetime
import csv
import os

#if os.path.exists(os.path.expanduser('~') + '/.config/conky/covidStats.csv'):
#    os.remove(os.path.expanduser('~') + '/.config/conky/covidStats.csv')
#if os.path.exists(os.path.expanduser('~') + '/.config/conky/dailyCases.png'):
#    os.remove(os.path.expanduser('~') + '/.config/conky/dailyCases.png')
#if os.path.exists(os.path.expanduser('~') + '/.config/conky/dailyDeaths.png'):
#    os.remove(os.path.expanduser('~') + '/.config/conky/dailyDeaths.png')

today = datetime.datetime.now()
strToday = today.strftime("       Last Updated: %H:%M %d/%m/%Y")


ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"
AREA_TYPE = "overview"

filters = [
    f"areaType={ AREA_TYPE }"
]

structure = {
    "date": "date",
    "name": "areaName",
    "code": "areaCode",
    "dailyCases": "newCasesByPublishDate",
    "totCases": "cumCasesByPublishDate",
    "dailyDeaths": "newDeaths28DaysByPublishDate",
    "totDeaths": "cumDeaths28DaysByPublishDate",
    "daily1Vac": "newPeopleVaccinatedFirstDoseByPublishDate",
    "daily2Vac": "newPeopleVaccinatedSecondDoseByPublishDate",
    "daily3Vac": "newPeopleVaccinatedThirdInjectionByPublishDate",
    "tot1Vac": "cumPeopleVaccinatedFirstDoseByPublishDate",
    "tot2Vac": "cumPeopleVaccinatedSecondDoseByPublishDate",
    "tot3Vac": "cumPeopleVaccinatedThirdInjectionByPublishDate"
}

api_params = {
    "filters": str.join(";", filters),
    "structure": dumps(structure, separators=(",", ":"))
}


response = get(ENDPOINT, params=api_params, timeout=10)
resJson = response.json()
if response.status_code >= 400:
    f = open(os.path.expanduser('~') + "/.config/conky/requestLog.txt", "a")
    f.write("\n" + today.strftime("%H:%M %d/%m/%Y") + "Request failed")
    f.close()
    raise RuntimeError(f'Request failed: { response.text }')
    
    quit()


#print(response.url)
t_Cases = resJson['data'][0]['dailyCases']
t_Deaths = resJson['data'][0]['dailyDeaths']
t_1Vac = resJson['data'][1]['daily1Vac']
t_2Vac = resJson['data'][1]['daily2Vac']
t_3Vac = resJson['data'][1]['daily3Vac']
y_Cases = resJson['data'][1]['dailyCases']
y_Deaths = resJson['data'][1]['dailyDeaths']
y_1Vac = resJson['data'][2]['daily1Vac']
y_2Vac = resJson['data'][2]['daily2Vac']
y_3Vac = resJson['data'][2]['daily3Vac']
T_Cases = resJson['data'][0]['totCases']
T_Deaths = resJson['data'][0]['totDeaths']
T_1Vac = resJson['data'][1]['tot1Vac']
T_2Vac = resJson['data'][1]['tot2Vac']
T_3Vac = resJson['data'][1]['tot3Vac']
strToday = "             Last Updated: " + str(resJson['data'][0]['date'])

if t_Cases > y_Cases:
    p_Cases = "↑" + str(round(((t_Cases / y_Cases) * 100)-100,1)) + "%"
else:
    p_Cases = "↓" + str(round(100-((t_Cases / y_Cases) * 100),1)) + "%"

if t_Deaths > y_Deaths:
    p_Deaths = "↑" + str(round(((t_Deaths / y_Deaths) * 100)-100,1)) + "%"
else:
    p_Deaths = "↓" + str(round(100-((t_Deaths / y_Deaths) * 100),1)) + "%"

if t_1Vac > y_1Vac:
    p_1Vac = "↑" + str(round(((t_1Vac / y_1Vac) * 100)-100,1)) + "%"
else:
    p_1Vac = "↓" + str(round(100-((t_1Vac / y_1Vac) * 100),1)) + "%"

if t_2Vac > y_2Vac:
    p_2Vac = "↑" + str(round(((t_2Vac / y_2Vac) * 100)-100,1)) + "%"
else:
    p_2Vac = "↓" + str(round(100-((t_2Vac / y_2Vac) * 100),1)) + "%"

if t_3Vac > y_3Vac:
    p_3Vac = "↑" + str(round(((t_3Vac / y_3Vac) * 100)-100,1)) + "%"
else:
    p_3Vac = "↓" + str(round(100-((t_3Vac / y_3Vac) * 100),1)) + "%"

#Exporting to CSV
csv_data = resJson['data']
data_file = open(os.path.expanduser('~') + '/.config/conky/covidStats.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0
 
for row in csv_data:
    if count == 0:
        header = row.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(row.values())
 
data_file.close()

import pandas
import matplotlib.pyplot as plt

array = [['3','dailyCases','Daily Cases'],['5','dailyDeaths','Daily Deaths']]

for each in array:
    df = pandas.read_csv(os.path.expanduser('~') + '/.config/conky/covidStats.csv', delimiter=',', 
                     usecols=[0,int(each[0])], infer_datetime_format=True,
                     parse_dates=True, date_parser=pandas.to_datetime,
                     nrows=30, )

    dfRev = df[::-1].reset_index(drop=True)
    dfRev['rolling_avg'] = round(dfRev.rolling(window = 7).mean(),0)
    dfRev.plot(legend=False, color=["green", "white"],linewidth=2.0)
    plt.axis('off')
    plt.title(str(each[2]), color="white",fontsize=20)
    plt.savefig(os.path.expanduser('~') + '/.config/conky/' + str(each[1])+'.png',bbox_inches='tight', transparent=True, pad_inches=0.01)

#Write out the summary text
f = open(os.path.expanduser('~') + "/.config/conky/covid.txt", "w")
f.write("       Today   Yest.  Total    Diff.")
f.write("\nCases  " + str(t_Cases) + " " * (8 - len(str(t_Cases))) + str(y_Cases) + " " * (7 - len(str(y_Cases))) + str(T_Cases) + " " * (9 - len(str(T_Cases))) + p_Cases)
f.write("\nDeaths " + str(t_Deaths) + " " * (8 - len(str(t_Deaths))) + str(y_Deaths) + " " * (7 - len(str(y_Deaths))) + str(T_Deaths) + " " * (9 - len(str(T_Deaths))) + p_Deaths)
f.write("\n1 Vac. " + str(t_1Vac) + " " * (8 - len(str(t_1Vac))) + str(y_1Vac) + " " * (7 - len(str(y_1Vac))) + str(T_1Vac) + " " * (9 - len(str(T_1Vac))) + p_1Vac)
f.write("\n2 Vac. " + str(t_2Vac) + " " * (8 - len(str(t_2Vac))) + str(y_2Vac) + " " * (7 - len(str(y_2Vac))) + str(T_2Vac) + " " * (9 - len(str(T_2Vac))) + p_2Vac)
f.write("\nB Vac. " + str(t_3Vac) + " " * (8 - len(str(t_3Vac))) + str(y_3Vac) + " " * (7 - len(str(y_3Vac))) + str(T_3Vac) + " " * (9 - len(str(T_3Vac))) + p_3Vac)
f.write("\n"+strToday)
f.close()

os.system('cat ' + os.path.expanduser('~') + "/.config/conky/covid.txt")

f = open(os.path.expanduser('~') + "/.config/conky/requestLog.txt", "a")
f.write("\n" + today.strftime("%H:%M %d/%m/%Y") + ": Request succeeded!")
f.close()