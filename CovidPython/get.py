from requests import get
import json


def get_data(url):
    response = get(endpoint, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=overview&'
        'structure={"date":"date","newCases":"newCasesByPublishDate", "newDeaths":"newDeaths28DaysByPublishDate", "cumCases":"cumCasesByPublishDate", "cumDeaths":"cumDeaths28DaysByPublishDate"}'
    )
    
    data = get_data(endpoint)

    for each in json.data("data"):
        print(each)
    ##print(json.dumps(data, indent=4))